class ReportTypes:
    TYPE_A = "TYPE_A"
    TYPE_B = "TYPE_B"
    UNKNOWN = "UNKNOWN"


class ReportKeywords:
    TYPE_A_MARKERS = [
        "150%,",
        " 125%",
        "100%",
        "נסיעות",
        "בונוס",
        "הפסקה"
    ]

    TYPE_B_MARKERS = [
        "כרטיס עובד לחודש",
        "הערות",
    ]

class PipelineConfig:
    OUTPUT_FILE_PATH = "output/type_a_final_report.csv"
    DATE_PATTERN = r"\d{2}/\d{2}/\d{4}"

class TypeAColumns:
    DATE = "תאריך"
    DAY = "יום"
    LOCATION = "מקום"
    ENTRY = "כניסה"
    EXIT = "יציאה"
    BREAK = "הפסקה"
    TOTAL = "סה\"כ"
    HOURS_100 = "100%"
    HOURS_125 = "125%"
    HOURS_150 = "150%"
    SHABBAT = "שבת"

    HEADERS = [DATE, DAY, LOCATION, ENTRY, EXIT, BREAK, TOTAL, HOURS_100, HOURS_125, HOURS_150, SHABBAT]