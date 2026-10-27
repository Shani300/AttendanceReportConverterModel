from abc import ABC, abstractmethod

class IClassifier(ABC):
    @abstractmethod
    def classify(self, raw_text: str) -> str:
        pass