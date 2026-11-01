from parsing.tesseract_spatial_extractor import TesseractSpatialExtractor
from parsing.spatial_grouper import SpatialGrouper
from parsing.classifier import ReportClassifier
from parsing.type_a_parser import TypeAParser
from transformation.type_a_transformer import TypeATransformer
from generation.csv_generator import CsvGenerator
from config.constants import ReportTypes, PipelineConfig


def process_pipeline():
    file_path = "docs/type_a_1.pdf"

    # 1. חילוץ וקיבוץ
    extractor = TesseractSpatialExtractor()
    elements = extractor.extract_elements(file_path)

    grouper = SpatialGrouper()
    spatial_lines = grouper.group_into_lines(elements)

    # 2. סיווג
    raw_text = "\n".join([" ".join([el.text for el in line]) for line in spatial_lines])
    classifier = ReportClassifier()
    report_type = classifier.classify(raw_text)

    if report_type != ReportTypes.TYPE_A:
        print(f"Skipping pipeline. Document is of type: {report_type}")
        return

    # 3. Parsing
    parser = TypeAParser()
    report = parser.parse(spatial_lines)
    print(report)
    # 4. Transformation
    transformer = TypeATransformer()
    transformed_report = transformer.transform(report)
    print(transformed_report)
    # 5. Generation
    generator = CsvGenerator()
    generator.generate(transformed_report, PipelineConfig.OUTPUT_FILE_PATH)

    print(f"Pipeline completed successfully. Output saved to {PipelineConfig.OUTPUT_FILE_PATH}")


if __name__ == "__main__":
    process_pipeline()