# load mat file
from scipy.io import loadmat
import numpy as np

def loadMat(path2MatFile):   
    """
    input    
    :path2MatFile: directory to the inverted NMR *.mat data
    parameters in *mat data 
    :'maxFit': maximum value of a T2-disttribution
    :'t2in': The T2 relaxation times
    :'t2mlNum': the mean-log T2 time
    :'dist': T2 distributions from all depths saved in a class of cell
    :'depth': the depth of a borehole where NMR dart data collected 
    
    output 
    :T2: a list of array of T2 predefined ralaxtion times
    :depth: the depth of a borehole where NMR dart data collected
    :T2dist.T (shape: length of T2 * number of depths): the combined T2 distributions from all depths
    :T2ml: the mean-log T2 time at each depth    
    """
    data = loadmat(path2MatFile)
    maxFit = data['maxFit']
    T2 = data['t2in']
    maxDist = data['maxDist']
    T2ml = data['t2mlNum']
    # dist.shape = (1,12)
    dist = data['dist']
    # stacking along rows shape(80,12)
    T2dist = np.hstack((dist[0][:]))
    
    depth = data['depth']
    # depth calibration with the well head
    depth -= depth[0]
    T2 = np.array(T2)
    return T2, depth, T2dist.T, T2ml

def loadMat_WC(path2MatFile):   
    """
    load the initial magnitude/the maxFit from the inversion data
    
    :in path2MatFile: directory to the mat data "*/*.mat"
    :out data: matlab inversion results 
    
    """
    data = loadmat(path2MatFile)
    maxFit = data['maxFit']   
    depth = data['depth']
    # depth calibration with the well head
    depth -= depth[0]

    return depth, maxFit