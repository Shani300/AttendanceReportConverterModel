# parsing/ocr_interface.py
from abc import ABC, abstractmethod

class IOcrProcessor(ABC):
    @abstractmethod
    def extract_text(self, file_path: str) -> str:
        pass