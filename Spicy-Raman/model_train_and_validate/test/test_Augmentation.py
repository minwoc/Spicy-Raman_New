from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
from matplotlib import image
# %matplotlib agg
import os

def test_augmentation():
    name = ''
    assert isinstance(name, str), 'The input has to be a string'

def test_full_augmentation():
    folder_name = ''
    assert isinstance(folder_name, str), 'The input has to be a string'