import matplotlib.pyplot as plt
import numpy as np
import re
import pandas as pd

#Louisville traffic stop data
c=pd.read_csv("CSVs/LMPD_STOPS_DATA.csv")
#Fayetteville traffic stop data
d=pd.read_csv("CSVs/Traffic_Stops.csv")

print(c[['ACTIVITY_DATE', 'ACTIVITY RESULTS']])
print(d[['stopdate', 'eDesc']])

set1Months = []
set1StopResults = []
set2Months = []
set2StopResults = []

for i in c['ACTIVITY_DATE']:
    date = i.split("/")
    month = date[0]
    set1Months.append(month)
    #if re.match("1[0-2]", month):
    #    set1Months.append(month)
    #else:
    #    set1Months.append("0" + month)

for i in c['ACTIVITY RESULTS']:
    if re.search(r'^C', i):
        set1StopResults.append("C")
    else:
        set1StopResults.append("W")

for i in d['stopdate']:
    month = i.split("/")
    set2Months.append(month[1])

for i in d['eDesc']:
    if re.search(r'^C', i):
        set2StopResults.append("C")
    else:
        set2StopResults.append("W")

set1Months.sort()

df = pd.DataFrame(set1Months, set1StopResults, columns=['Month', 'Results'])
plt.title('Louisville')
plt.xlabel('Month')


plt.hist(df['Month'], bins=12, density=True, alpha=0.6)
plt.bar(['Month', 'Results'])


plt.show()