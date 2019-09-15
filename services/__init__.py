import services.Reader as reader
import services.DataService as dataService
import keras

import services.DataManipulator as dm
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.core import Dense, Flatten
from keras.layers.convolutional import *
from keras.models import Sequential
from keras.optimizers import Adam

basic_model_file = "basic_model.h5"
vgg_model_file = "vgg_model.h5"


train_batches = ImageDataGenerator().flow_from_directory(dataService.data_training, target_size=(224, 224),
                                                         classes=["_20", "21_35", "36_60", "60_"], batch_size=20)

validation_batches = ImageDataGenerator().flow_from_directory(dataService.data_validation, target_size=(224, 224),
                                                              classes=["_20", "21_35", "36_60", "60_"],
                                                              batch_size=8)

test_batches = ImageDataGenerator().flow_from_directory(dataService.data_test, target_size=(224, 224),
                                                        classes=["_20", "21_35", "36_60", "60_"], batch_size=20)

def main():
    print(">>Program started<<")
    #dm.split_data_num()

    # basic ====
    #train_basic_model()
    #predict_ages(basic_model_file)
    # ====

    # vgg 16====
    #train_with_VGG16()
    predict_ages(vgg_model_file)
    # ====




def predict_ages(model_file_name):
    model = reader.read_model(model_file_name)

    test_imgs, test_labels = next(test_batches)

    predictions = model.predict_generator(test_batches, steps=10, verbose=0) #steps sum all up / batch size //262

    for e in predictions:
        print(e)


def train_basic_model():
    print(">>Creating basic age recognition model<<")
    imgs, labels = next(train_batches)

    model = Sequential([
        Conv2D(52, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        Flatten(),
        Dense(4, activation="softmax")
    ])
    model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit_generator(train_batches, steps_per_epoch=400, validation_data=validation_batches,
                        validation_steps=150, epochs=5, verbose=2)

    fit_and_save_the_model(model, basic_model_file)

def train_with_VGG16(): #16
    vgg_model = keras.applications.vgg16.VGG16()
    model = Sequential()

    for layer in vgg_model.layers:
        model.add(layer)

    model.layers.pop()

    for layer in model.layers:
        layer.trainable = False

    model.add(Dense(4, activation="softmax"))

    fit_and_save_the_model(model, vgg_model_file)

def fit_and_save_the_model(model, file_name):
    model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit_generator(train_batches, steps_per_epoch=400, validation_data=validation_batches,
                        validation_steps=150, epochs=5, verbose=2)

    reader.save_model(model, file_name)

if __name__ == "__main__":
    main()
