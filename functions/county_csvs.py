# create county csvs
# dft = df total as variable
# dct = dictionary of interest as variable
# a = demographic as string ('')
# b = FF of interest as string ('')
# c = Save location as string ('')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dcor
def county_csvs(dft,dct,a,b,c):
    df_coastalcounties = pd.DataFrame(columns=['County','poptotal','pop'+a,'popnon'+a,'Gini_total','Gini_'+a,'Gini_non'+a,'II_total','II_'+a,'II_non'+a,'Area_km2','medHincome','medHvalue','edu'])

    for i in dct:
        # start of calculations
        df_county = dft[dft['NAME'].str.endswith(i)]

        df_county_total = df_county[['GEOID_x','NAME','total',b,'Area_km2','medHincome','medHvalue','edu']]
        df_county_total = df_county_total.sort_values(by=[b],ascending=True) # weighted FF sum serves as the "exposure" value for sorting and analysis
        df_county_total['cum_pop'] = df_county_total['total'].cumsum()
        df_county_total['cum_'+b] = df_county_total[b].cumsum()
        df_county_total['normalized_pop'] = df_county_total['cum_pop']/df_county_total['total'].sum()
        df_county_total['normalized_'+b] = df_county_total['cum_'+b]/df_county_total[b].sum()

        df_county_a = df_county[['GEOID_x','NAME',a,b]]
        df_county_a = df_county_a.sort_values(by=[b],ascending=True)
        df_county_a['cum_pop'] = df_county_a[a].cumsum()
        df_county_a['cum_'+b] = df_county_a[b].cumsum()
        df_county_a['normalized_pop'] = df_county_a['cum_pop']/df_county_a[a].sum()
        df_county_a['normalized_'+b] = df_county_a['cum_'+b]/df_county_a[b].sum()

        df_county_nona = df_county[['GEOID_x','NAME','non'+a,b]]
        df_county_nona = df_county_nona.sort_values(by=[b],ascending=True)
        df_county_nona['cum_pop'] = df_county_nona['non'+a].cumsum()
        df_county_nona['cum_'+b] = df_county_nona[b].cumsum()
        df_county_nona['normalized_pop'] = df_county_nona['cum_pop']/df_county_nona['non'+a].sum()
        df_county_nona['normalized_'+b] = df_county_nona['cum_'+b]/df_county_nona[b].sum()

        poptotal = df_county_total['total'].sum()
        popa = df_county_a[a].sum()
        popnona = df_county_nona['non'+a].sum()

        Gini_total = (0.5 - np.trapz(df_county_total['normalized_'+b],df_county_total['normalized_pop']))/0.5
        Gini_a = (0.5 - np.trapz(df_county_a['normalized_'+b],df_county_a['normalized_pop']))/0.5
        Gini_nona = (0.5 - np.trapz(df_county_nona['normalized_'+b],df_county_nona['normalized_pop']))/0.5

        B10T10_total = np.percentile(df_county_total['normalized_'+b],10)/(1-np.percentile(df_county_total['normalized_'+b],90))
        B10T10_a = np.percentile(df_county_a['normalized_'+b],10)/(1-np.percentile(df_county_a['normalized_'+b],90))
        B10T10_nona = np.percentile(df_county_nona['normalized_'+b],10)/(1-np.percentile(df_county_nona['normalized_'+b],90))
        II_total = np.sqrt((Gini_total**2)+(((1-B10T10_total)**(1/4))**2))/np.sqrt(2) # value of 1/4 is used by Sitthyot et al. (2020), this alpha value is based, then rounded for practicality, on average of all country Gini values
        II_a = np.sqrt((Gini_a**2)+(((1-B10T10_a)**(1/4))**2))/np.sqrt(2)
        II_nona = np.sqrt((Gini_nona**2)+(((1-B10T10_nona)**(1/4))**2))/np.sqrt(2)

        Area_km2 = df_county_total['Area_km2'].sum()
        medHincome_ave = df_county_total['medHincome'].mean()
        medHvalue_ave = df_county_total['medHvalue'].mean()
        edu_ave = (df_county_total['edu']/df_county_total['total']).mean()
        # end of calculations

        # start of results synthesis
        df_coastalcounties = df_coastalcounties.append({'County':i,'poptotal':poptotal,'pop'+a:popa,'popnon'+a:popnona,
                                                    'Gini_total':Gini_total,'Gini_'+a:Gini_a,'Gini_non'+a:Gini_nona,
                                                    'II_total':II_total,'II_'+a:II_a,'II_non'+a:II_nona,
                                                    'Area_km2':Area_km2,'medHincome':medHincome_ave,'medHvalue':medHvalue_ave,'edu':edu_ave}, ignore_index=True)

    df_coastalcounties.to_csv('results/csvs/'+c+'/'+a+'_'+b+'.csv', index=False)
    return df_coastalcounties