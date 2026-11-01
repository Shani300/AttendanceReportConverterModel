from abc import ABC, abstractmethod
from domain.models.attendance_report import AttendanceReport

class ITransformer(ABC):
    @abstractmethod
    def transform(self, report: AttendanceReport) -> AttendanceReport:
        pass