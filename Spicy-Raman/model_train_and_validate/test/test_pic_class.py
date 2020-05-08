import os
import pic_class as pc
import shutil

def test_picture_classification():
    source = os.getcwd()
    source2 = os.path.dirname(source) + '/trainingdata_Pictures'
    with os.scandir(source2) as entries:
        for entry in entries:
            foldername = entry.name
            pnumber = 0
            if foldername.endswith(".jpg") or foldername.endswith(".png"):
                pnumber = pnumber + 1
    assert pnumber is not 0,'There is no pictures in the' + source2
    pc.picture_classification(source2)
    