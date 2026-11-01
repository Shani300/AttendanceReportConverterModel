from parsing.classifier_interface import IReportClassifier
from config.constants import ReportTypes, ReportKeywords


class ReportClassifier(IReportClassifier):
    """
    מממש את ממשק הסיווג תוך שימוש בלוגיקת צבירת נקודות (Scoring)
    המבוססת על מילות מפתח קבועות מראש.
    """

    def classify(self, raw_text: str) -> str:
        if not raw_text or not isinstance(raw_text, str):
            return ReportTypes.UNKNOWN

        # ספירת מופעים של מילות מפתח עבור סוג A
        type_a_score = sum(1 for keyword in ReportKeywords.TYPE_A_MARKERS if keyword in raw_text)

        # ספירת מופעים של מילות מפתח עבור סוג B
        type_b_score = sum(1 for keyword in ReportKeywords.TYPE_B_MARKERS if keyword in raw_text)

        # בחירת הסוג בעל הניקוד הגבוה ביותר, בתנאי שזוהתה לפחות מילה אחת
        if type_a_score > 0 and type_a_score > type_b_score:
            return ReportTypes.TYPE_A
        elif type_b_score > 0 and type_b_score > type_a_score:
            return ReportTypes.TYPE_B

        return ReportTypes.UNKNOWN