# Enhancing Network Security Through Phishing Website Detection Using Machine Learning (MLOps)

## Overview
This project aims to develop an end-to-end pipeline for detecting phishing websites by leveraging machine learning techniques. The pipeline includes multiple modular components to ensure efficient data handling, model training, and deployment.

---

## Architecture
The folders contain architecture details for each component.

### Pipeline Components
1. **ETL Pipelines**
   - Extracts data from various sources and loads it into a MongoDB database.
   - Ensures efficient data processing and storage as structured artifacts.

2. **Data Validation**
   - Ensures the quality and consistency of the ingested data.
   - Checks for missing values, invalid formats, or other anomalies.
   - Outputs validated data artifacts.

3. **Data Transformation**
   - Converts raw features into a suitable format for model training.
   - Applies techniques like scaling, encoding, or feature engineering.
   - Generates transformation artifacts.

4. **Model Training**
   - Trains a machine learning model using the transformed data.
   - Utilizes tools like MLflow for tracking experiments.
   - Stores model artifacts for evaluation.

5. **Model Evaluation**
   - Evaluates the trained model against validation metrics.
   - Determines if the model meets acceptance criteria for deployment.
   - Outputs evaluation artifacts.

6. **Model Deployment**
   - Deploys the accepted model using AWS services, including S3 buckets, ECR repositories, and EC2 instances.
   - Uses Docker to create containerized images for deployment.
   - Implements CI/CD pipelines using GitHub Actions for seamless and automated deployment.

---

## Workflow Description

### 1. ETL Pipelines
The **ETL Pipeline Component** extracts data from various sources, transforms it, and loads it into a MongoDB database. This process ensures the data is stored in a structured format for downstream tasks.

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
The **Model Trainer Component** uses the transformed data to train a machine learning model. It applies hyperparameter tuning and tracks experiments using tools like MLflow and DagsHub. Trained model artifacts are stored for evaluation.

### 5. Model Evaluation
The **Model Evaluation Component** assesses the model's performance using metrics such as accuracy, precision, recall, and F1-score. Models meeting predefined criteria are marked for deployment.

### 6. Model Deployment
The **Model Pusher Component** deploys the accepted model using:
- **AWS Services**: S3 Buckets for storing model artifacts, ECR Repository for managing Docker images, and EC2 Instances for hosting and running the deployed model.
- **CI/CD Pipelines**: GitHub Actions for automating and streamlining the deployment process.
- **Docker**: For containerizing the application to ensure consistency across environments.

---

## Key Features
- **Scalability**: Modular pipeline ensures scalability for large datasets.
- **Automation**: End-to-end workflow automation for seamless execution.
- **Cloud Integration**: Leverages AWS services (S3, ECR, EC2) for deployment.
- **CI/CD Integration**: GitHub Actions ensures smooth and automated deployment workflows.
- **Experiment Tracking**: Tracks experiments and models using MLflow and DagsHub.
- **Validation**: Robust mechanisms for ensuring data quality.

---

## Usage Instructions
1. Clone the repository.
2. Configure MongoDB, AWS credentials, Docker, and GitHub Actions.
3. Run the pipeline by executing the main script.
4. Use MLflow and DagsHub for tracking experiments and monitoring performance.

---

## Future Work
- Add support for additional data sources.
- Improve model interpretability.
- Implement real-time model monitoring.
- Expand deployment options to other cloud platforms (e.g., GCP, Azure).

---
