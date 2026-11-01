# Type A End-to-End Pipeline

מסמך זה מתאר את זרימת הנתונים של דוחות מסוג A.

## שלבי הזרימה (Data Flow):
1. **Extraction & Grouping**: המרת קובץ ה-PDF לטקסט מרחבי וקיבוצו לשורות (`spatial_lines`).
2. **Classification**: קביעת סוג המסמך על בסיס מילות מפתח (`ReportClassifier`).
3. **Parsing (`TypeAParser`)**: קריאת השורות, סינון שורות נוכחות על בסיס זיהוי תבנית תאריך, ויצירת מודל `AttendanceReport` המורכב משורות מסוג `TypeARow`.
4. **Transformation (`TypeATransformer`)**: החלת טיוב נתונים ולוגיקה עסקית על מודל הנתונים השלם (מבלי לשנות את סוג האובייקט).
5. **Generation (`CsvGenerator`)**: קריאת הנתונים מהמודל המעובד וכתיבתם לקובץ CSV מובנה ומוכן לשימוש (הפורמט הוא `utf-8-sig` כדי לאפשר פתיחה תקינה של תווים בעברית ב-Excel).