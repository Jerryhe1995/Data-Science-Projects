# Noah Davis & Jie He
# CSC392
# Assignment: Basic Data Sets

import pandas as pd
from model_error import model_error
from sklearn import tree
from csc310viz import tree_print

# Read data
df = pd.read_csv("tennis_numeric.csv")

#df.head()

# Get features
features_df = df.drop(['play'],axis=1)

# Get target
target_df = df['play']

# Create a decision tree object
dtree = tree.DecisionTreeClassifier(criterion='entropy',max_depth=2)
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
print("Tree predicts training data:{}".format(predict_df.equals(target_df)))
accuracy = 1- model_error(target_df,predict_df)
print("Model Accuracy:{}".format(accuracy))
