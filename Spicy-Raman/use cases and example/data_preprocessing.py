# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


def graph_and_save(data, name):
    y = data.iloc[:, 1]
    x = data.iloc[:, 0]
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(x, y)
    fig.savefig('Raman_Pictures/' + name)
    plt.close('all')


def preprocessing(big_folder):
    os.listdir()
    with os.scandir(big_folder) as entries:
        for entry in entries:
            filename = entry.name
            data = pd.read_csv(big_folder + '/' + filename, sep='\s+')
            name = filename + ".png"
            graph_and_save(data, name)
