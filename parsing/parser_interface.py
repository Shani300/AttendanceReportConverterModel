from abc import ABC, abstractmethod
from typing import List
from domain.models.text_element import TextElement
from domain.models.attendance_report import AttendanceReport

class IParser(ABC):
    @abstractmethod
    def parse(self, spatial_lines: List[List[TextElement]]) -> AttendanceReport:
        pass