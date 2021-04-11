# joyplot the T2-dist at a borehole with many NMR measurements

import numpy as np
import matplotlib.pyplot as plt
import os

import getBoreholeName as gbn
import interpolation as ip
import loadMat as lmat
import pltridge as pltr

if __name__ =="__main__":    
    fileDir = 'D:/Github/DartPy/example-data/data/'
    figDir = 'D:/Github/DartPy/example-data/figure/'
    
    # when there are many boreholes
    boreholeNames = gbn.getBoreholeName(fileDir)
    
    # Dart measurements with two frequencies
    freqs = ['freq1', 'freq2']
    # Dart experiments conducted on Jun and Sep
    months = ['June','sep']    
    
    # this is how the inversion *.mat was named
    # select the frequency to visulize the data in each experiment
    # example: a ridge plot of T2-dist measured at freq2 from experiment conducted in Jun    
    fileName = boreholeNames[0] + '_' + freqs[1] + '_' + months[0]  
    # locate the *mat file
    path2MatFile = os.path.join(fileDir, fileName +'.mat')
    print('Currently working on' + fileName)
    # load mat file
    T2, depth, T2dist, T2ml = lmat.loadMat(path2MatFile)  
    
    fig = plt.figure(figsize=(3,8)) 
    pltr.pltGridSpec(T2, T2dist, depth, fig, hstackspace= -0.7)
    fig.savefig(os.path.join(figDir, fileName + '_ridge.svg'), format='svg', dpi=1000)
    fig.savefig(os.path.join(figDir, fileName + '_ridge.png'), bbox_inches='tight')
    plt.show()