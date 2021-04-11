# load mat file
from scipy.io import loadmat
import numpy as np
def loadMat(path2MatFile):   
    """
    :in path2MatFile: directory to the mat data "*/*.mat"
    :out data: matlab inversion results 
    
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
    :in path2MatFile: directory to the mat data "*/*.mat"
    :out data: matlab inversion results 
    
    """
    data = loadmat(path2MatFile)
    maxFit = data['maxFit']   
    depth = data['depth']
    # depth calibration with the well head
    depth -= depth[0]

    return depth, maxFit