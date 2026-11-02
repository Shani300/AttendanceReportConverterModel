import cv2
import numpy as np
import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path
from PIL import Image
from typing import List
from parsing.spatial_extractor_interface import ISpatialExtractor
from domain.models.text_element import TextElement
from config.ocr_settings import OcrSettings

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class TesseractSpatialExtractor(ISpatialExtractor):

    def _preprocess_image(self, pil_image: Image.Image) -> Image.Image:
        """עיבוד מקדים מתקדם לחידוד טקסט ותאריכים"""
        open_cv_image = np.array(pil_image)
        gray = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)

        # 1. הגדלת התמונה (Upscaling) פי 2
        # פעולה זו מעבה את הפיקסלים של תווים קטנים (כמו '/' ו-':') ומונעת את מחיקתם בשלב הבא.
        gray = cv2.resize(gray, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

        # 2. סף אדפטיבי (Adaptive Thresholding) במקום סף קבוע
        # סף קבוע (150) נכשל כשהסריקה מעט חשוכה או בהירה באזורים שונים.
        # הסף האדפטיבי בודק כל בלוק פיקסלים בנפרד (כאן בגודל 31x31) ומייצר שחור-לבן נקי ומדויק.
        thresh = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31, 2
        )

        return Image.fromarray(thresh)

    def extract_elements(self, file_path: str) -> List[TextElement]:
        elements = []

        images = convert_from_path(
            file_path,
            dpi=OcrSettings.DEFAULT_DPI,
            poppler_path=r"C:\Users\User\Documents\poppler\poppler-26.09.0\Library\bin"
        )

        for image in images:
            processed_image = self._preprocess_image(image)

            data = pytesseract.image_to_data(
                processed_image,
                lang=OcrSettings.LANGUAGE_MIXED,
                config=OcrSettings.SPATIAL_CONFIG,
                output_type=Output.DICT
            )

            # כיוון שהגדלנו את התמונה פי 2 בעיבוד המקדים, עלינו לחלק את
            # הקואורדינטות המוחזרות ב-2 כדי שישמרו על פרופורציית הדף המקורית
            scale_factor = 2.0

            n_boxes = len(data['text'])
            for i in range(n_boxes):
                text = data['text'][i].strip()

                if text:
                    x0 = float(data['left'][i]) / scale_factor
                    top = float(data['top'][i]) / scale_factor
                    width = float(data['width'][i]) / scale_factor
                    height = float(data['height'][i]) / scale_factor

                    elements.append(
                        TextElement(
                            text=text,
                            x0=x0,
                            top=top,
                            x1=x0 + width,
                            bottom=top + height
                        )
                    )
        print("elements:")
        print(elements)
        return elements
