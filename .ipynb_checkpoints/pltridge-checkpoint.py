# reference to https://matplotlib.org/matplotblog/posts/create-ridgeplots-in-matplotlib/
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid_spec

def pltGridSpec(T2, T2dist, depth, fig, hstackspace = - 0.3):
    """
    Creates a standard ridgeline plot with gridspec.
    T2: numpy array of T2 (size = 80 or 160 during inversion)
    data of T2-dist: numpy array with shape number of depth * number of T2
    """
    
    depths = [x for x in np.unique(depth)]
    x_T2 = np.geomspace(np.min(T2), np.max(T2), T2.size)
    len_T2dist = T2dist.shape[0]
    
    gs = grid_spec.GridSpec(len_T2dist,1) 
    
    # in case different colors are needed
    colors = ['#3300cc', '#660099', '#990066', '#ece2f0','#d0d1e6','#a6bddb','#67a9cf','#3690c0','#02818a','#016c59','#014636']

    ax = [ ]
    i = 1

    while i < len_T2dist:

        ax.append(fig.add_subplot(gs[i:i+1, 0]))

        ax[-1].semilogx(T2, T2dist[i,:], c='k', lw = 1)
        ax[-1].fill_between(x_T2, T2dist[i,:], alpha = 1, color= 'g') #where = T2dist[i,:]>0

        ax[-1].set_ylim(0,5) #np.max(T2dist[i,:])
        ax[-1].set_xlim(1e-4, 10)

        ax[-1].set_yticklabels([])
        ax[-1].set_yticks([])
        ax[-1].set_ylabel('')
        # ax[-1].set_xscale('log')

        # make background transparent
        rect = ax[-1].patch
        rect.set_alpha(0)

        # xticks only for the bottom axis
        if i == len_T2dist-1:
            ax[-1].set_xlabel("$T_2 (s)$", fontsize= 14,fontweight="bold")
        else:
            ax[-1].set_xticklabels([])
            ax[-1].set_xticks([])
            ax[-1].set_xticks([], minor=True)
        # boxoff and now show lines    
        spines = ["top","right","left","bottom"]
        for s in spines:
            ax[-1].spines[s].set_visible(False)

        ax[-1].text(1e-4, 0, '{:3.2f}'.format(depths[i]), fontsize=10, ha="right") #rotation=45, fontweight="bold",

        i += 1

    gs.update(hspace = hstackspace)
    return fig

def ridgeline(T2, T2dist, overlap=0, fill=True, labels=None):
    """
    Creates a standard ridgeline plot.
    T2: numpy array of T2 (size = 80 or 160 during inversion)
    data of T2-dist: numpy array with shape number of depth * number of T2
    
    overlap, overlap between distributions. 1 max overlap, 0 no overlap.
    
    fill, matplotlib color to fill the distributions.
        
    labels, values to place on the y axis to describe the distributions.
    """
    if overlap > 1 or overlap < 0:
        raise ValueError('overlap must be in [0 1]')
    x_T2 = np.geomspace(np.min(T2), np.max(T2), T2.size)

    ys = []
    len_T2dist = T2dist.shape[0]
    
    for i in range(len_T2dist-1,-1,-1):        
        y = i*(1.0-overlap)
        ys.append(y)
        if fill:
            plt.fill_between(x_T2, np.ones(T2.size)*y, T2dist[i,:] + y, zorder=len_T2dist-i+1, color=fill)
        plt.plot(x_T2, T2dist[i,:] + y, c ='k', zorder=len_T2dist-i+1)
        
    if labels.any():
        plt.yticks(ys, labels)