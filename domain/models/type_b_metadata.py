from dataclasses import dataclass
from typing import Optional
from domain.models.base_report_metadata import BaseReportMetadata

@dataclass
class TypeBMetadata(BaseReportMetadata):
    """Metadata specific to Type B reports."""
    company_name: Optional[str] = None