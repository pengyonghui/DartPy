# 2-D T2-dist plotting at a single frequency

import numpy as np
import matplotlib.pyplot as plt
import os.path

import getBoreholeName as gbn
import interpolation as ip
import loadMat as lmat
import pltpcolormesh as pltpcm


if __name__ =="__main__":   
    fileDir = 'D:/Github/DartPy/example-data/data/'
    figDir = 'D:/Github/DartPy/example-data/figure/'
    # when there are many boreholes
    boreholeNames = gbn.getBoreholeName(fileDir)    
    # Dart measurements with two frequencies
    freqs = ['freq1', 'freq2']
    # Dart experiments conducted on Jun and Sep
    months = ['June','sep']      
    
    # a_index = [(0,0),(0,1),(1,0),(1,1)] # index to simplize the index 
    # a for loop when usually there are many boreholes
    for i in range(len(boreholeNames)):    
        # for j in a_index: 
        
        # this is how the inversion *.mat was named
        # select the frequency to visulize the data in each experiment
        # example: a ridge plot of T2-dist measured at freq2 from experiment conducted in Jun 
        fileName = boreholeNames[i] + '_' + freqs[1] + '_' + months[0]   
        
        path2MatFile = os.path.join(fileDir, fileName + '.mat')
        print("Currently working on", fileName)
        # load mat file
        T2, depth, T2dist, T2ml = lmat.loadMat(path2MatFile)  

        fig = plt.figure(figsize=(4,8))
        ax = fig.add_subplot(111)
        # interpolate the data from each depth 
        # both methods in the following working well
#         T2_RBS, depth_RBS,T2dist_RBS = ip.interpolation_RBS(T2, depth, T2dist)
#         pbar = pltpcm.pltpcolormesh(T2_RBS, depth_RBS,T2dist_RBS, ax, T2dist_RBS.max())
        T2_gd, depth_gd,T2dist_gd = ip.interpolation_griddata(T2, depth, T2dist)
        pbar = pltpcm.pltpcolormesh(T2_gd, depth_gd,T2dist_gd, ax,T2dist_gd.max())  
        
        plt.colorbar(pbar)
        fig.tight_layout()
        
#        fig.savefig(os.path.join(figDir, fileName + '_T2dist.eps'))
        fig.savefig(os.path.join(figDir, fileName + '_T2dist.png'), bbox_inches='tight')
        fig.savefig(os.path.join(figDir, fileName + '_T2dist.svg'), format='svg', dpi=1000)
        plt.show()