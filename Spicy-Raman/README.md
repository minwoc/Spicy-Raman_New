# Spicy-Raman <img src="https://github.com/nsuzuki97/Spicy-Raman/blob/master/logo.png" width="25%">

[![Build Status](https://travis-ci.org/nsuzuki97/Spicy-Raman.svg?branch=master)](https://travis-ci.org/nsuzuki97/Spicy-Raman)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<img src="https://www.cei.washington.edu/wordpress/wp-content/uploads/2016/01/CEI_logo_tag_color.1.png" width="555" height="160">  ![image](https://i.dailymail.co.uk/1/2018/09/27/17/4591062-0-image-m-35_1538065690576.jpg)

### Background
-----------
Microplastic ingestion has been considered to be a serious detriment to marine organisms, from oysters to orca whales. The majority of these samples have been identified to be one of four categories: polyethylene, nylon, polyamides, and fluorescents. Although comprising only about 20 - 25% of the total samples, this still represents about 10+ hours of analysis per study. By categorizing and filtering out these major classes of spectra, researchers will be able to focus on identifying novel groups of microparticles.

### Project Scope, Quick Intro
-----------
We employed TensorFlow (and the keras API because we are beginners) to create a model to classify the Raman spectrum from orca whale samples. The goal of our project is to machine learn the pattern of Raman spectra by polymer categories(e.g. polyamide, polyethylene), and let it expect the type a designated material falls into.
In this specific model, 3 levels of neurons were used in order to optimize adequate complexity with ease of model creation and speed.

We acquired Raman spectra from Luscombe Lab. We acquired them as .txt files so that we can finally change them into image files that can be used with Tensorflow(or Keras?). We first plotted those text data and converted them into image files(.png).

However since the amount of data we could get was less than we expected, we talked to Jimin Qian with this issue, and we decided to do data augmentation.
We first converted images into a numpy array(img_to_array), expanded dimension(expand_dims), and created image data augmentation generator(ImageDataGenerator(zoom_range=[0.5,1.0])). We used os.scandir() function to iterate over data not yet augmented and got augmented data.

We then created image databse in order to load these image data into codes.

The augmented data was then separated 80/20 into training and validation data.
They were stored in either "trainingdata_Pictures" directory or "validationdata_Pictures".

Each train and validation set were then split into 5 categories: flourescent, nylon, polyamide, polyethylene, and unknown.

### Sturcture

```
|-Licence

|-README

|-model_train_and_validate/

  |-Post_Augmented_Raman_Pictures
  
  |-Pre_Augmented_Raman_Picture
  
  |-Raman_Data
  
  |-py_files
  
  |-test/
  
  |-preprocessing.py
    
  |-Augmentation.py
    
  |-pic_class.py
    
  |-TrainTestSplit.py
    
    |-test_Augmentation.py
    
    |-test_pic_class.py
    
    |-test_preprocessing.py
    
    |-test_TrainTestSplit.py
    
  |-trainingdata_Pictures/
  
    |-fluorescent_Pictures
    
    |-nylon_Pictures
    
    |-others_Pictures
    
    |-polyamide_Pictures
    
    |-polyethylene_Pictures
    
  |-validationdata_Pictures
  
    |-fluorescent_Pictures
    
    |-nylon_Pictures
    
    |-others_Pictures
    
    |-polyamide_Pictures
    
    |-polyethylene_Pictures
    
  |-IPYNB Files/
  
    |-Data Augmentation .ipynb
    
    |-Data Preprocessing - creating an image database for training and testing the program.ipynb
    
    |-MFramework.ipynb
    
    |-TrainTestSplit .ipynb
    
    |-picture_classification.ipynb
    
  |-Core Model.ipynb
  
  |-Spicy_Raman_Saved_Model.zip
  
  |-Training and Validation Files Generation.ipynb
  
|-use cases and example/

  |-Put_Raman_txt_Files_Here
  
  |-Model.ipynb
  
  |-data_preprocessing.py
  
  |-Put_Raman_txt_Files_Here
  
|-SpicyRaman.yml

|-.gitignore

|-.travis.yml

|-logo.jpg

|-result.jpg

|-usecases.jpg
```

### Instructions
-----------
#### Dependencies:

`pandas` `tensorflow` `os` `matplotlib`
`numpy` `random` `shutil` `zipfile`

#### Installing:

* Open your terninal, `git clone https://github.com/nsuzuki97/Spicy-Raman.git` to download

* To see the files inside, put `cd Spicy-Raman`, `ls`

#### brefore starting

* Open your terminal, put `conda activate SpicyRaman` to change the environment -- `SpicyRaman.yslm` 

#### Training machine and creating the model

* Go to the `model_train_and_validate` directory 

* Put the Raman data txt file into the `Raman_Data` directory

* Go to the `Training and Validation Files Generation.ipynb` file and run it

* Go to the `Core Model.ipynb` file and run it, you can save and zip the model

#### Using the model to predict your own images

* Go to the `use cases and example` folder

* Put your own txt data in `Put_Raman_txt_Files_Here`

* Go to the `data_preprocessing.py` run it, you can get the images

* Go to the `Model.ipynb` and run it, you can get the prediction result of you own images

### The result of the model

![img](https://github.com/nsuzuki97/Spicy-Raman/blob/master/result.png) 
### Data Dependencies
--------
The data was taken from the Luscome Lab, at the University of Washington. When first importing the .txt files from your raman results, please open the use_cases_and_examples directory, then put your files into the put_your_raman_txt_files_here directory.

### Running the nosetests
--------
By using the `nosetests` in the terminal

### Use Case: Example 
-----------
<img src="https://github.com/nsuzuki97/Spicy-Raman/blob/master/usecases.jpg" width="40%">
This is intended for use primarily as an classfication tool for samples obtained from marine biology. This is because the classes of molecules that this program can currently identify are polyethylene, nylon, polyamides, and fluorescent molecules. All other molecules types will be sorted into an "unknown" category, to be manually researched later. 

When using a raman scope in the Nanoes laboratory, the files must be saved to the M or Q drive in order to be accessed outside of the raman room. This should be saved as a .txt file in order to run this program. This data can then be stored in the "Put_Raman_txt_Files_Here" folder within the Use cases and examples. 

When first using the Spicy-Raman program, open the Model (also saved within the Use cases and examples category). Once the model is ran, a list of the probabilities will be shown, along with a resulting classfication inferred from the highest probability. 

### Future work
-----------
In the future, we would like to make functionality improvements in both machine learning aspects, as well as automation of other manual tasks when using a Raman Microscope. Firstly, as the number of identified particles increases, the hope is to increase the capability of the model in identifying an increasing category of Raman spectrum. This will enable future researchers to save more time when analyzing the Raman spectrum of orca (and other) microplastic pollution. 

We would also like to automate the process of physically taking raman spectrums. Currently, the laser is manually focused through a light microscope onto single particles, layed out on filters, after which a spectrum is taken. By using stepmotor/image recognition, we would like the machine to sample though the specimens, automatically collecting raman data.

### Thanks and Acknowledgements
-----------
Special thanks to Dave Beck, Ting Cao and the TAs of the University of Washington Direct Program for help and guidance in learning python and machine learning. Jimin was especially helpful when solving problems related to the TensorFlow model creation and various other difficulties. Thank you Jimin!!!

Also many thanks to freeCodeCamp.org, for free Tensorflow tutorials.

Lastly, thank you so much to the Luscombe Lab and Samantha Phan for access to the raman spectrum data, sorry to increase your workflow in your already busy schedule. 



<img src="http://depts.washington.edu/uwdirect/wordpress/wp-content/uploads/2017/04/uwdirect-logo-w7.png"> <img src="https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/98/2014/09/07214443/Signature_Center_Purple_Hex.png" width="50%">
