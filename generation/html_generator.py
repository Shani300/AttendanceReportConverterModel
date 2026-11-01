import os
from domain.models.attendance_report import AttendanceReport
from config.constants import TypeAColumns
from generation.generator_interface import IGenerator


class HtmlGenerator(IGenerator):
    def generate(self, report: AttendanceReport, output_path: str) -> None:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # בניית שלד ה-HTML ותמיכה בעברית (RTL)
        html_content = """
        <!DOCTYPE html>
        <html dir="rtl" lang="he">
        <head>
            <meta charset="UTF-8">
            <title>דוח נוכחות</title>
            <style>
                table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: right; }
                th { background-color: #f2f2f2; font-weight: bold; }
            </style>
        </head>
        <body>
            <h2>דוח נוכחות מסכם</h2>
            <table>
                <thead>
                    <tr>
        """

        # הוספת כותרות
        for header in TypeAColumns.HEADERS:
            html_content += f"<th>{header}</th>"

        html_content += """
                    </tr>
                </thead>
                <tbody>
        """

        # הוספת שורות הנתונים
        for row in report.rows:
            html_content += "<tr>"
            html_content += f"<td>{row.date}</td>"
            html_content += f"<td>{row.day_of_week}</td>"
            html_content += f"<td>{row.work_location}</td>"
            html_content += f"<td>{row.entry_time}</td>"
            html_content += f"<td>{row.exit_time}</td>"
            html_content += f"<td>{row.break_time}</td>"
            html_content += f"<td>{row.total_hours}</td>"
            html_content += f"<td>{row.hours_100}</td>"
            html_content += f"<td>{row.hours_125}</td>"
            html_content += f"<td>{row.hours_150}</td>"
            html_content += f"<td>{row.shabbat_hours}</td>"
            html_content += "</tr>"
            html_content += "</tr>"

        html_content += """
                </tbody>
            </table>
        </body>
        </html>
        """

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)