# create county dfs
# x = df as variable
# y = demographic as string ('')
# z = FF of interest as string ('')
# i = Iterator name as dictionary
def county_dfs(x,y,z,i):
    df_county = x[x['NAME'].str.endswith(i)]
    
    df_county_total = df_county[['GEOID_x','NAME','total',z]]
    df_county_total = df_county_total.sort_values(by=[z],ascending=True) # weighted FF sum serves as the "exposure" value for sorting and analysis
    df_county_total['cum_pop'] = df_county_total['total'].cumsum()
    df_county_total['cum_'+z] = df_county_total[z].cumsum()
    df_county_total['normalized_pop'] = df_county_total['cum_pop']/df_county_total['total'].sum()
    df_county_total['normalized_'+z] = df_county_total['cum_'+z]/df_county_total[z].sum()
    
    df_county_y = df_county[['GEOID_x','NAME',y,z]]
    df_county_y = df_county_y.sort_values(by=[z],ascending=True)
    df_county_y['cum_pop'] = df_county_y[y].cumsum()
    df_county_y['cum_'+z] = df_county_y[z].cumsum()
    df_county_y['normalized_pop'] = df_county_y['cum_pop']/df_county_y[y].sum()
    df_county_y['normalized_'+z] = df_county_y['cum_'+z]/df_county_y[z].sum()
    
    df_county_nony = df_county[['GEOID_x','NAME','non'+y,z]]
    df_county_nony = df_county_nony.sort_values(by=[z],ascending=True)
    df_county_nony['cum_pop'] = df_county_nony['non'+y].cumsum()
    df_county_nony['cum_'+z] = df_county_nony[z].cumsum()
    df_county_nony['normalized_pop'] = df_county_nony['cum_pop']/df_county_nony['non'+y].sum()
    df_county_nony['normalized_'+z] = df_county_nony['cum_'+z]/df_county_nony[z].sum()
    return df_county_total, df_county_y, df_county_nony