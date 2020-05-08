# import numpy as np
# import keras
# from keras import backend as K
# from keras.models import Sequential
# from keras.layers import Activation
# from keras.layers.core import Dense, Flatten
# from keras.optimizers import Adam
# from keras.metrics import categorical_crossentropy
# from keras.preprocessing.image import ImageDataGenerator
# from keras.layers.normalization import BatchNormalization
# from keras.layers.convolutional import *
# from matplotlib import pyplot as plt
# from sklearn.metrics import confusion_matrix
# import itertools
# import matplotlib.pyplot as plt
import os
import random
import shutil


def train_test_split(source, train_size):
    with os.scandir(source) as entries:
        train_size = train_size
        validation_counter = 0
        train_counter = 0
        for entry in entries:
            foldername = entry.name
            print(foldername)
            if not os.path.exists('trainingdata_Pictures'):
                os.makedirs('trainingdata_Pictures')
            if not os.path.exists('validationdata_Pictures'):
                os.makedirs('validationdata_Pictures')
            if foldername.endswith(".jpg") or foldername.endswith(".png"):
                if random.uniform(0, 1) <= train_size:
                    shutil.copy(source + '/' + foldername, os.getcwd() + '/trainingdata_Pictures')
                    train_counter += 1
                else:
                    shutil.copy(source + '/' + foldername, os.getcwd() + '/validationdata_Pictures')
                    validation_counter += 1
    print('Copied ' + str(train_counter))
    print('Copied ' + str(validation_counter))
