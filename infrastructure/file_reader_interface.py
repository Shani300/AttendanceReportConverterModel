# infrastructure/file_reader_interface.py
from abc import ABC, abstractmethod

class IFileReader(ABC):
    @abstractmethod
    def read(self, file_path: str) -> str:
        pass