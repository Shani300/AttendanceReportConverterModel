from abc import ABC, abstractmethod
import csv
import os
from domain.models.attendance_report import AttendanceReport
from config.constants import TypeAColumns, PipelineConfig

class IGenerator(ABC):
    @abstractmethod
    def generate(self, report: AttendanceReport, output_path: str) -> None:
        pass