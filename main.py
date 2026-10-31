from parsing.tesseract_spatial_extractor import TesseractSpatialExtractor
from parsing.spatial_grouper import SpatialGrouper


def main():
    file_path_a = "docs/type_a_2.pdf"
    file_path_b = "docs/type_b_1.pdf"

    # 1. שלב החילוץ: קבלת כל המילים עם הקואורדינטות שלהן
    extractor = TesseractSpatialExtractor()
    elements = extractor.extract_elements(file_path_a)

    # 2. שלב הקיבוץ: סידור המילים לשורות הגיוניות
    grouper = SpatialGrouper()
    spatial_lines = grouper.group_into_lines(elements)

    # 3. הדפסת התוצאה לבדיקה (וידוא שהמספרים צמודים לכותרות)
    for line in spatial_lines:
        line_text = " ".join([el.text for el in line])
        print(line_text)


if __name__ == "__main__":
    main()