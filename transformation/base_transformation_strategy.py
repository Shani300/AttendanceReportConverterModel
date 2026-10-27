from abc import ABC, abstractmethod
from domain.models.attendance_row import AttendanceRow

class BaseTransformationStrategy(ABC):
    @abstractmethod
    def transform_row(self, row: AttendanceRow, rules: dict, seed: int) -> AttendanceRow:
        pass