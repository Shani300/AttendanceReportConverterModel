import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from bidi.algorithm import get_display  # דורש: pip install python-bidi
from domain.models.attendance_report import AttendanceReport
from config.constants import TypeAColumns
from generation.generator_interface import IGenerator


class PdfGenerator(IGenerator):
    def generate(self, report: AttendanceReport, output_path: str) -> None:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # טעינת פונט שתומך בעברית (יש לוודא שהקובץ קיים בנתיב המערכת או בתיקיית הפרויקט)
        # pdfmetrics.registerFont(TTFont('HebrewFont', 'Arial.ttf'))

        doc = SimpleDocTemplate(output_path, pagesize=A4)
        elements = []

        # פונקציית עזר להיפוך הטקסט עבור תצוגה תקינה בעברית ב-PDF
        def fix_hebrew(text):
            return get_display(str(text)) if text else ""

        # הכנת הנתונים לטבלה (כותרות תחילה)
        # יש להפוך את סדר העמודות כדי שיוצגו נכון מימין לשמאל ב-ReportLab
        headers = [fix_hebrew(h) for h in reversed(TypeAColumns.HEADERS)]
        data = [headers]

        for row in report.rows:
            # הכנסת הנתונים בסדר הפוך, בהתאמה לכותרות
            row_data = [
                fix_hebrew(row.total_hours),
                fix_hebrew(row.break_time),
                fix_hebrew(row.exit),
                fix_hebrew(row.entry),
                fix_hebrew(row.work_location),
                fix_hebrew(row.day),
                fix_hebrew(row.date)
            ]
            data.append(row_data)

        # יצירת ועיצוב הטבלה
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            # ('FONTNAME', (0, 0), (-1, -1), 'HebrewFont'), # הפעלה במידה ונטען פונט
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)
        doc.build(elements)