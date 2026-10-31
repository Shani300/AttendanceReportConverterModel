from dataclasses import dataclass

@dataclass
class TextElement:
    """ייצוג מרחבי של מילה בודדת שחולצה מהמסמך"""
    text: str
    x0: float  # קצה שמאלי
    top: float # קצה עליון
    x1: float  # קצה ימני
    bottom: float # קצה תחתון