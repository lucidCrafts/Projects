from sklearn.metrics import f1_score, make_scorer
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from tensorflow.keras.callbacks import ModelCheckpoint
import pandas as pd
from scripts.preprocessing import split_dataset, balanced_dataframe
from scripts.model import create_shallow_nn


# Create a KerasClassifier based on the function
shallow_nn_model = KerasClassifier(build_fn=create_shallow_nn, epochs=10, batch_size=16, verbose=2)

# Defining the parameter grid to search through
param_grid = {
    'optimizer': ['adam', 'sgd'],
    'activation': ['relu', 'tanh']
}

# Creating a scorer for F1-score
f1_scorer = make_scorer(f1_score, average='binary')
checkpoint =ModelCheckpoint('best_model.h5', save_best_only=True)
# Create the GridSearchCV object
grid = GridSearchCV(estimator=shallow_nn_model, param_grid=param_grid, scoring=f1_scorer, cv=3)
grid_result = grid.fit(X_train_b, y_train_b, validation_data=(X_val_b, y_val_b), callbacks=[checkpoint])

# Print the best results
print("Best F1-score: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

