from abc import ABC, abstractmethod

class IReportClassifier(ABC):
    """
    ממשק המגדיר את החוזה עבור מסווג דוחות.
    """
    @abstractmethod
    def classify(self, raw_text: str) -> str:
        """
        מקבל טקסט גולמי ומחזיר מזהה של סוג הדוח.
        """
        pass