from abc import ABC, abstractmethod
from typing import List
from domain.models.text_element import TextElement


class ISpatialExtractor(ABC):
    """ממשק לחילוץ טקסט מבוסס קואורדינטות"""

    @abstractmethod
    def extract_elements(self, file_path: str) -> List[TextElement]:
        pass