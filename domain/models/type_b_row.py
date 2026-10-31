from dataclasses import dataclass
from typing import Optional
from domain.models.attendance_row import AttendanceRow

@dataclass
class TypeBRow(AttendanceRow):
    """Fields specific to a row in a Type B report."""
    comments: Optional[str] = None