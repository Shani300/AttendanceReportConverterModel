from domain.models.attendance_report import AttendanceReport
from generation.generator_interface import IGenerator
import csv
import os
from config.constants import TypeAColumns, PipelineConfig

class CsvGenerator(IGenerator):
    def generate(self, report: AttendanceReport, output_path: str) -> None:
        # יצירת התיקייה במידה ואינה קיימת
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, mode='w', newline='', encoding='utf-8-sig') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(TypeAColumns.HEADERS)

            for row in report.rows:
                writer.writerow([
                    row.date,
                    row.day_of_week,
                    row.work_location,
                    row.entry_time,
                    row.exit_time,
                    row.break_time,
                    row.total_hours,
                    row.hours_100,
                    row.hours_125,
                    row.hours_150,
                    row.shabbat_hours
                ])