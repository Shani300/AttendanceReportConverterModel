from dataclasses import dataclass
from typing import Optional
from domain.models.attendance_row import AttendanceRow

@dataclass
class TypeARow(AttendanceRow):
    """Fields specific to a row in a Type A report."""
    work_location: Optional[str] = None
    break_time: Optional[str] = None
    hours_100: Optional[str] = None
    hours_125: Optional[str] = None
    hours_150: Optional[str] = None
    shabbat_hours: Optional[str] = None