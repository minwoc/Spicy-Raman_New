import os
import shutil


def picture_classification(source):
    with os.scandir(source) as entries:
        for entry in entries:
            foldername = entry.name
            if 'polyethylene' in foldername:
                if not os.path.exists('polyethylene_Pictures'):
                    os.makedirs('polyethylene_Pictures')
                shutil.move(source + '/' + foldername, source + '/polyethylene_Pictures')
            elif 'polyamide' in foldername:
                os.chdir(source)
                if not os.path.exists('polyamide_Pictures'):
                    os.makedirs('polyamide_Pictures')
                shutil.move(source + '/' + foldername, source + '/polyamide_Pictures')
            elif 'fluorescent' in foldername:
                os.chdir(source)
                if not os.path.exists('fluorescent_Pictures'):
                    os.makedirs('fluorescent_Pictures')
                shutil.move(source + '/' + foldername, source + '/fluorescent_Pictures')
            elif 'nylon' in foldername:
                os.chdir(source)
                if not os.path.exists('nylon_Pictures'):
                    os.makedirs('nylon_Pictures')
                shutil.move(source + '/' + foldername, source + '/nylon_Pictures')
            else:
                if not os.path.exists('others_Pictures'):
                    os.makedirs('others_Pictures')
                shutil.move(source + '/' + foldername, source + '/others_Pictures')
