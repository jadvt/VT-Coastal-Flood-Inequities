# create state dfs
# x = df as variable
# y = demographic as string ('')
# z = FF of interest as string ('')
# i = Iterator name as dictionary
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dcor
def state_dfs(x,y,z,i):
    df_state = x[x['NAME'].str.endswith(i)]
    
    df_state_total = df_state[['GEOID','NAME','total',z]]
    df_state_total = df_state_total.sort_values(by=[z],ascending=True) # weighted FF sum serves as the "exposure" value for sorting and analysis
    df_state_total['cum_pop'] = df_state_total['total'].cumsum()
    df_state_total['cum_'+z] = df_state_total[z].cumsum()
    df_state_total['normalized_pop'] = df_state_total['cum_pop']/df_state_total['total'].sum()
    df_state_total['normalized_'+z] = df_state_total['cum_'+z]/df_state_total[z].sum()
    
    df_state_y = df_state[['GEOID','NAME',y,z]]
    df_state_y = df_state_y.sort_values(by=[z],ascending=True)
    df_state_y['cum_pop'] = df_state_y[y].cumsum()
    df_state_y['cum_'+z] = df_state_y[z].cumsum()
    df_state_y['normalized_pop'] = df_state_y['cum_pop']/df_state_y[y].sum()
    df_state_y['normalized_'+z] = df_state_y['cum_'+z]/df_state_y[z].sum()
    
    df_state_nony = df_state[['GEOID','NAME','non'+y,z]]
    df_state_nony = df_state_nony.sort_values(by=[z],ascending=True)
    df_state_nony['cum_pop'] = df_state_nony['non'+y].cumsum()
    df_state_nony['cum_'+z] = df_state_nony[z].cumsum()
    df_state_nony['normalized_pop'] = df_state_nony['cum_pop']/df_state_nony['non'+y].sum()
    df_state_nony['normalized_'+z] = df_state_nony['cum_'+z]/df_state_nony[z].sum()
    return df_state_total, df_state_y, df_state_nony