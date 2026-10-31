from dataclasses import dataclass
from typing import List, Union
from domain.models.type_a_row import TypeARow
from domain.models.type_b_row import TypeBRow
from domain.models.base_report_metadata import BaseReportMetadata
from domain.models.base_report_summary import BaseReportSummary

@dataclass
class AttendanceReport:
    """Root entity representing a fully parsed report."""
    report_type: str
    metadata: BaseReportMetadata
    rows: List[Union[TypeARow, TypeBRow]]
    summary: BaseReportSummary