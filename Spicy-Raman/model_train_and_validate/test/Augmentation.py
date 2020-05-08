from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
from matplotlib import image
# %matplotlib agg
import os


def augmentation(name):
    # load the image
    img = load_img('Pre_Augmented_Raman_Pictures/' + name)
    # convert to numpy array
    data = img_to_array(img)
    # expand dimension to one sample
    samples = expand_dims(data, 0)
    # create image data augmentation generator
    datagen = ImageDataGenerator(zoom_range=[0.5, 1.0])
    # prepare iterator
    it = datagen.flow(samples, batch_size=1)
    # generate samples and plot
    for i in range(9):
        batch = it.next()
        # convert to unsigned integers for viewing
        current_image = batch[0].astype('uint8')
        # plot raw pixel data
        pyplot.imshow(current_image)
        # imwrite(fig, 'Post_Augmented_Raman_Pictures/1')
        image.imsave('Post_Augmented_Raman_Pictures/' + str(i) + name, current_image)


def full_augmentation(folder_name):
    with os.scandir(folder_name) as entries:
        for entry in entries:
            name = entry.name
            augmentation(name)
