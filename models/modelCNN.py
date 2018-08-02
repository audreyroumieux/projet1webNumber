# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:45:30 2018
@author: audrey roumieux
Projet: web
Description : Model Convolutional
"""
import numpy as np
import keras
from keras.utils import to_categorical
from keras.datasets import mnist
from keras.layers import Dense
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dropout

# import du jeu de donnée
(x_mnist_train, y_mnist_train), (x_mnist_test, y_mnist_test) = mnist.load_data()

# One hot encoding sur les y
y_mnist_train = to_categorical(y_mnist_train, 10) # il existe 10 chiffres different
y_mnist_test = to_categorical(y_mnist_test, 10)


#traitement dimention des données
x_mnist_train = x_mnist_train.astype('float32') # On convertie les données en nombre entre 0 et 1
x_mnist_train = x_mnist_train / 255
x_mnist_test = x_mnist_test.astype('float32') 
x_mnist_test = x_mnist_test / 255

# change la forme de la matrice pour donnéer une pronfondeur de 1
x_mnist_train = x_mnist_train.reshape(x_mnist_train.shape[0], 28, 28, 1)
x_mnist_test = x_mnist_test.reshape(x_mnist_test.shape[0], 28, 28, 1)



model = keras.models.Sequential()
# Premier couche
model.add(Conv2D(64, # il y a 64 images en sorti
                     kernel_size=(3, 3), # la taille du filtre, on selectionne des matrices de 3x3
                     activation='relu', input_shape=(28, 28, 1)))

model.add(MaxPooling2D()) # Reduit la taille de l'image

model.add(Flatten()) # Reformatte les données en un vercteur
# model.add(Dropout(0.5)) # Methode de regularisation, empeche l'over fiting en changent les valeur
model.add(Dense(512, activation='relu'))
model.add(Dense(10, activation='softmax'))
# print(model.summary())

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(x_mnist_train, y_mnist_train,
          epochs=6, # nombre de fois ou l'on traitre l'ensemble des données
          validation_data=(x_mnist_test, y_mnist_test))


model.save('cnn_model.h5') # creates a HDF5 file 'cnn_model.h5'