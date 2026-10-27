# domain/models/attendance_row.py
from dataclasses import dataclass

@dataclass
class AttendanceRow:
    raw_line_data: str