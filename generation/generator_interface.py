from abc import ABC, abstractmethod
from domain.models.attendance_report import AttendanceReport

class IGenerator(ABC):
    @abstractmethod
    def generate(self, report: AttendanceReport, output_path: str) -> None:
        pass