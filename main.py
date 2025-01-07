from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.Entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.Entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
import sys

if __name__=="__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info(f"initiate the data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info(f"Data Ingestion is completed")
        print(data_ingestion_artifact)
        data_validation_config=DataValidationConfig(training_pipeline_config)
        data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info(f"initiate data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info(f"data validation is completed")
        print(data_validation_artifact)
        

    except Exception as e:
        raise NetworkSecurityException(e, sys)