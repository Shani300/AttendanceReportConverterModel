import pytest
from parsing.classifier import ReportClassifier
from config.constants import ReportTypes

@pytest.fixture
def classifier():
    return ReportClassifier()

def test_classify_type_a_correctly(classifier):
    raw_text = "דוח 100% 125% 150% 150"
    assert classifier.classify(raw_text) == ReportTypes.TYPE_A

def test_classify_type_b_correctly(classifier):
    raw_text = "כרטיס עובד לחודש אוקטובר פרויקט גונן שם הערות הערות הערות"
    assert classifier.classify(raw_text) == ReportTypes.TYPE_B

def test_classify_unknown_format(classifier):
    raw_text = "דוח סתמי ללא מילות מפתח מוכרות כלל"
    assert classifier.classify(raw_text) == ReportTypes.UNKNOWN

def test_classify_empty_or_invalid_input(classifier):
    assert classifier.classify("") == ReportTypes.UNKNOWN
    assert classifier.classify(None) == ReportTypes.UNKNOWN

def test_classify_mixed_content_favors_highest_score(classifier):
    # טקסט המכיל מילה אחת של A ושתיים של B - אמור להיות מזוהה כ-B
    raw_text = "גליליון מציג כרטיס עובד לחודש עבור גונן"
    assert classifier.classify(raw_text) == ReportTypes.TYPE_B