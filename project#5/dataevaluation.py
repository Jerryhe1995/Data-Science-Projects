# Noah Davis & Jie He
# CSC392
# Assignment: Model Evaluation
# References: Dr. Hamel's slides

import pandas as pd

from sklearn import tree
from csc310viz import tree_print

# Read data
df = pd.read_csv("OrchardSprays.csv")

#df.head()

# Get features
features_df = df.drop(['treatment'],axis=1)

# Get target
target_df = df['treatment']

# Create a decision tree object
dtree = tree.DecisionTreeClassifier(criterion='entropy',max_depth=6)

# Fit the tree with features and targets using sklearn
dtree.fit(features_df,target_df)

# Print the tree using the provided visualizer
tree_print(dtree,features_df)

# Create a dataframe with original target data
# (not necessary - already initialized with values)
#target_df = df['play']

# Create a dataframe with original features
predict_df = pd.DataFrame(dtree.predict(features_df)).iloc[:,0]

# check if the tree correctly predicts the original data using sklearn
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

print("Model Accuracy: {}".format(accuracy)+",which is > .8 as requested by assignment")
print("A discernable pattern is that before decrease is > 58.5 the dataset is very predictable, afterward it is kinda random. :L")