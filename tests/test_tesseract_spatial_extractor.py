import pytest
from parsing.tesseract_spatial_extractor import TesseractSpatialExtractor
from domain.models.text_element import TextElement
import pytesseract
from unittest.mock import patch, MagicMock


@patch('parsing.tesseract_spatial_extractor.convert_from_path')
@patch('parsing.tesseract_spatial_extractor.pytesseract.image_to_data')
def test_extract_elements_returns_list_of_text_elements(mock_image_to_data, mock_convert_from_path):
    # הדמיית פלט ה-OCR מ-image_to_data כמילון
    mock_image_to_data.return_value = {
        'text': ['כותרת', ' ', '123'],
        'left': [10, 50, 100],
        'top': [20, 20, 20],
        'width': [30, 10, 20],
        'height': [15, 15, 15]
    }

    # הדמיית המרת ה-PDF לתמונה (מחזיר תמונה ריקה אחת לדוגמה)
    mock_convert_from_path.return_value = [MagicMock()]

    extractor = TesseractSpatialExtractor()
    elements = extractor.extract_elements("dummy_path.pdf")

    assert isinstance(elements, list)
    assert len(elements) == 2  # המילה הריקה ' ' סוננה

    assert isinstance(elements[0], TextElement)
    assert elements[0].text == 'כותרת'
    assert elements[0].x0 == 10
    assert elements[0].top == 20
    assert elements[0].x1 == 40  # x0 + width
    assert elements[0].bottom == 35  # top + height

    assert elements[1].text == '123'
    assert elements[1].x0 == 100
    assert elements[1].x1 == 120