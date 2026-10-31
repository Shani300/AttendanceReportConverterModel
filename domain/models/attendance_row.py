# domain/models/attendance_row.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class AttendanceRow:
    """Base class for common row fields shared across all report types."""
    date: str
    day_of_week: str
    entry_time: str
    exit_time: str
    total_hours: str