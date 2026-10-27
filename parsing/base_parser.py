from abc import ABC, abstractmethod
from typing import List
from domain.models.attendance_report import AttendanceReport
from domain.models.attendance_row import AttendanceRow
from domain.models.report_summary import ReportSummary


def clean(raw_text: str) -> str:
    return raw_text.strip()


class BaseParser(ABC):
    def __init__(self, report_type: str):
        self.report_type = report_type

    def parse(self, raw_text: str) -> AttendanceReport:
        # shared flow - identical for every report type
        lines = clean(raw_text).splitlines()
        summary = self._parse_summary(lines)
        rows = [
            self._parse_row(l) for l in lines
            if not self._is_header_line(l)
        ]
        return AttendanceReport(self.report_type, rows, summary)

    # each subclass fills in only what differs
    @abstractmethod
    def _parse_row(self, line: str) -> AttendanceRow | None: ...

    @abstractmethod
    def _parse_summary(self, lines: list[str]) -> ReportSummary: ...

    @abstractmethod
    def _is_header_line(self, line: str) -> bool: ...