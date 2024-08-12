# create lorenz curves
# dft = df total as variable
# dfd = df demographic as variable
# dfnd = df nondemographic as variable
# a = demographic as string ('')
# b = FF of interest as string ('')
# c = Save location as string ('')
# i = Iterator as dictionary
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dcor
def lorenz_curve(dft,dfd,dfnd,a,b,c,i):
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_title(i+' '+b)
    
    x = np.arange(0, 1.1, 0.1) # equations to define eqaulity
    y = x
    
    ax.plot(x, y, color='black',linestyle='--')
    ax.plot(dft['normalized_pop'],dft['normalized_'+b],color='black',linestyle='-')
    ax.plot(dfd['normalized_pop'],dfd['normalized_'+b],color='blue',linestyle='-')
    ax.plot(dfnd['normalized_pop'],dfnd['normalized_'+b],color='orange',linestyle='-')
    
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_xlabel('Cumulative Population Fraction')
    ax.set_ylabel('Cumulative Exposure Population')
    ax.legend(['Equality','Total',a.capitalize(),'Non'+a],loc=2)
    
    plt.savefig('results/LorenzCurves/'+c+'/'+b+'/'+i+'_'+a+'.png', dpi=300, bbox_inches='tight')