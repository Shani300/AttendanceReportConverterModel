# config/ocr_log_messages.py
class OcrLogMessages:
    PROCESSING_START = "Starting OCR processing for file: %s"
    PROCESSING_SUCCESS = "Successfully extracted text from file: %s"
    CONVERSION_ERROR = "Failed to convert PDF to images: %s"
    EXTRACTION_ERROR = "OCR extraction failed on page %d: %s"
    INACCURACY_WARNING = "Potential OCR inaccuracy detected: Empty or whitespace-only output on page %d"