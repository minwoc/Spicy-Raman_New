import numpy as np 
import keras
from keras import backend as K
from keras.models import Sequential 
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator 
from keras.layers.normalization import BatchNormalization 
from keras.layers.convolutional import *
from matplotlib import pyplot as plt 
from sklearn.metrics import confusion_matrix 
import itertools 
import matplotlib.pyplot as plt 
import os
import random
import shutil

def test_train_test_split():
    numberofpicture = 0
    train_size = 0.6
    source = os.getcwd()
    source1 = os.path.dirname(source) + '/Post_Augmented_Raman_Pictures'
    with os.scandir(source1) as entries:
        for entry in entries: 
            foldername = entry.name
            if foldername.endswith(".jpg") or foldername.endswith(".png"): 
                numberofpicture += 1 
                assert train_size >= 0.5, 'train_size cannot be too low'
        print (numberofpicture) 
        assert numberofpicture is not 0, 'Please check if there are pictures in' + source
        assert train_size >= 0.5, 'train_size cannot be too low'
  
    
    
       