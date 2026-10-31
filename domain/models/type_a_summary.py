from dataclasses import dataclass
from typing import Optional
from domain.models.base_report_summary import BaseReportSummary

@dataclass
class TypeASummary(BaseReportSummary):
    """Summary fields specific to Type A reports."""
    total_monthly_work_days: Optional[str] = None
    total_monthly_hours: Optional[str] = None
    hourly_rate: Optional[str] = None
    total_to_pay: Optional[str] = None
    comments: Optional[str] = None