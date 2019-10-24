import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import AveragePooling2D
from keras.layers import Flatten
from keras.layers import Dense

with tf.device('/gpu:0'):
    #Initializing the CNN
    classifier = Sequential()

    #Convulution
    classifier.add(Convolution2D(128, 3, 3, input_shape = (64, 64,3), activation = 'relu'))

    #Pooling
    classifier.add(AveragePooling2D(pool_size = (2,2)))
    classifier.add(Convolution2D(256, 3, 3, activation = 'relu'))
    classifier.add(AveragePooling2D(pool_size = (2,2)))

   
    #LSTM
    model.add(LSTM(300))

    #Flattening
    classifier.add(Flatten())

    #Full Connection
    classifier.add(Dense(output_dim = 128, activation = 'relu'))
    classifier.add(Dense(output_dim = 128, activation = 'relu'))
    classifier.add(Dense(output_dim = 3, activation = 'softmax'))

    #Compiling the CNN_LSTM
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

    #Training and Testing
    from keras.preprocessing.image import ImageDataGenerator

    train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

    training_set = train_datagen.flow_from_directory(
            'TrainingSet',
            target_size=(64, 64),
            batch_size=64,
            class_mode='categorical')


    classifier.fit_generator(
            training_set,
            steps_per_epoch=1040,
            epochs=2)

    #Saving the model
    classifier.save('gestures')