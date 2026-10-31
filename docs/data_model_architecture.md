# docs/data_model_architecture.md
# Data Model Architecture

## Objective
To strictly map the varied data structures of incoming PDF timesheets into strongly typed Python dataclasses, supporting rigorous parsing and transformation steps.

## Design Pattern
The domain utilizes **Inheritance** via `dataclasses`.
- **Base Classes** (`AttendanceRow`, `BaseReportMetadata`, `BaseReportSummary`) hold properties that are universally true across all incoming timesheets.
- **Concrete Subclasses** (e.g., `TypeARow`, `TypeBSummary`) implement attributes exclusively required by that specific document type.

This approach guarantees that when a Type B document is processed, memory is not allocated for Type A fields (like `shabbat_hours`), adhering to the Interface Segregation and Liskov Substitution principles of SOLID. All fields utilize standard Python strings at this boundary layer; type coercion (e.g., casting hours to floats or datetimes) is strictly the responsibility of the subsequent Transformation layer.