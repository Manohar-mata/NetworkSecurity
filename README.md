# Phishing Website Detection using Machine Learning

## Overview
This project aims to develop an end-to-end pipeline for detecting phishing websites by leveraging machine learning techniques. The pipeline includes multiple modular components to ensure efficient data handling, model training, and deployment.

---

## Architecture folders contian the architectures.

### Pipeline Components
1. **Data Ingestion**
   - Extracts data from a MongoDB database.
   - Converts raw data into a structured format.
   - Stores the processed data as artifacts.



2. **Data Validation**
   - Ensures the quality and consistency of the ingested data.
   - Checks for missing values, invalid formats, or other anomalies.
   - Outputs validated data artifacts.

   

3. **Data Transformation**
   - Converts raw features into a suitable format for model training.
   - Applies techniques like scaling, encoding, or feature engineering.
   - Generates transformation artifacts.

   _Add Architecture Diagram Here_

4. **Model Training**
   - Trains a machine learning model using the transformed data.
   - Stores model artifacts for evaluation.

   _Add Architecture Diagram Here_

5. **Model Evaluation**
   - Evaluates the trained model against validation metrics.
   - Determines if the model meets acceptance criteria for deployment.
   - Outputs evaluation artifacts.

   

6. **Model Pusher**
   - Pushes the accepted model to cloud services (AWS/Azure) for production use.
   - Deploys the model for real-time or batch inference.

 

---

## Workflow Description

### 1. Data Ingestion
The **Data Ingestion Component** connects to a MongoDB database to fetch raw data. This component processes and stores the data as artifacts to be consumed by downstream components.

### 2. Data Validation
The **Data Validation Component** verifies the ingested data by:
- Checking schema consistency.
- Identifying and handling missing or invalid entries.
- Generating validation artifacts to ensure data quality.

### 3. Data Transformation
The **Data Transformation Component** prepares the validated data for model training by:
- Encoding categorical variables.
- Normalizing numerical features.
- Outputting transformed data artifacts.

### 4. Model Training
The **Model Trainer Component** uses the transformed data to train a machine learning model. It applies hyperparameter tuning and stores the trained model artifacts.

### 5. Model Evaluation
The **Model Evaluation Component** assesses the model's performance using evaluation metrics like accuracy, precision, recall, and F1-score. Models meeting predefined criteria are marked for deployment.

### 6. Model Deployment
The **Model Pusher Component** deploys the accepted model to cloud environments (AWS/Azure) for production. It generates deployment artifacts to facilitate inference tasks.

---

## Key Features
- **Scalability**: Modular pipeline ensures scalability for large datasets.
- **Automation**: End-to-end workflow automation for seamless execution.
- **Cloud Integration**: Supports model deployment on AWS and Azure.
- **Validation**: Robust mechanisms for ensuring data quality.

---

## Usage Instructions
1. Clone the repository.
2. Configure MongoDB and cloud credentials.
3. Run the pipeline by executing the main script.

---

## Future Work
- Add support for additional data sources.
- Improve model interpretability.
- Implement real-time model monitoring.

---



