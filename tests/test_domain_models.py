import pytest
from domain.models.type_a_row import TypeARow
from domain.models.type_b_row import TypeBRow
from domain.models.type_a_metadata import TypeAMetadata
from domain.models.type_b_summary import TypeBSummary
from domain.models.attendance_report import AttendanceReport


def test_type_a_row_creation():
    row = TypeARow(
        date="01/01/2026",
        day_of_week="א",
        entry_time="08:00",
        exit_time="16:00",
        total_hours="08:00",
        work_location="ירושלים",
        hours_125="01:00"
    )
    assert row.date == "01/01/2026"
    assert row.work_location == "ירושלים"
    with pytest.raises(AttributeError):
        _ = row.comments

def test_type_b_row_creation():
    row = TypeBRow(
        date="02/01/2026",
        day_of_week="ב",
        entry_time="09:00",
        exit_time="17:00",
        total_hours="08:00",
        comments="איחור מוצדק"
    )
    assert row.entry_time == "09:00"
    assert row.comments == "איחור מוצדק"
    assert not hasattr(row, "work_location")


def test_attendance_report_composition():
    metadata = TypeAMetadata(employee_name="ראובן")
    summary = TypeBSummary(total_hours="150:00")

    report = AttendanceReport(
        report_type="MIXED_TEST",
        metadata=metadata,
        rows=[],
        summary=summary
    )

    assert report.metadata.employee_name == "ראובן"
    assert report.summary.total_hours == "150:00"