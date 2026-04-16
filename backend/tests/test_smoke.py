"""
Smoke tests — verify all project modules can be imported
and that core classes are instantiable without a trained model.
"""
import sys
import os

# Ensure the backend package is on the path when running from the repo root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_import_text_processor():
    from src.text_processor import TextPreprocessor  # noqa: F401
    tp = TextPreprocessor()
    assert hasattr(tp, "preprocess_pipeline")


def test_import_feature_extractor():
    from src.feature_extractor import FeatureExtractor  # noqa: F401
    fe = FeatureExtractor()
    assert hasattr(fe, "extract_tfidf_features")


def test_import_database():
    from src.database import DatabaseManager  # noqa: F401


def test_import_alert_system():
    from src.alert_system import AlertSystem  # noqa: F401
    a = AlertSystem()
    assert hasattr(a, "should_alert")


def test_import_data_collector():
    from src.data_collector import WebDataCollector  # noqa: F401


def test_import_classifier():
    from src.classifier import ContentClassifier  # noqa: F401
    # ContentClassifier gracefully handles missing model files
    c = ContentClassifier()
    assert hasattr(c, "predict")


def test_import_model_trainer():
    from src.model_trainer import TerrorismDetectionModel  # noqa: F401


def test_import_train_pipeline():
    from src.train_pipeline import TrainingPipeline  # noqa: F401


def test_import_monitor():
    from src.monitor import AutomatedMonitor  # noqa: F401
