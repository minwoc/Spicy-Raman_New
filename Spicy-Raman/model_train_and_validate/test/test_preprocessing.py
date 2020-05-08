import numpy as np
import matplotlib.pyplot as plt
# %matplotlib agg
import pandas as pd
import os
import preprocessing as pp


def test_graph_and_save():
    source = os.getcwd()
    big_folder = os.path.dirname(source) + '/Raman_Data'
    data = pd.read_csv(big_folder + '/' + 'fluorescent' + '/' + '20191004 Set3Sample3_10a 1_.txt' , sep='\s+')
    name = 'fluorescent' + "_" + '20191004 Set3Sample3_10a 1_.txt' + ".png"
    assert len(data) is not 2, 'the dataframe needs to have two columns'
    assert isinstance(data, pd.DataFrame) == True, 'you need to put a Dataframe inside'
    pp.graph_and_save(data, name)
    
def test_preprocessing():
    source = os.getcwd()
    big_folder = os.path.dirname(source) + '/Raman_Data'
    with os.scandir(big_folder) as entries:
        for entry in entries:
            foldername = entry.name
            print (foldername)
            subig_folder = os.path.dirname(source) + '/Raman_Data/' + foldername
            with os.scandir(subig_folder) as entries:
                pnumber = 0
                for entry in entries:
                    filename = entry.name
                    if filename.endswith(".txt"):
                        pnumber = pnumber + 1
    assert pnumber is not 0,'There is no txt file in the' + subig_folder
    pp.preprocessing(big_folder)