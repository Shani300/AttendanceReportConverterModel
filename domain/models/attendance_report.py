# domain/models/attendance_report.py
from dataclasses import dataclass
from typing import List
from domain.models.attendance_row import AttendanceRow
from domain.models.report_summary import ReportSummary

@dataclass
class AttendanceReport:
    report_type: str
    rows: List[AttendanceRow]
    summary: ReportSummary