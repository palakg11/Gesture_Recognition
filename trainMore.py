#Importing keras libraries


import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model


with tf.device('/gpu:0'):
    #Initializing the CNN
    classifier = Sequential()
    classifier = load_model('gestures')

    #Compiling the CNN
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

    #Training and Testing
    from keras.preprocessing.image import ImageDataGenerator

    train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

    training_set = train_datagen.flow_from_directory(
            'Train More',
            target_size=(64, 64),
            batch_size=64,
            class_mode='categorical')


    classifier.fit_generator(
            training_set,
            steps_per_epoch=1822,
            epochs=1)

    #Saving the model
    classifier.save('gestures')


