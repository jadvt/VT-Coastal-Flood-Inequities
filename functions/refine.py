# refine counties csv
# x = df as variable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dcor
def refine(x):
    df_coastalcounties_refinement = x.groupby('COUNTY')['GEOID'].nunique()
    df_coastalcounties_refinement = df_coastalcounties_refinement[df_coastalcounties_refinement > 5] # excludes counties that have less than 6 census tracts
    df_coastalcounties_refined = pd.merge(left=x, right=df_coastalcounties_refinement, how='right', on='COUNTY')
    df_coastalcounties_refined = df_coastalcounties_refined.sort_values(by='OID_')
    return df_coastalcounties_refined