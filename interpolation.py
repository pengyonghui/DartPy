# interpolate to make it convenient to plot
from scipy.interpolate import RectBivariateSpline as RBS
from scipy.interpolate import griddata
import numpy as np

def interpolation_RBS(T2, depth, T2dist):
    
    f = RBS(depth, T2, T2dist, kx = 1, ky =1) # kx, ky =1 is linear interpolation
    
    up_T2 = np.geomspace(np.min(T2), np.max(T2), 160)
    up_depth = np.linspace(np.min(depth), np.max(depth), 24)   
    
    zRBS = f(up_depth, up_T2)
    return up_T2, up_depth,zRBS

def interpolation_griddata(T2, depth, T2dist):
    
    grid_T2, grid_depth = np.meshgrid(T2, depth)
    
    up_T2 = np.geomspace(np.min(T2), np.max(T2), 160)
    up_depth = np.linspace(np.min(depth), np.max(depth), 24)   
    
    Xg, Yg = np.meshgrid(up_T2, up_depth)  
    
    points = np.vstack([np.ravel(grid_T2, order ='F'), np.ravel(grid_depth, order ='F')]).T
    values = np.ravel(T2dist, order ='F')
    
    ZGD = griddata(points, values, (Xg, Yg), method = "linear")
    # np.ravel(grid_T2, order ='F') [0.0001, 0.00001....0.0001, 0.000015....10] (960,)
    # np.ravel(grid_depth, order ='F') [0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.....] (960,)
    # Yg.T.shape (160, 24)
    # Xg.T.shape (160, 24)
    # ZGD.shape (160, 24)
    return up_T2, up_depth, ZGD   
