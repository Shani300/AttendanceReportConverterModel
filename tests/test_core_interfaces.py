import pytest
from infrastructure.file_reader_interface import IFileReader
from parsing.classifier_interface import IReportClassifier
from parsing.base_parser import BaseParser
from transformation.base_transformation_strategy import BaseTransformationStrategy
from generation.generator_interface import IGenerator
from config.error_messages import ErrorMessages


def test_cannot_instantiate_interfaces():
    with pytest.raises(TypeError, match=ErrorMessages.INSTANTIATION_ERROR):
        IFileReader()

    with pytest.raises(TypeError, match=ErrorMessages.INSTANTIATION_ERROR):
        IReportClassifier()

    with pytest.raises(TypeError, match=ErrorMessages.INSTANTIATION_ERROR):
        BaseTransformationStrategy()

    with pytest.raises(TypeError, match=ErrorMessages.INSTANTIATION_ERROR):
        IGenerator()


def test_base_parser_enforces_abstract_methods():
    class IncompleteParser(BaseParser):
        pass

    with pytest.raises(TypeError, match=ErrorMessages.INSTANTIATION_ERROR):
        IncompleteParser(report_type="TEST")