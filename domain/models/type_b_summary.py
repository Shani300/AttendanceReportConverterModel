from dataclasses import dataclass
from typing import Optional
from domain.models.base_report_summary import BaseReportSummary

@dataclass
class TypeBSummary(BaseReportSummary):
    """Summary fields specific to Type B reports."""
    total_days: Optional[str] = None
    total_hours: Optional[str] = None
    hours_100: Optional[str] = None
    hours_125: Optional[str] = None
    hours_150: Optional[str] = None
    bonus: Optional[str] = None
    travel: Optional[str] = None