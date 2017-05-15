# Noah Davis & Je Hie
# CSC 392
# Assignment: Pie Chart
# References: that link in the assignment and pandas docs

# Import stuff
import matplotlib.pyplot as plt, pandas as pd, numpy as np

# Read csv values
df = pd.read_csv("states.csv") # not hardcoded, see the csv value in the zip.

# Get the first letter of each abbreviation
labels = []
for thing in df['Abbreviation']:
	labels.append(thing[0])

# Use those letters to get the sizes from the dataframe and rename to columns
# doing this lazy because still learning idk
count = df.groupby(labels).size().reset_index().rename(columns={0:'count'})	# get a set with the values we want
labels = list(count['index']) 												# set the labels to be plotted
sizes = list(count['count'].values)											# set other values to be plotted

# Plot using example code
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, shadow=True, startangle=90)
ax1.axis('equal')

# Show the plot
#plt.show()
plt.savefig('pie.pdf')
