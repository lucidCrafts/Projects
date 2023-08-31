from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
import pandas as pd

columns_to_scale = list(input("Enter the columns to scale (comma-separated): ").split(','))

def Robust_Scaler_M(df,coloumns_to_scale):
    new_df = df.copy()
    rc = RobustScaler()
    for c in coloumns_to_scale:
      new_df[c]= rc.fit_transform(new_df[c].to_numpy().reshape(-1,1))

    return new_df

#coloumns_to_scale =['Time','Amount']
#Call this fucntion Robust_Scaler_M(df,coloumns_to_scale)




def dataframe_b(unbalanced_df):
    not_frauds = new_df.query('Class == 0')
    frauds = new_df.query('Class == 1')
    not_frauds['Class'].value_counts(), frauds['Class'].value_counts()
    balanced_dataframe= unbalanced_df.sample(len(frauds), random_state=33)
    balanced_dataframe = unbalanced_df.sample(frac=1, random_state=1)
    return balanced_dataframe

# Call this fucntion by balanced_dataframe = dataframe_b(new_df)




def t_t_s_skl(preprocessed_df, train_test_size, val_size):
    X = preprocessed_df.drop(columns=['Class'])
    y = preprocessed_df['Class']

    X_train_1, X_temp_1, y_train_1, y_temp_1 = train_test_split(X, y, test_size=train_test_size, random_state=42)
    X_test_1, X_val_1, y_test_1, y_val_1 = train_test_split(X_temp_1, y_temp_1, test_size=val_size, random_state=42)

    print("Shapes:")
    print("X_train:", X_train_1.shape)
    print("X_temp:", X_temp_1.shape)
    print("y_train:", y_train_1.shape)
    print("y_temp:", y_temp_1.shape)
    print("X_test:", X_test_1.shape)
    print("X_val:", X_val_1.shape)
    print("y_test:", y_test_1.shape)
    print("y_val:", y_val_1.shape)

    return X_train_1, X_test_1, X_val_1, y_train_1, y_test_1, y_val_1

# Call this function
#X_train_b, X_test_b, X_val_b, y_train_b, y_test_b, y_val_b = t_t_s_skl(new_df, 0.2, 0.5)



def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path)
    return data


if __name__ == "__main__":
    file_path = "data/YOUR_DATASET_NAME.csv"
    dataset = load_data(file_path)
    print("Loaded dataset:", dataset.shape)


