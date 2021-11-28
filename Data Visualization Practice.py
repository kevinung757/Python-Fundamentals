#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
fig,ax=plt.subplots()
ax.plot(squares)
plt.show()


# In[16]:


#changing the label type and line thickness
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
fig,ax=plt.subplots()
ax.plot(squares,linewidth=3)


#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value", fontsize =14)

#Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()


# In[18]:


#Correcting the Plot

import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares = [1,4,9,16,25]
fig,ax=plt.subplots()
ax.plot(input_values,squares,linewidth=3)


#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value", fontsize =14)

#Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()


# In[30]:


styles= []
mp_styles = plt.style.available
mp_styles.append(styles)
print(mp_styles)


# In[35]:


#Using Built-in Styles
styles= []
mp_styles = plt.style.available
mp_styles.append(styles)

import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares = [1,4,9,16,25]

plt.style.use('ggplot')
fig,ax=plt.subplots()
ax.plot(input_values,squares,linewidth=3)


#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value", fontsize =14)

#Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()


# In[38]:


#Plotting and Styling Individual Points with scatter()
plt.style.use('seaborn')
fig,ax=plt.subplots()

ax.scatter(2,4, s=200)
ax.set_title("Square Numbers",fontsize= 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize =14)

ax.tick_params(axis='both', which ='major', labelsize=14)

plt.show()


# In[41]:


#Plotting a Series of Points with scatter()
x_values= [ 1,2,3,4,5]
y_values = [ 1,4,9,16,25]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,s=100)

ax.set_title("Square Numbers",fontsize = 24)
ax.set_xlabel("Value", fontsize =14)
ax.set_ylabel("Square of Values", fontsize =14)

plt.show()


# In[46]:


#Calculating Data Automatically

x_values= range(1,1001)
y_values= [i**2 for i in x_values]

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,s=10)

