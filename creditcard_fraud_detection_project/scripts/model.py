from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense, BatchNormalization

# function to create the shallow neural network model
def create_shallow_nn(optimizer, activation):
    shallow_nn = Sequential()
    shallow_nn.add(InputLayer((X_train_b.shape[1],)))
    shallow_nn.add(Dense(5, activation=activation))
    shallow_nn.add(BatchNormalization())
    shallow_nn.add(Dense(1, activation='sigmoid'))

    shallow_nn.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    return shallow_nn
