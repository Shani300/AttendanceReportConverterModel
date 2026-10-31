# parsing/tesseract_spatial_extractor.py
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
        """המרת התמונה לפורמט OpenCV וביצוע חידוד שחור-לבן"""
        # המרה למערך פיקסלים
        open_cv_image = np.array(pil_image)

        # המרה לצבעי אפור
        gray = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)

        # ניגודיות אגרסיבית (Thresholding) - הופך רקע ללבן ואותיות לשחור מוחלט
        # ערך ה-150 הוא סף הרגישות. כל פיקסל כהה מ-150 יהפוך לשחור.
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # חזרה לאובייקט PIL עבור Tesseract
        return Image.fromarray(thresh)

    def extract_elements(self, file_path: str) -> List[TextElement]:
        elements = []

        images = convert_from_path(
            file_path,
            dpi=OcrSettings.DEFAULT_DPI,
            poppler_path=r"C:\Users\User\Documents\poppler\poppler-26.09.0\Library\bin"
        )

        for image in images:
            # הפעלת עיבוד התמונה לפני החילוץ
            processed_image = self._preprocess_image(image)

            data = pytesseract.image_to_data(
                processed_image,
                lang=OcrSettings.LANGUAGE_HEBREW_ENGLISH,
                config=OcrSettings.CUSTOM_CONFIG,
                output_type=Output.DICT
            )

            n_boxes = len(data['text'])
            for i in range(n_boxes):
                text = data['text'][i].strip()

                if text:
                    x0 = float(data['left'][i])
                    top = float(data['top'][i])
                    width = float(data['width'][i])
                    height = float(data['height'][i])

                    elements.append(
                        TextElement(
                            text=text,
                            x0=x0,
                            top=top,
                            x1=x0 + width,
                            bottom=top + height
                        )
                    )

        return elements