from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential

class ModelBuilder:
    @staticmethod
    def generate_model():
        model = Sequential()
        model.add(Dense(3, activation='relu'))
        model.add(Dense(2, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model
