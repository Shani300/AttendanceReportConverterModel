from typing import List
from domain.models.text_element import TextElement


class SpatialGrouper:
    def __init__(self, y_tolerance: float = 15.0):
        # הגדלנו את טווח הסטייה ל-15 פיקסלים כדי לספוג הבדלי גובה וסריקה
        self.y_tolerance = y_tolerance

    def _get_center_y(self, element: TextElement) -> float:
        """פונקציית עזר לחישוב המרכז האנכי של אלמנט הטקסט"""
        return (element.top + element.bottom) / 2.0

    def group_into_lines(self, elements: List[TextElement]) -> List[List[TextElement]]:
        if not elements:
            return []

        # 1. מיון כללי מלמעלה למטה על בסיס מרכז המילה (ולא הקצה העליון בלבד)
        elements.sort(key=self._get_center_y)

        lines: List[List[TextElement]] = []
        current_line: List[TextElement] = [elements[0]]

        # 2. קיבוץ לשורות על בסיס קירבה בציר ה-Y של מרכזי המילים
        for el in elements[1:]:
            # אנו בודקים האם המרכז של המילה הנוכחית קרוב למרכז של המילה הקודמת בשורה
            if abs(self._get_center_y(el) - self._get_center_y(current_line[-1])) <= self.y_tolerance:
                current_line.append(el)
            else:
                lines.append(current_line)
                current_line = [el]

        if current_line:
            lines.append(current_line)

        # 3. מיון כל שורה בנפרד מימין לשמאל (לקריאה תקינה של עברית ומספרים)
        for line in lines:
            line.sort(key=lambda e: e.x1, reverse=True)

        return lines