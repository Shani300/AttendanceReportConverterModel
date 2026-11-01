import os
import pytest
from domain.models.attendance_report import AttendanceReport
from domain.models.base_report_metadata import BaseReportMetadata
from domain.models.base_report_summary import BaseReportSummary
from domain.models.type_a_row import TypeARow
from generation.csv_generator import CsvGenerator
from generation.html_generator import HtmlGenerator
from generation.excel_generator import ExcelGenerator

TEST_OUTPUT_DIR = "tests/test_outputs"

@pytest.fixture
def sample_report():
    rows = [
        TypeARow(
            date="01/01/2023", day_of_week="ראשון", work_location="ירושלים", entry_time="08:00", exit_time="16:00",
            break_time="00:30", total_hours="07:30", hours_100="07:30", hours_125="00:00", hours_150="00:00", shabbat_hours="00:00"
        ),
        TypeARow(
            date="02/01/2023", day_of_week="שני", work_location="ירושלים", entry_time="08:30", exit_time="16:30",
            break_time="00:30", total_hours="07:30", hours_100="07:30", hours_125="00:00", hours_150="00:00", shabbat_hours="00:00"
        )
    ]
    return AttendanceReport(
        report_type="TYPE_A",
        metadata=BaseReportMetadata(),
        rows=rows,
        summary=BaseReportSummary(),
    )

def setup_module(module):
    os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)


def test_csv_generator_creates_file(sample_report):
    output_path = os.path.join(TEST_OUTPUT_DIR, "test_report.csv")
    generator = CsvGenerator()

    # הפעלת המחולל
    generator.generate(sample_report, output_path)

    # בדיקה שהקובץ אכן נוצר
    assert os.path.exists(output_path)

    # בדיקה בסיסית שהקובץ אינו ריק (גודלו גדול מ-0)
    assert os.path.getsize(output_path) > 0

    # מחיקת הקובץ לאחר הבדיקה (אופציונלי - כדי לשמור על סביבה נקייה)
    if os.path.exists(output_path):
        os.remove(output_path)


def test_html_generator_creates_file(sample_report):
    output_path = os.path.join(TEST_OUTPUT_DIR, "test_report.html")
    generator = HtmlGenerator()

    # הפעלת המחולל
    generator.generate(sample_report, output_path)

    # בדיקה שהקובץ אכן נוצר
    assert os.path.exists(output_path)

    # וידוא שהקובץ מכיל תגיות HTML בסיסיות
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "<html>" in content or "<html" in content
        assert "<table>" in content

    if os.path.exists(output_path):
        os.remove(output_path)


def test_excel_generator_creates_file(sample_report):
    output_path = os.path.join(TEST_OUTPUT_DIR, "test_report.xlsx")
    generator = ExcelGenerator()

    # הפעלת המחולל
    generator.generate(sample_report, output_path)

    # בדיקה שהקובץ אכן נוצר
    assert os.path.exists(output_path)

    assert os.path.getsize(output_path) > 0

    if os.path.exists(output_path):
        os.remove(output_path)