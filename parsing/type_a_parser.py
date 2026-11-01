import re
from typing import List
from parsing.parser_interface import IParser
from domain.models.text_element import TextElement
from domain.models.attendance_report import AttendanceReport
from domain.models.type_a_row import TypeARow
from config.constants import PipelineConfig


class TypeAParser(IParser):
    def parse(self, spatial_lines: List[List[TextElement]]) -> AttendanceReport:
        rows = []

        for line in spatial_lines:
            line_text = " ".join([el.text for el in line])

            # זיהוי שורת נתונים באמצעות הימצאות תאריך
            if re.search(PipelineConfig.DATE_PATTERN, line_text):
                # לצורך ה-Happy Path בשלב זה, אנו מסתמכים על סדר הופעת המילים בשורה
                # הערה: בייצור נרחיב זאת לשימוש מדויק בקואורדינטות של כל TextElement
                elements_text = [el.text for el in line]

                if len(elements_text) >= 7:
                    row = TypeARow(
                        date=elements_text[-1],  # הימני ביותר
                        day_of_week=elements_text[-2],
                        work_location=elements_text[-3],
                        entry_time=elements_text[-4],
                        exit_time=elements_text[-5],
                        break_time=elements_text[-6],
                        total_hours=elements_text[-7]
                    )
                    rows.append(row)

        return AttendanceReport(report_type="TYPE_A", rows=rows)