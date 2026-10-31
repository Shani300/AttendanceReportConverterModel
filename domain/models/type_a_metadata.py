# domain/models/type_a_metadata.py
from dataclasses import dataclass
from typing import Optional
from domain.models.base_report_metadata import BaseReportMetadata

@dataclass
class TypeAMetadata(BaseReportMetadata):
    """Metadata specific to Type A reports."""
    employee_name: Optional[str] = None
    employee_card_month: Optional[str] = None