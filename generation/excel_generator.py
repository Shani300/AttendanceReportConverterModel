import os
import openpyxl
from openpyxl.styles import Font, Alignment
from domain.models.attendance_report import AttendanceReport
from config.constants import TypeAColumns
from generation.generator_interface import IGenerator


class ExcelGenerator(IGenerator):
    def generate(self, report: AttendanceReport, output_path: str) -> None:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "דוח נוכחות"

        # הגדרת כיווניות הגיליון לימין-לשמאל
        ws.sheet_view.rightToLeft = True

        # כתיבת כותרות עם עיצוב בסיסי
        for col_num, header_title in enumerate(TypeAColumns.HEADERS, start=1):
            cell = ws.cell(row=1, column=col_num, value=header_title)
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

        # כתיבת הנתונים
        for row_num, report_row in enumerate(report.rows, start=2):
            ws.cell(row=row_num, column=1, value=report_row.date)
            ws.cell(row=row_num, column=2, value=report_row.day_of_week)
            ws.cell(row=row_num, column=3, value=report_row.work_location)
            ws.cell(row=row_num, column=4, value=report_row.entry_time)
            ws.cell(row=row_num, column=5, value=report_row.exit_time)
            ws.cell(row=row_num, column=6, value=report_row.break_time)
            ws.cell(row=row_num, column=7, value=report_row.total_hours)
            ws.cell(row=row_num, column=8, value=report_row.hours_100)
            ws.cell(row=row_num, column=9, value=report_row.hours_125)
            ws.cell(row=row_num, column=10, value=report_row.hours_150)
            ws.cell(row=row_num, column=11, value=report_row.shabbat_hours)

        wb.save(output_path)