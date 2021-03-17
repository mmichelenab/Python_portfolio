import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

state1 = pd.read_csv('states1.csv')
state2 = pd.read_csv('states2.csv')
#print(state1.head(), state2.head())

#putting together al the csv files and concatenating them
files = glob.glob('states*.csv')
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)

#print(us_census.columns, us_census.dtypes)
#print(us_census.head())

# cleaning the income column that has a dollar sing and converting it to numerical
us_census['Income'] = us_census.Income.str[1:]
us_census['Income'] = pd.to_numeric(us_census.Income)

#splitting the Gender Population column, creating to different colums for men and women and converting them to numerical by removing the M and W
split_gender = us_census.GenderPop.str.split('_')
#creating both new columns
us_census['Men'] = split_gender.str.get(0)
us_census['Women'] = split_gender.str.get(1)
#cleaning each column and converting it to numerical
us_census['Men'] = us_census.Men.str[:-1]
us_census['Men'] = pd.to_numeric(us_census.Men)
us_census['Women'] = us_census.Women.str[:-1]
us_census['Women'] = pd.to_numeric(us_census.Women)


#there are Nan values and duplicates
#filling nan values in women columns
us_census = us_census.fillna(value={
'Women': us_census.TotalPop - us_census.Men
})
#deleting duplicates
duplicates = us_census.duplicated(subset=['State'])
print(duplicates.value_counts())
us_census = us_census.drop_duplicates()

#making scatterplot women vs their income
plt.scatter(us_census['Women'], us_census['Income'], color=['red','green'])
plt.xlabel('Women')
plt.ylabel('Income')
plt.show()
plt.cla()

#print(us_census.columns)
#Cleaning data and making scatterplot for each race vs income
us_census['Hispanic'] = us_census.Hispanic.str[:-1]
us_census['Hispanic'] = pd.to_numeric(us_census.Hispanic)
us_census = us_census.fillna(value={
'Hispanic': us_census.Hispanic.mean()})
plt.hist(us_census['Hispanic'])
plt.title('Hispanic')
plt.show()
plt.cla()

us_census['White'] = us_census.White.str[:-1]
us_census['White'] = pd.to_numeric(us_census.White)
us_census = us_census.fillna(value={
'White': us_census.White.mean()})
plt.hist(us_census['White'])
plt.title('White')
plt.show()
plt.cla()

#separate excersice cleaning data with regex
#the thing we are cleaning is a column that has first three leters of a country AUS and next three letters are feature pop AUSpop = australias population
#so separate the big caps from small caps and make twho diferrent columns
country = pd.read_csv("country.csv")

# Extract Country abbreviation and Feature from 'Country_Feature' using regular expressions
sep = country["Country_Feature"].str.extract("(\D{3})(\D{3})")

# Name Columns "Country" and "Feature"
sep.columns = ["Country", "Feature"]

# Merge country and sep
country = pd.concat([country, sep], axis = 1)

# Drop 'Country_Feature' column
country = country.drop(['Country_Feature'], axis = 1)

# Sort Columns to 'Country', 'Feature', and 'Observation'
country = country[["Country", "Feature", "Observation"]]

# Print country
print(country)