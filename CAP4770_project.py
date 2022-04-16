import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Louisville traffic stop data
c=pd.read_csv("CSVs/LMPD_STOPS_DATA.csv")
#Fayetteville traffic stop data
d=pd.read_csv("CSVs/Traffic_Stops.csv")

print(c[['ACTIVITY_DATE', 'ACTIVITY RESULTS']])
print(d[['stopdate', 'eDesc']])



