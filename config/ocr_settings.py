# class OcrSettings:
#     LANGUAGE_HEBREW_ENGLISH = "eng+heb"
#     DEFAULT_DPI = 300
#     CUSTOM_CONFIG = "--oem 3 --psm 11"
class OcrSettings:

    DEFAULT_DPI = 300

    LANGUAGE_MIXED = "heb+eng"
    LANGUAGE_HEBREW = "heb"
    LANGUAGE_NUMERIC = "eng"

    # Used to detect individual text elements and their coordinates
    SPATIAL_CONFIG = "--oem 1 --psm 11"

    # Used for individual columns
    COLUMN_CONFIG = "--oem 1 --psm 6"

    # Used for individual rows or cells
    CELL_CONFIG = "--oem 1 --psm 7"

    TESSERACT_CMD = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    DATE_CONFIG = (
        "--oem 1 --psm 6 "
        "-c tessedit_char_whitelist=0123456789/"
    )

    TIME_CONFIG = (
        "--oem 1 --psm 6 "
        "-c tessedit_char_whitelist=0123456789:"
    )

    NUMBER_CONFIG = (
        "--oem 1 --psm 6 "
        "-c tessedit_char_whitelist=0123456789."
    )

    POPPLER_PATH = (
        r"C:\Users\User\Documents\poppler"
        r"\poppler-26.09.0\Library\bin"
    )