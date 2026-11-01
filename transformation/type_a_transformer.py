from domain.models.attendance_report import AttendanceReport
from transformation.transformer_interface import ITransformer


class TypeATransformer(ITransformer):
    def transform(self, report: AttendanceReport) -> AttendanceReport:
        # לוגיקה עסקית לדוגמה: ניקוי תווי רווח עודפים מהתאריכים
        for row in report.rows:
            if hasattr(row, 'date'):
                row.date = row.date.strip()

            # כאן ניתן להוסיף חישובי שעות או אימות נתונים עתידיים

        return report