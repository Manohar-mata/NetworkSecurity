import sys
import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constant.training_pipeline import TARGET_COLUMN
from networksecurity.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from networksecurity.Entity.artifact_entity import (
    DataTransformationArtifact,
    DataValidationArtifacts
)

from networksecurity.Entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object

class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifacts,
                 data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact: DataValidationArtifacts = data_validation_artifact
            self.data_transformation_config: DataTransformationConfig = data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        """
        Reads data from a CSV file and returns a DataFrame.
        """
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def get_data_transformer_object(self) -> Pipeline:
        """
        Initializes a KNNImputer object with parameters specified in training_pipeline.py
        and returns a Pipeline object.
        """
        logging.info("Entered get_data_transformer_object method of DataTransformation class")
        try:
            imputer: KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"Initialized KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            processor: Pipeline = Pipeline([("imputer", imputer)])
            return processor
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        """
        Performs data transformation and prepares artifacts for training and testing datasets.
        """
        logging.info("Entered initiate_data_transformation method of DataTransformation class")
        try:
            logging.info("Starting data transformation")

            # Reading train and test data
            train_df = self.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = self.read_data(self.data_validation_artifact.valid_test_file_path)

            # Preparing input and target features for training data
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN].replace(-1, 0)

            # Preparing input and target features for testing data
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN].replace(-1, 0)

            input_feature_train_df = input_feature_train_df.apply(pd.to_numeric, errors='coerce')
            input_feature_test_df = input_feature_test_df.apply(pd.to_numeric, errors='coerce')

            # Get the data transformer object
            preprocessor = self.get_data_transformer_object()

            # Fit and transform the training data
            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature = preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature = preprocessor_object.transform(input_feature_test_df)

            # Combine transformed input features and target features
            train_arr = np.c_[transformed_input_train_feature, np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_feature, np.array(target_feature_test_df)]

            # Save transformed data and preprocessor object
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor_object)

            # Preparing data transformation artifact
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            logging.info("Data transformation completed successfully")
            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)
