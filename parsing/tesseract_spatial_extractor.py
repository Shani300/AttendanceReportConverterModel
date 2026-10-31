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

    # בתוך הקובץ: parsing/tesseract_spatial_extractor.py

    def _preprocess_image(self, pil_image: Image.Image) -> Image.Image:
        """המרת התמונה לפורמט OpenCV, חידוד והעלמת קווי רשת של טבלאות"""
        open_cv_image = np.array(pil_image)
        gray = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)

        # 1. המרה לתמונה בינארית הפוכה (רקע שחור, טקסט וקווים בלבן)
        # זה נדרש כדי שהפעולות המורפולוגיות של OpenCV יעבדו נכון על האובייקטים המוארים
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        # 2. זיהוי והסרת קווים אנכיים (עמודות טבלה)
        # יצירת "מברשת" אנכית ארוכה. רק רצף פיקסלים באורך 20 ומעלה יזוהה כקו
        vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 20))
        vertical_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
        # החסרת הקווים האנכיים מהתמונה המקורית
        thresh = cv2.subtract(thresh, vertical_lines)

        # 3. זיהוי והסרת קווים אופקיים (שורות טבלה)
        # יצירת "מברשת" אופקית ארוכה
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
        horizontal_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
        # החסרת הקווים האופקיים
        thresh = cv2.subtract(thresh, horizontal_lines)

        # 4. חזרה לתמונה רגילה (רקע לבן, טקסט שחור)
        result = cv2.bitwise_not(thresh)

        return Image.fromarray(result)

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