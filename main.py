# main.py
from matplotlib import pyplot
from data_generator import Dres
from data_preprocessing import DataPreprocessor
from model_builder import ModelBuilder

def main():
    model = ModelBuilder.generate_model()
    attr, labels = Dres.generate_list(5000)
    data_preprocessor = DataPreprocessor()
    attr, labels = data_preprocessor.normalize_data(attr, labels)
    training_atr, training_lab, test_atr, test_lab = data_preprocessor.split_list(attr, labels)
    history = model.fit(training_atr, training_lab, validation_data=(test_atr, test_lab), batch_size=50, epochs=300)
    model.summary()
    return history

def plots(history):
    pyplot.plot(history.history['accuracy'])
    pyplot.plot(history.history['val_accuracy'])
    pyplot.plot(history.history["loss"])
    pyplot.plot(history.history["val_loss"])
    pyplot.legend(['train_acc', 'test_acc', 'train_loss', 'val_loss'])

if __name__ == "__main__":
    history = main()
    plots(history)
    pyplot.show()
