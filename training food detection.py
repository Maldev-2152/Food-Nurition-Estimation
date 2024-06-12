import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
import json

#https://www.youtube.com/watch?v=DJLM8ZDUHpI&list=PLvz5lCwTgdXByZ_z-LFo4vJbbFIMPhkkM&index=10

#Data Preprocessing
training_set = tf.keras.utils.image_dataset_from_directory(
    "C:\\Users\\Lenovo\\Desktop\\PBL\\PBL_2\\Food_Dataset\\train",
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(64, 64),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    data_format=None,
    verbose=True,
)

validation_set = tf.keras.utils.image_dataset_from_directory(
    "C:\\Users\\Lenovo\\Desktop\\PBL\\PBL_2\\Food_Dataset\\validation",
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(64, 64),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    data_format=None,
    verbose=True,
)


#Building Models
cnn = tf.keras.models.Sequential()

#building layers
cnn.add(tf.keras.layers.Input(shape=(64, 64, 3)))
cnn.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2, strides = 2))

cnn.add(tf.keras.layers.Conv2D(filters=64, kernel_size = 3, activation = 'relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2, strides = 2))

cnn.add(tf.keras.layers.Dropout(0.5)) #avoids overfitting

cnn.add(Flatten())
cnn.add(Dense(units = 128, activation = 'relu')) #can change units value
cnn.add(Dense(units = 36, activation = 'softmax')) #this is output layer & 36 units for 36 layers


#Compiling and Training
cnn.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

training_history = cnn.fit(x = training_set, validation_data = validation_set, epochs = 30)


#Saving Model
cnn.save('C:\\Users\\Lenovo\\Desktop\\PBL\\PBL_2\\trained_model.h5')

with open('C:\\Users\\Lenovo\\Desktop\\PBL\\PBL_2\\training_history','w') as f:
    json.dump(training_history.history,f)

print("Validation set Accuraccy: {} %".format(training_history.history['val_accuracy'][-1]*100))


#Loading Model, In another module
'''
cnn = tf.keras.models.load_model("Path of the saved model")

import cv2
img = cv2.imread("Image Path")
plt.imshow(img)
plt.title("Test Image")
plt.xticks([])
plt.yticks([])
plt.show()
'''
