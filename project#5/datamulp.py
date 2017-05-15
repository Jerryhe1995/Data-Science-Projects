# Noah Davis & Jie He
# CSC392
# Assignment: Data Manipulation
# References: Dr. Hamel's slides

import pandas as pd, numpy as np

from sklearn import tree, preprocessing
from csc310viz import tree_print
from collections import defaultdict

# Dr. Hamel's slides are creating userwarnings so we're going to suppress them
import warnings
warnings.filterwarnings("ignore")

# Read data
df_og = pd.read_csv("Titanic.csv")

## Preprocess data

# Set working dataframe to original dataframe
df = df_og

# Finder out whether there are any duplicated rows
print("There are "+ str(df.duplicated().sum()) +" duplicated rows")

# Remove duplicates
df = df.drop_duplicates()

# Find out whether there is any missing data (NaNs)
nulls = pd.isnull(df)
for col in nulls:
    print("There are " + str(nulls[col].sum()) + " null values in " + str(col) + ".")

# Deal with missing data:
# Remove rows with missing data
#df = df.dropna(how='any',axis=0)
# or
# Impute values to replace NaN in in whole dataset, since no missing values in target dataframe
for c in df.columns:
    if (pd.isnull(df[c]).sum()!=0):
        df[c].fillna(df[c].mean(),inplace=True)
# Imputing is more accurate in our case

# Drop 'useless' columns: name of passenger (meaningless), index (meaningless), and sex (represented twice)
# would be better to use a generic comprehension for this
df = df.drop(['Name','Unnamed: 0','Sex'],axis=1)

# Get dummy of features (categorical to numerical)
df = pd.get_dummies(df)

# Target column
# would be better to stick this somewhere up top but this is cool for now
target_col = 'Survived'

# Get features
features_df = df.drop([target_col],axis=1)

# Get target
target_df = df[target_col]

# Create a decision tree object
# Using 2 depth because it's very accurate! (> 0.8)
dtree = tree.DecisionTreeClassifier(criterion='entropy',max_depth=2)

# Fit the tree with features and targets using sklearn
dtree.fit(features_df,target_df)

# Print the tree using the provided visualizer
tree_print(dtree,features_df)

# Create a dataframe with original features
predict_df = pd.DataFrame(dtree.predict(features_df)).iloc[:,0]

# check if the tree correctly predicts the original data using sklearn (In this exercise it does not!)
print(predict_df.equals(target_df))

# Check accuracy of model
def model_error(target,predict):

	target = list(target)
	predict = list(predict)
	if len(target) != len(predict):
		raise ValueError
	error = 0
	for t,p in zip(target,predict):
		if t != p:
			error += 1

	return error/len(target)

accuracy = 1 - model_error(target_df,predict_df)

print("Model Accuracy: {}".format(accuracy))

## Boolean indexing and filtering to find patterns, etc
# We can use filtering to figure out whatever we want from the data
# We decided to use Boolean indexing to figure out what the survival rate was
# for each class and each gender within that class

## Survival rates
# any column is OK for count
total = df_og['Survived'].count()
print(total)
total_survived = ((df_og[df_og['Survived']==1])['Survived']).sum()
print(total_survived)
survival_rate = total_survived/total
print("This overall survival rate was: "+str(survival_rate))

# Survival rates for first class
first_total = (df_og[df_og['PClass']=='1st'])['Survived'].count()
first_total_survived = (df_og[df_og['PClass']=='1st'])['Survived'].sum()
first_survival_rate = first_total_survived / first_total
print("This first class survival rate was: "+str(first_survival_rate))
first_m_survivers = ((df_og[df_og['PClass']=='1st'])[df_og['Sex']=='male'])['Survived'].sum()
first_f_survivers = ((df_og[df_og['PClass']=='1st'])[df_og['Sex']=='female'])['Survived'].sum()

# Survival rates for second class
second_total = (df_og[df_og['PClass']=='2nd'])['Survived'].count()
second_total_survived = (df_og[df_og['PClass']=='2nd'])['Survived'].sum()
second_survival_rate = second_total_survived / second_total
print("This second class survival rate was: "+str(second_survival_rate))
second_m_survivers = ((df_og[df_og['PClass']=='2nd'])[df_og['Sex']=='male'])['Survived'].sum()
second_f_survivers = ((df_og[df_og['PClass']=='2nd'])[df_og['Sex']=='female'])['Survived'].sum()

# Survival rates for third class
third_total = (df_og[df_og['PClass']=='3rd'])['Survived'].count()
third_total_survived = (df_og[df_og['PClass']=='3rd'])['Survived'].sum()
third_survival_rate = third_total_survived / third_total
print("This third class survival rate was: "+str(third_survival_rate))
third_m_survivers = ((df_og[df_og['PClass']=='3rd'])[df_og['Sex']=='male'])['Survived'].sum()
third_f_survivers = ((df_og[df_og['PClass']=='3rd'])[df_og['Sex']=='female'])['Survived'].sum()

# With this information in hand we may be able to come up with better ways to impute data. 
# We could find rates for other occurances, as well, and come up with more probabilities to compound
# our decision tree? I dunno but this stuff is fun! :D



