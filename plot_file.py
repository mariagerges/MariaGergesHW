import matplotlib.pyplot as plt
import json
import math 
import matplotlib.patches as mpatches
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
        if z not in season:
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

season_1 = []
season_1.append(runtimes[0:8])
avg_1 = sum(season_1[0]) / len(season_1[0])
  

season_2 = []
season_2.append(runtimes[8:17])
avg_2 = sum(season_2[0]) / len(season_2[0])


season_3 = []
season_3.append(runtimes[17:25])
avg_3 = sum(season_3[0]) / len(season_3[0])


season_4 = []
season_4.append(runtimes[25:])
avg_4 = sum(season_4[0]) / len(season_4[0])


average_runtimes = []
average_runtimes.append(avg_1)
average_runtimes.append(avg_2)
average_runtimes.append(avg_3)
average_runtimes.append(avg_4)
print (average_runtimes)


fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))   
plt.bar(season, average_runtimes, color='b')
plt.ylabel('Average Runtime (Mins)')
plt.xlabel('Season')
title = 'Average Runtime for each season of Stranger Things'
plt.title(title)
plt.show()


#Second Graph (year vs. income value) (year vs. Measles - number of reported cases)

with open ('data.json') as m:
    data2 = json.load(m)

income_value = []
year = []
for i in range (len(data2['fact'])):
    x = (data2['fact'][i]) 
    y = (x['dims'])
    u = y.get('GHO')
    if u == "Gross national income per capita (PPP int. $)":
        l = x.get('Value')
        v = (y['YEAR'])
        year.append(v)
        income_value.append(l)
print (income_value)
s= list(reversed(income_value))

reported_cases = {}
for i in range (len(data2['fact'])):
    x = (data2['fact'][i]) 
    y = (x['dims'])
    u = y.get('GHO')
    if u == "Measles - number of reported cases":
        l = x.get('Value')
        z = (y['YEAR'])
        if z in year:
            reported_cases [z] = int(l) 


fig, ax = plt.subplots()
color = 'tab:red'
ax.set_xlabel('YEAR')
ax.set_ylabel('income_value' , color = color)
ax.plot(list(reversed(year)) , list(reversed(income_value)), color = color)
ax.tick_params(axis='y', labelcolor = color)
ax2 = ax.twinx()
color = 'tab:blue'
red_patch = mpatches.Patch(color='red', label='income values/ year')
ax.legend(handles=[red_patch])
ax2.set_ylabel('reported_cases_of_Maesles', color = color)
ax2.plot(list(reversed(year)), reported_cases.values(), color = color)
ax2.tick_params(axis='y', labelcolor = color)
blue_patch = mpatches.Patch(color='blue', label='cases of Maesles/ year')
ax2.legend(handles=[blue_patch], loc ='upper left', bbox_to_anchor=(-0.014, 0.92))
fig.tight_layout()
title = "Egypt Income values/year & number of cases for Maesles/year"
plt.title(title)
plt.show()