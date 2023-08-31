# Fraud Detection Pipeline

This repository contains a Python pipeline for building and training a neural network for fraud detection using the TensorFlow library. The pipeline includes data preprocessing, model creation, and hyperparameter tuning using GridSearchCV.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/lucidCrafts/credit_fraud_detection_project.git
    cd credit_fraud_detection_project
    ```

## Usage

Follow these steps to set up and use the fraud detection pipeline:

1. **Prepare Data:** Place your dataset (`your_dataset.csv`) in the `data` directory. Ensure that the dataset contains the necessary features, including the columns you specified for scaling.

2. **Configure Scripts:** Open the scripts in the `scripts` directory and configure them according to your dataset and pipeline requirements:
   
   - `preprocessing.py`: Customize data preprocessing steps, currently there are 1.load_data() 2.Robust_Scaler_M(), 3.dataframe_b(), 4.t_t_s_skl(). These are for loading, scaling, balancing, and splitting the dataset, you can adjust or skip using any of these as per you requirements, remember to make changes to the other ".py" files when you do. 
   - `model.py`: Adjust the neural network model architecture and hyperparameters.
   - `train.py`: Set up hyperparameter tuning settings and any additional training configurations.

3. **Install Dependencies:** Navigate to the `credit_fraud_detection_project` directory and install the required dependencies:
    ```bash
    cd credit_fraud_detection_project
    pip install -r requirements.txt
    ```

4. **Run the Training Script:** Execute the training script:
    ```bash
    python scripts/train.py
    ```
    This script will execute the preprocessing, model creation, training, and hyperparameter tuning steps.

5. **Check Outputs:** After the script completes, you should see console outputs indicating the progress of training and hyperparameter tuning. If everything is working correctly, you will also see the Best F1-score and the corresponding best hyperparameters.

6. **Verify Saved Model:** Check if the `best_model.h5` file is saved in the `saved_models` directory. This file should contain the best-trained model's weights and configuration.

7. **Interpret Results:** Depending on your use case, you can further evaluate the trained model on a validation or test dataset to assess its performance. You might need additional code to load the model and perform predictions using new data.

