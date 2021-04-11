# get the boreholeNames
import os, fnmatch
from collections import OrderedDict

def getBoreholeName(fileDir):
    """
    :in fileDir: directory to the folder
    :out boreholeNames: ordered boreholeNames in a list 
    ['WO03109',
     'WO03118',
     'WO05117',
     'WO07111',
     'WO07116',
     'WO10112',
     'WO10115',
     'WO34113',
     'WO34114',
     'WO34118',
     'WO41112',
     'WO41115',
     'WO41117',
     'WO45116',
     'WO48110',
     'WO55109']    
    """
    
    listOfFiles = os.listdir(fileDir)
    pattern = "*.mat"
    matFile = []
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            matFile.append(entry.split('_')[0])
# '624reshape.mat' was deleted that's why the index is [1:]     
# set to delete the duplicates(without), but results are not in order
    #boreholeNames = list(set(matFile[1:])) 
    boreholeNames = list(OrderedDict.fromkeys(matFile[1:]).keys())
    
    return boreholeNames