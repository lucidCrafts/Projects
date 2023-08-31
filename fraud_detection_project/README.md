# Fraud Detection Pipeline

This repository contains a Python pipeline for building and training a neural network for fraud detection using the `tensorflow` library. The pipeline includes data preprocessing, model creation, and hyperparameter tuning using `GridSearchCV`.

## Installation

1. Clone this repository:
bash
git clone https://github.com/lucidCrafts/credit_fraud_detection_project.git

cd credit_fraud_detection_project


##Usage

Follow these steps to set up and use the fraud detection pipeline:

## Prepare Data:

Place your dataset (your_dataset.csv) in the data directory. Ensure that the dataset contains the necessary features, including the columns you specified for scaling.

Configure Scripts:
Open the scripts in the scripts directory and configure them according to your dataset and pipeline requirements:

preprocessing.py:
Customize data preprocessing steps, such as handling missing values, encoding categorical variables, and splitting data.
model.py: Adjust the neural network model architecture and hyperparameters.
train.py: Set up hyperparameter tuning settings and any additional training configurations.

Install Dependencies:
bash
"cd credit_fraud_detection_project"
Run the training script:

bash
"python scripts/train.py"
This script will execute the preprocessing, model creation, training, and hyperparameter tuning steps.

Check Outputs:
After the script completes, you should see console outputs indicating the progress of the training and hyperparameter tuning. If everything is working correctly, you will  also see the Best F1-score and the corresponding best hyperparameters.

Verify Saved Model:
Check if the best_model.h5 file is saved in the saved_models directory. This file should contain the best-trained models  weights and configuration.

Interpret Results:
Depending on your use case, you can further evaluate the trained model on a validation or test dataset to assess its performance. You might need additional code to load the model and perform predictions using new data.
