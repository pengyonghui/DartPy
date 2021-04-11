#### t2ml plot 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
   
def pltt2ml(t2ml, depth, ax, colorLine, lineWideth, alphaVal, labelName):   
    """

    """
    
    ax.plot(t2ml, depth, color = colorLine, lw = lineWideth, alpha = alphaVal, label = labelName)
    ax.set_xscale('log')
    #ax.set_ylim(0.5,2.75)
    ax.invert_yaxis()    
    
    ax.set_ylabel('Depth (m)',fontname="Arial", fontsize=12)
    ax.set_xlabel('$log_{10}(T_2)$ (s)',fontname="Arial", fontsize=12)  
    
    ax.tick_params(which='both', width = 1)
    ax.tick_params(which='major', length = 6)
    ax.tick_params(axis='x', which='minor', bottom = False) # turn off the minor x-ticks
    
#     ax.get_yaxis().set_tick_params(which='both', direction='in')
#     ax.get_xaxis().set_tick_params(which='both', direction='in')
    
    ax.grid(linestyle="-", linewidth = 0.4,  zorder = -10, alpha = 0.9)
    
    
    labels = ['-4','-3','-2','-1', '0', '1']
    xticks = np.logspace(-4,1,len(labels))
    
    
    ax.set_xticks(xticks)
    ax.set_xticklabels(labels)
    for tick in ax.get_xticklabels():
        tick.set_fontname("Arial")
        tick.set_fontsize(10) 
    for tick in ax.get_yticklabels():
        tick.set_fontname("Arial")
        tick.set_fontsize(10)   