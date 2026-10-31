# parsing/tesseract_spatial_extractor.py
import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path
from typing import List
from parsing.spatial_extractor_interface import ISpatialExtractor
from domain.models.text_element import TextElement
from config.ocr_settings import OcrSettings

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class TesseractSpatialExtractor(ISpatialExtractor):
    def extract_elements(self, file_path: str) -> List[TextElement]:
        elements = []

        # המרת ה-PDF הסרוק לתמונות
        images = convert_from_path(
            file_path,
            dpi=OcrSettings.DEFAULT_DPI,
            poppler_path=r"C:\Users\User\Documents\poppler\poppler-26.09.0\Library\bin"
        )

        for image in images:
            # חילוץ נתונים מרחביים במקום טקסט שטוח
            data = pytesseract.image_to_data(
                image,
                lang=OcrSettings.LANGUAGE_HEBREW_ENGLISH,
                config=OcrSettings.CUSTOM_CONFIG,  # ודא שמוגדר --psm 6 ב-OCR Settings
                output_type=Output.DICT
            )

            n_boxes = len(data['text'])
            for i in range(n_boxes):
                text = data['text'][i].strip()

                # סינון זיהויים ריקים או רעשי רקע
                if text:
                    # המרת המידות של Tesseract לקואורדינטות מוחלטות
                    x0 = float(data['left'][i])
                    top = float(data['top'][i])
                    width = float(data['width'][i])
                    height = float(data['height'][i])

                    elements.append(
                        TextElement(
                            text=text,
                            x0=x0,
                            top=top,
                            x1=x0 + width,  # חישוב נקודת הסיום האופקית
                            bottom=top + height  # חישוב נקודת הסיום האנכית
                        )
                    )

        return elements