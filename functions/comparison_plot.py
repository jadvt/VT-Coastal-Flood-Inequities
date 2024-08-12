# create comparison plots
# xy = demographic x and y to plot as variable
# xyn = non demographic x and y to plot as variable
# x = x-axis variable as string ('')
# y = y-axis variable as string ('')
# a = demographic as string ('')
# b = FF of interest as string ('')
# c = Save location as string ('')
# d = Save descriptor as string ('')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dcor
def comparison_plot(xy,xyn,x,y,a,b,c,d):
    fig, ax = plt.subplots(figsize=(10,10))

    ax.scatter(xy[0],xy[1], color='blue')
    ax.scatter(xyn[0],xyn[1], color='orange')

    ax.set_title(y+' vs. '+x+' '+b)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.legend([a.capitalize(),'Non'+a],loc=1)
    ax.grid(True)

    dcor_a = dcor.distance_correlation(xy[0],xy[1])
    dcor_nona = dcor.distance_correlation(xyn[0],xyn[1])

    plt.savefig('results/ComparisonPlots/'+c+'/'+a+'_'+b+'_'+d, dpi=300, bbox_inches='tight')
    return dcor_a, dcor_nona