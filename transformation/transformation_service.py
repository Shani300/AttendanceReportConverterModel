from typing import Dict
from domain.models.attendance_report import AttendanceReport
from transformation.base_transformation_strategy import BaseTransformationStrategy

class TransformationService:
    def __init__(self, strategies: Dict[str, BaseTransformationStrategy]):
        self._strategies = strategies

    def process(self, report: AttendanceReport, rules: dict, seed: int) -> AttendanceReport:
        strategy = self._strategies.get(report.report_type)
        if not strategy:
            raise ValueError(f"No strategy found for {report.report_type}")

        new_rows = [strategy.transform_row(row, rules, seed) for row in report.rows]
        return AttendanceReport(report.report_type, new_rows, report.summary)