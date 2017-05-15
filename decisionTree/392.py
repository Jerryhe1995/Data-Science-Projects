# Noah Davis & Jie He
# CSC392
# Assignment: Data Manipulation
# References: Dr. Hamel's slides

import pandas as pd, numpy as np

from sklearn import tree, preprocessing
from csc310viz import tree_print
from collections import defaultdict

# Read data
df_og = pd.read_csv("Titanic.csv")

## Preprocess data
# Set working dataframe to original dataframe
df = df_og

# Finder out whether there are any duplicated rows
print("There are "+ str(df.duplicated().sum()) + " duplicated rows")

# Remove duplicates
df = df.drop_duplicates()

# Find out whether there is any missing data (NaNs)
print("The total missing data is \n{} ".format(pd.isnull(df).sum()))

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
df = df.drop(['Name','Unnamed: 0','Sex'],axis=1)

# Get dummy of features (categorical to numerical)
df = pd.get_dummies(df)

# Target column
target_col = 'Survived'

## Useless columns
# useless_col = 'Name'

# Get features
features_df = df.drop([target_col],axis=1)

# Get target
target_df = df[target_col]

#print(features_df)

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

# Reverse dummies

def reverse_dummy(df_dummies):
    pos = defaultdict(list)
    vals = defaultdict(list)

    for i, c in enumerate(df_dummies.columns):
        if "_" in c:
            k, v = c.split("_", 1)
            pos[k].append(i)
            vals[k].append(v)
        else:
            pos["_"].append(i)

    dfOut = pd.DataFrame({k: pd.Categorical.from_codes(
                              np.argmax(df_dummies.iloc[:, pos[k]].values, axis=2),
                              vals[k])
                      for k in vals})

    dfOut[df_dummies.columns[pos["_"]]] = df_dummies.iloc[:, pos["_"]]
    return dfOut

print (  (df_og[df_og['PClass']=='3rd'])[df_og['Sex']=='male'].sum()  )

# print(df_og[(df_og['PClass']=='3rd'df_og['Sex']=='male')])
# ['SexCode'].isin(['1'])]   (df_og['Sex']=='male')