ax.set_title("Square Numbers", fontsize= 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Values", fontsize = 14)

#Seet the range for each axis.
ax.axis([0,1100,0,1100000])

plt.show()


# In[48]:


#Defining Custom Colors 
x_values= range(1,1001)
y_values= [i**2 for i in x_values]

plt.style.use('seaborn')
fig,ax=plt.subplots()
#ax.scatter(x_values,y_values,s=10, c='red')
ax.scatter(x_values,y_values,s=10, c=(0,0.8,0))

ax.set_title("Square Numbers", fontsize= 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Values", fontsize = 14)

#Seet the range for each axis.
ax.axis([0,1100,0,1100000])

plt.show()


# In[49]:


#Using a colormap - a series of colors in a gradient that moves from a starting to an ending color.
#You use colormaps in visualizations to emphasize a pattern in the data 

x_values= range(1,1001)
y_values= [i**2 for i in x_values]

plt.style.use('seaborn')
fig,ax=plt.subplots()
#ax.scatter(x_values,y_values,s=10, c='red')
ax.scatter(x_values,y_values,s=10, c=y_values, cmap=plt.cm.Blues)

ax.set_title("Square Numbers", fontsize= 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Values", fontsize = 14)

#Seet the range for each axis.
ax.axis([0,1100,0,1100000])

plt.show()


# In[50]:


#Saving your Plots automatically
x_values= range(1,1001)
y_values= [i**2 for i in x_values]

plt.style.use('seaborn')
fig,ax=plt.subplots()
#ax.scatter(x_values,y_values,s=10, c='red')
ax.scatter(x_values,y_values,s=10, c=y_values, cmap=plt.cm.Blues)

ax.set_title("Square Numbers", fontsize= 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Values", fontsize = 14)

#Seet the range for each axis.
ax.axis([0,1100,0,1100000])

plt.savefig('squares_plot.png',bbox_inches='tight')


# In[54]:


#Practice
x_values= range(1,5001)
y_values= [i**3 for i in x_values]

plt.style.use('seaborn')
fig,ax=plt.subplots()
#ax.scatter(x_values,y_values,s=10, c='red')
ax.scatter(x_values,y_values,s=10, c=y_values, cmap=plt.cm.Reds)

ax.set_title("Cubed Numbers", fontsize= 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Values", fontsize = 14)

#Seet the range for each axis.
#ax.axis([0,1100,0,1100000])

plt.savefig('squares_plot.png',bbox_inches='tight')


# In[ ]:


#Random Walks -Path that has no clear diretion but is determined by a series of random decisons, each of 
#which is entirely left to chance.
#Creating the RandomWalk Class
 
from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self,num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points=num_points
        
        #All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]
        


# In[56]:


#Choosing Directions
from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self,num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points=num_points
        
        #All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calculate all the points in the walk."""
        
        #Keep taking steps until the walk reaches the desired length. 
        while len(self.x_values) < self.num_points:
            
            #Decide which direction to go and how far to go in that direction.
            x_direction =choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step=x_direction*x_distance
            
            y_direction =choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step=y_direction*y_distance
            
            #Reject moves that no nowhere.
            if x_step == 0 and y_step == 0:
                continue
                
            #Calculate the new position
            x=self.x_values[-1] + x_step
            y=self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)


# In[60]:


#Plotting the Random Walk

#Make a random walk

rw=RandomWalk()
rw.fill_walk()

plt.style.use('seaborn')
fig,ax =plt.subplots()
ax.scatter(rw.x_values,rw.y_values,s=15,c='red')
plt.show()


# In[64]:


#Generating Multiple Random Walks

#Keep making new walks, as long as the program is active.
while True:
    rw=RandomWalk()
    rw.fill_walk()
    
    plt.style.use('seaborn')
    fig,ax =plt.subplots()
    ax.scatter(rw.x_values,rw.y_values,s=15,c='red')
    plt.show()
    
    keep_running=input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


# In[67]:


#Styling the Walk
#Coloring the Points


    rw=RandomWalk()
    rw.fill_walk()
    
    plt.style.use('seaborn')
    fig,ax =plt.subplots()
    point_numbers =range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,s=15,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none')
    plt.show()
    


# In[70]:


#Plotting the Starting and Ending Points


rw=RandomWalk()
rw.fill_walk()

plt.style.use('seaborn')
fig,ax =plt.subplots()
point_numbers =range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,s=15,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none')

#Emphasize the first and last points.
ax.scatter(0,0,c='green',edgecolors='none',s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

plt.show()


# In[71]:


#Cleaning up the Axes

#Plotting the Starting and Ending Points


rw=RandomWalk()
rw.fill_walk()

plt.style.use('seaborn')
fig,ax =plt.subplots()
point_numbers =range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,s=15,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none')

#Emphasize the first and last points.
ax.scatter(0,0,c='green',edgecolors='none',s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()


# In[74]:


#Adding Plot Points

#Plotting the Starting and Ending Points


rw=RandomWalk(50000)
rw.fill_walk()

plt.style.use('seaborn')
fig,ax =plt.subplots()
point_numbers =range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,cmap=plt.cm.Reds,edgecolors='none')

#Emphasize the first and last points.
ax.scatter(0,0,c='green',edgecolors='none',s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='blue',edgecolors='none',s=100)

plt.show()


# In[79]:


#Altering the Size to Fill the Screen

rw=RandomWalk(50000)
rw.fill_walk()

plt.style.use('seaborn')
fig,ax =plt.subplots(figsize=(15,9))
point_numbers =range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,cmap=plt.cm.Reds,edgecolors='none')

#Emphasize the first and last points.
ax.scatter(0,0,c='green',edgecolors='none',s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='blue',edgecolors='none',s=100)

plt.show()


# In[8]:


#Rolling Dice with Plotly
#Creating the Dice Class

from random import randint
class Die:
    """A class representing a single die"""
    
    def __init__(self, num_sides=6):
        """Assumes a six-sided die"""
        self.num_sides=num_sides
        
    def roll(self):
        """Return a random value between 1 and 6"""
        return randint(1,self.num_sides)
Die().roll()


# In[9]:


#Rolling the Die

#Create a 6sided die
die =Die()

#Roll some dice and store the results in a list
results=[]

for result in range(100):
    result=die.roll()
    results.append(result)
print(results)


# In[10]:


#Analyzing the Results
die =Die()

#Roll some dice and store the results in a list
results=[]

for result in range(1000):
    result=die.roll()
    results.append(result)

frequencies=[]
for i in range(1,die.num_sides+1):
    frequency=results.count(i)
    frequencies.append(frequency)
print(frequencies)


# In[11]:


pip install  --user plotly


# In[12]:


#Making a Histogram
from plotly.graph_objs import Bar,Layout
from plotly import offline

die =Die()
results=[]

for result in range(1000):
    result=die.roll()
    results.append(result)

frequencies=[]
for i in range(1,die.num_sides+1):
    frequency=results.count(i)
    frequencies.append(frequency)

#Visualize the results.
x_values=list(range(1,die.num_sides+1))
data=[Bar(x=x_values,y=frequencies)]

x_axis_config= {'title': 'Result'}
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling one D6 1000 times',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout} , filename = 'd6.html')


# In[14]:


#rolling 2 dice

from plotly.graph_objs import Bar,Layout
from plotly import offline

die_1 =Die()
die_2=Die()
results=[]

for result in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

frequencies=[]
max_results= die_1.num_sides+die_2.num_sides
for i in range(2,max_results+1):
    frequency=results.count(i)
    frequencies.append(frequency)

#Visualize the results.
x_values=list(range(2,max_results+1))
data=[Bar(x=x_values,y=frequencies)]

x_axis_config= {'title': 'Result','dtick':1}
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling two D6 1000 times',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout} , filename = 'd6_d6.html')


# In[15]:


#Rolling Dice of Different Sizes

from plotly.graph_objs import Bar,Layout
from plotly import offline

die_1 =Die()
die_2=Die(10)
results=[]

for result in range(50000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

frequencies=[]
max_results= die_1.num_sides+die_2.num_sides
for i in range(2,max_results+1):
    frequency=results.count(i)
    frequencies.append(frequency)

#Visualize the results.
x_values=list(range(2,max_results+1))
data=[Bar(x=x_values,y=frequencies)]

x_axis_config= {'title': 'Result','dtick':1}
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling D10 & D6 50000 times',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout} , filename = 'd6_d10.html')


# In[ ]:


CHAPTER 16 -DOWNLOADING DATA


# In[25]:


#The CSV File Format
#Parsing the CSV File Headers

import csv
import pandas as pd

filename ="sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)
    
df= pd.read_csv("sitka_weather_07-2018_simple.csv")
df.head(0)


# In[33]:


#Printing the Headers and Their Positions
 
import csv
import pandas as pd

filename ="sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)

    for index,column_headers in enumerate(header_row):
        print(index,column_headers)


# In[48]:


#Extracting and Reading Data

import csv
import pandas as pd

filename ="sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    highs=[]
    for i in reader:
        tmax=int(i[5])
        highs.append(tmax)
print(highs)


# In[50]:


#Plotting Data in a temperature chart

import matplotlib.pyplot as plt

filename ="sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    highs=[]
    for i in reader:
        tmax=int(i[5])
        highs.append(tmax)

#Plot the High temperatures

plt.style.use('seaborn')
fix,ax=plt.subplots()
ax.plot(highs, c='red')



#Format Plot
ax.set_title("Daily high temperatures, July 208", fontsize = 24)
ax.set_xlabel("", fontsize = 16)
ax.set_ylabel("Temperature (F)", fontsize =16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()


# In[56]:


#The dattime Module
#Plotting Data in a temperature chart

import matplotlib.pyplot as plt
from datetime import datetime

firstdate=datetime.strptime('2018-07-01', '%Y-%m-%d')
print(firstdate)


# In[64]:


#Plotting Dates
import matplotlib.pyplot as plt
from datetime import datetime

filename ="sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs=[],[]
    for i in reader:
        current_date=datetime.strptime(i[2],'%Y-%m-%d')
        tmax=int(i[5])
        highs.append(tmax)
        dates.append(current_date)
    
#Plot the High temperatures

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs, c='red')



#Format Plot
ax.set_title("Daily high temperatures, July 208", fontsize = 24)
ax.set_xlabel("", fontsize = 5)
ax.set_ylabel("Temperature (F)", fontsize =16)
fig.autofmt_xdate()
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()


# In[66]:


#Plotting a Longer Timeframe
import matplotlib.pyplot as plt
from datetime import datetime

filename ="sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs=[],[]
    for i in reader:
        current_date=datetime.strptime(i[2],'%Y-%m-%d')
        tmax=int(i[5])
        highs.append(tmax)
        dates.append(current_date)
    
#Plot the High temperatures

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs, c='red')



#Format Plot
ax.set_title("Daily high temperatures- 2018", fontsize = 24)
ax.set_xlabel("", fontsize = 5)
ax.set_ylabel("Temperature (F)", fontsize =16)
fig.autofmt_xdate()
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()


# In[71]:


#Plotting a 2nd data series
import matplotlib.pyplot as plt
from datetime import datetime

filename ="sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs,lows =[],[], []
    for i in reader:
        current_date=datetime.strptime(i[2],'%Y-%m-%d')
        low= int(i[-1])
        tmax=int(i[5])
        highs.append(tmax)
        dates.append(current_date)
        lows.append(low)
    
#Plot the High temperatures

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs ,c='red')
ax.plot(dates,lows ,c='blue')


#Format Plot
ax.set_title("Daily highs & lows temperatures - 2018", fontsize = 24)
ax.set_xlabel("", fontsize = 5)
ax.set_ylabel("Temperature (F)", fontsize =16)
fig.autofmt_xdate()
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()


# In[72]:


#Shading an Area in the Chart

import matplotlib.pyplot as plt
from datetime import datetime

filename ="sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs,lows =[],[], []
    for i in reader:
        current_date=datetime.strptime(i[2],'%Y-%m-%d')
        low= int(i[-1])
        tmax=int(i[5])
        highs.append(tmax)
        dates.append(current_date)
        lows.append(low)
    
#Plot the High temperatures

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs ,c='red',alpha=0.5)
ax.plot(dates,lows ,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=.1)


#Format Plot
ax.set_title("Daily highs & lows temperatures - 2018", fontsize = 24)
ax.set_xlabel("", fontsize = 5)
ax.set_ylabel("Temperature (F)", fontsize =16)
fig.autofmt_xdate()
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()


# In[76]:


#Error Checking 

import matplotlib.pyplot as plt
from datetime import datetime

filename ="death_valley_2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs,lows =[],[], []
    for i in reader:
        current_date=datetime.strptime(i[2],'%Y-%m-%d')
        try:
            low= int(i[5])
            tmax=int(i[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(tmax)
            dates.append(current_date)
            lows.append(low)
    
#Plot the High temperatures

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs ,c='red',alpha=0.5)
ax.plot(dates,lows ,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=.1)


#Format Plot
ax.set_title("Daily highs & lows temperatures - 2018", fontsize = 24)
ax.set_xlabel("", fontsize = 5)
ax.set_ylabel("Temperature (F)", fontsize =16)
fig.autofmt_xdate()
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()


# In[82]:


#Mapping Global Data Sets: JSON Format

import json

#Explore the structure of the data
filename = "eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)

readable_file= 'readable_eq_data.json'
with open(readable_file,'w') as f:
    json.dump(all_eq_data,f,indent=4)


# In[85]:


#Making a List of All Earthquakes
import json

#Explore the structure of the data
filename = "eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)
all_eq_dicts= all_eq_data['features']
print(len(all_eq_dicts))

#158 earthquakes


# In[86]:


#Extracting Magnitudes
import json

#Explore the structure of the data
filename = "eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)
all_eq_dicts= all_eq_data['features']

mags=[]
for i in all_eq_dicts:
    mag=i['properties']['mag']
    mags.append(mag)
    
print(mags[:10])


# In[88]:


#Extracting Location Data
import json

#Explore the structure of the data
filename = "eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)
all_eq_dicts= all_eq_data['features']

mags, lons, lats = [], [], []
for i in all_eq_dicts:
    mag=i['properties']['mag']
    lon=i['geometry']['coordinates'][0]
    lat=i['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
print(mags[:10])
print(lons[:5])
print(lats[:5])


# In[1]:


#Building a World Map

import json 
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline
filename = "eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)
all_eq_dicts= all_eq_data['features']

mags, lons, lats = [], [], []
for i in all_eq_dicts:
    mag=i['properties']['mag']
    lon=i['geometry']['coordinates'][0]
    lat=i['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
data=[Scattergeo(lon=lons, lat= lats)]
my_layout=Layout(title="Global Earquakes")

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')


# In[ ]:


#A different Way of Specifying Chart Data 

#DIFFERENT APPROACH TO data =[Scattergeo(lon =lons,lat=lats)]

#data = [{'type':'scattergeo', 'lon': lons, 'lat': lats,}]


# In[3]:


#Customizing Marker Size 


import json 
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline
filename = "eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)
all_eq_dicts= all_eq_data['features']

mags, lons, lats = [], [], []
for i in all_eq_dicts:
    mag=i['properties']['mag']
    lon=i['geometry']['coordinates'][0]
    lat=i['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
data=[{'type': 'scattergeo', 'lon': lons, 'lat': lats ,'marker':{'size':[5*mag for mag in mags],},}]
my_layout=Layout(title="Global Earquakes")

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')


# In[5]:


#Customizing Marker Colors
import json 
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline
filename = "eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)
all_eq_dicts= all_eq_data['features']

mags, lons, lats = [], [], []
for i in all_eq_dicts:
    mag=i['properties']['mag']
    lon=i['geometry']['coordinates'][0]
    lat=i['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
data=[{'type': 'scattergeo', 'lon': lons, 'lat': lats ,'marker':{'size':[5*mag for mag in mags],'color':mags,
'colorscale':'Viridis','reversescale':True,'colorbar': {'title': 'Magnitude'}},}]
my_layout=Layout(title="Global Earquakes")

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')


# In[10]:


#Other Colorscales

from plotly import colors
for i in colors.PLOTLY_SCALES.keys():
    print(i)


# In[11]:


print(colors.PLOTLY_SCALES)


# In[13]:


#Adding Hover Text

import json 
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline
filename = "eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)
all_eq_dicts= all_eq_data['features']

mags, lons, lats ,hover_text = [], [], [] , []
for i in all_eq_dicts:
    mag=i['properties']['mag']
    lon=i['geometry']['coordinates'][0]
    lat=i['geometry']['coordinates'][1]
    title=i['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)
    
data=[{'type': 'scattergeo', 'lon': lons, 'lat': lats , 'text': hover_text, 'marker':{'size':[5*mag for mag in mags],
'color':mags,'colorscale':'Viridis','reversescale':True,'colorbar': {'title': 'Magnitude'}},}]
my_layout=Layout(title="Global Earquakes")

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')


# In[ ]:


CHAPTER 17- Working APIs application programming interface


# In[ ]:


#Using a Web API


# In[17]:


#Requesting Data Using an API Call

import requests

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers= {'Accept': 'application/vnd.github.v3+json'}  #Asking to use this version of the API ...3rd
r=requests.get(url,headers=headers)  #This makes the call to the api
print(f"Status code: {r.status_code}")

#Store API response in a variable
response_dict = r.json()

#Proccess the results.
print(response_dict.keys())

#status code of 200 means successfull


# In[34]:


#Working with the Response Dictionary
import requests

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers= {'Accept': 'application/vnd.github.v3+json'}  #Asking to use this version of the API ...3rd
r=requests.get(url,headers=headers)  #This makes the call to the api

#Store API response in a variable
response_dict = r.json()
print(f"Total repositories : {response_dict['total_count']}")

#Explore the information about the repositories
repo_dict=response_dict['items']
print(f"Repositories returned: {len(repo_dict)}")

#Examine the first repository.
repo_dict=repo_dict[0]
print(f"\nKeys: {len(repo_dict)}")
#for i in sorted(repo_dict.keys()):
  #  print(i)
print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")


# In[39]:


#Working with the Response Dictionary
import requests

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers= {'Accept': 'application/vnd.github.v3+json'}  #Asking to use this version of the API ...3rd
r=requests.get(url,headers=headers)  #This makes the call to the api

#Store API response in a variable
response_dict = r.json()
print(f"Total repositories : {response_dict['total_count']}")

#Explore the information about the repositories
repo_dict=response_dict['items']
print(f"Repositories returned: {len(repo_dict)}")

#Examine the first repository.

print(f"\nKeys: {len(repo_dict)}")
#for i in sorted(repo_dict.keys()):
  #  print(i)
print("\nSelected information about each repository:")
for repo_dict in repo_dict:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")


# In[ ]:


#Monitoring API Rate Limits
api.github.com/rate_limit

#Many APIs require you to register and obtain an API key to make an API calls.


# In[11]:


#Visualizing Repositories using Plotly
import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers= {'Accept': 'application/vnd.github.v3+json'}  #Asking to use this version of the API ...3rd
r=requests.get(url,headers=headers)  #This makes the call to the api
print(f"Status Code: {r.status_code}")

#Process Results
response_dict=r.json()
repo_dicts=response_dict['items']
repo_names,stars = [],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
#Make visualization
data =[{'type':'bar', 'x':repo_names, 'y': stars,'marker': {'color': 'rgb(60,100,150)','line': {'width': 1.5,'color':'rgb(25,25,25)'}},'opacity':0.6,}]
my_layout = {'title': 'Most-Starred Python Projects on Github', 'titlefont': {'size':28},
'xaxis': {'title':'Repository','titlefont':{'size': 24},'tickfont':{'size':14},}
,'yaxis':{'title':'Stars','titlefont':{'size': 24},'tickfont':{'size':14},},}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')


# In[17]:


#Adding Custom Tooltips

import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers= {'Accept': 'application/vnd.github.v3+json'}  #Asking to use this version of the API ...3rd
r=requests.get(url,headers=headers)  #This makes the call to the api
print(f"Status Code: {r.status_code}")

#Process Results
response_dict=r.json()
repo_dicts=response_dict['items']
repo_names,stars ,labels= [],[],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    owner=repo_dict['owner']['login']
    description =repo_dict['description']
    label=f"{owner}<br />{description}"
    labels.append(label)
    
#Make visualization
data =[{'type':'bar', 'x':repo_names, 'y': stars,'hovertext':labels,'marker': {'color': 'rgb(60,100,150)','line': {'width': 1.5,'color':'rgb(25,25,25)'}},'opacity':0.6,}]
my_layout = {'title': 'Most-Starred Python Projects on Github', 'titlefont': {'size':28},
'xaxis': {'title':'Repository','titlefont':{'size': 24},'tickfont':{'size':14},}
,'yaxis':{'title':'Stars','titlefont':{'size': 24},'tickfont':{'size':14},},}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')


# In[21]:


#Adding Clickable Links to Our Graph
import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers= {'Accept': 'application/vnd.github.v3+json'}  #Asking to use this version of the API ...3rd
r=requests.get(url,headers=headers)  #This makes the call to the api
print(f"Status Code: {r.status_code}")

#Process Results
response_dict=r.json()
repo_dicts=response_dict['items']
repo_links,stars ,labels= [],[],[]
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_url= repo_dict['html_url']
    repo_link = f"<a href ='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner=repo_dict['owner']['login']
    description =repo_dict['description']
    label=f"{owner}<br />{description}"
    labels.append(label)
    
#Make visualization
data =[{'type':'bar', 'x':repo_links, 'y': stars,'hovertext':labels,'marker': {'color': 'rgb(60,100,150)','line': {'width': 1.5,'color':'rgb(25,25,25)'}},'opacity':0.6,}]
my_layout = {'title': 'Most-Starred Python Projects on Github', 'titlefont': {'size':28},
'xaxis': {'title':'Repository','titlefont':{'size': 24},'tickfont':{'size':14},}
,'yaxis':{'title':'Stars','titlefont':{'size': 24},'tickfont':{'size':14},},}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')


# In[ ]:


#The Hacker News API
import requests 
import json 

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r=requests.get(url)
print(f"Status Code: {r.status_code}")

#Explore the Structure of the data
response_dict =r.json()
readable_file='readable_hn_data.json'
with open(readable_file) as f:
    json.dump(response_dict,f, indent= 4)


# In[28]:


from operator import itemgetter

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")


# In[35]:


#Funny chuck norris api pulls
import requests

# Make an API call and store the response.
url = 'https://api.chucknorris.io/jokes/random'
r = requests.get(url)
print(f"Status code: {r.status_code}")

quotes = r.json()
print(quotes['value'])

