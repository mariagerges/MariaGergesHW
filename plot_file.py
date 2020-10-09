import matplotlib.pyplot as plt
import json
import os
from matplotlib.ticker import FuncFormatter, MaxNLocator

#First Graph (Season vs. runtime)

with open ('stranger_things.json') as f:
   data_stranger = json.load(f)

runtimes = []
season = []
for i in range (len(data_stranger['_embedded'])):
    x = (data_stranger['_embedded'])
    l = (x['episodes'])
    for i in range (len(l)):
        y = (l[i])
        z = (y['season'])
        season.append(z)
    print (season)
for i in range (len(data_stranger['_embedded'])):
    f = (data_stranger['_embedded'])
    q = (f['episodes'])
    for i in range (len(q)):
        o = (q[i])
        p = (o['runtime'])
        runtimes.append(p)
    print (runtimes)  

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))   
plt.bar(season, runtimes, color='b')
plt.ylabel('Runtime (Mins')
plt.xlabel('Season')
title = 'Runtimes/Episode for each season of Stranger Things'
plt.title(title)
plt.show()

#Second Graph (year vs. income value) (year vs. number of protected children against tetanus)

with open ('data.json') as m:
    data2 = json.load(m)

year = []
income_value = []
for i in range (len(data2['fact'])):
    x = (data2['fact'][i]) 
    y = (x['dims'])
    u = y.get('GHO')
    if u == "Gross national income per capita (PPP int. $)":
        l = x.get('Value')
        v = (y['YEAR'])
        year.append(v)
        income_value.append(l)
print (year)
print (income_value)
x = list(reversed(year))


year2 = []
protected_number = []
for i in range (len(data2['fact'])):
    x = (data2['fact'][i]) 
    y = (x['dims'])
    u = y.get('GHO')
    if u == "Neonates protected at birth against neonatal tetanus (PAB) (%)":
        l = x.get('Value')
        z = (y['YEAR'])
        year2.append(z)
        protected_number.append(l)
print (year2)
print (protected_number)
y = list(reversed(year2))
   
plo1 = plt.plot(x,income_value)
plot2 = plt.plot(y ,protected_number)
plt.ylabel('Gross National Income') #suggestions for label for the y-axis?
plt.xlabel('year') 
title = 'Egypt Income Data'
plt.title(title)
plt.show()