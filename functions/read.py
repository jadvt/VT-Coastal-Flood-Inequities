# read csv function
# x = csv file as string ('')
# y = demographic as string ('')
# z = FF of interest as string ('')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dcor
def read(x,y,z):
    df = pd.read_csv(x)
    df = df.rename(columns={'pop_total':'total'})
    df = df.dropna(subset=['GEOID','NAME','total',y,'non'+y,z])
    df = df[df[z] != 0]
    return df