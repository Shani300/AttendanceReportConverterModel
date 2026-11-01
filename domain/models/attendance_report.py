from dataclasses import dataclass, field
from typing import List, Optional, Any
from domain.models.attendance_row import AttendanceRow

@dataclass
class AttendanceReport:
    report_type: str
    rows: List[AttendanceRow] = field(default_factory=list)
    metadata: Optional[Any] = None
    summary: Optional[Any] = None