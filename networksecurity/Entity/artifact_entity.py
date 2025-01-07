from dataclasses import dataclass

@dataclass
class DataIngestoinArtifacts:
    trained_file_path:str
    tested_file_path: str

@dataclass
class DataValidationArtifacts:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str