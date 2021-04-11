#### 2-D surf plot 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
   
def pltpcolormesh(xi, yi, zi, ax, Zmax, Zmin = 0):   
    """
    in: gridded data 
    out: 2d surf figure
    
    """ 
    """ 02-16-2021
    MatplotlibDeprecationWarning: shading='flat' when X and Y have the same dimensions as C is deprecated since 3.3.  
    Either specify the corners of the quadrilaterals with X and Y, or pass shading='auto', 'nearest' or 'gouraud', 
    or set rcParams['pcolor.shading'].  This will become an error two minor releases later.
    """
    
    pbar = ax.pcolormesh(xi, yi, zi,  vmin = Zmin, vmax = Zmax, shading='nearest', cmap='RdBu_r',rasterized = True)# coolwarm RdBu_r
    # pbar = ax.pcolormesh(xi, yi, zi,  vmin = Zmin, vmax = Zmax, shading='flat', cmap='RdBu_r',rasterized = True)# coolwarm RdBu_r
    ax.set_xscale('log')
    #ax.set_ylim(0.5,2.75)
    ax.invert_yaxis()    
    
    ax.set_ylabel('Depth (m)',fontname="Arial", fontsize=12)
    ax.set_xlabel('$log_{10}(T_2)$ (s)',fontname="Arial", fontsize=12)  
    
    ax.tick_params(which='both', width = 1)
    ax.tick_params(which='major', length = 6)
    ax.tick_params(axis='x', which='minor', bottom=False) # turn off the minor x-ticks
    
    
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
    return pbar