# Noah Davis & Jie He
# CSC392
# Assignment: Basic Data Sets

import pandas as pd

from sklearn import tree
from csc310viz import tree_print

# Read data
df = pd.read_csv("Titanic.csv")

#df.head()

# Get features
print("The number of duplicated rows is(are):{}".format(df.duplicated().sum()))
#drop useless data "Name","Sex" and target data "Survived"
features_df = df.drop(['Survived','Name','Sex'], axis=1)
features_df.drop(features_df.columns[[0]],axis=1,inplace=True)
# Get target
target_df = df['Survived']
#data type
#features_df.Mammal.dtype
# Create a decision tree object
#detect the missing data:
md=pd.isnull(features_df).sum()
print('the proportion of missing data out of total data size is =')
print(str(md/pd.isnull(features_df).shape[0]))
print('because the missing data is a big part of our data set, so we can\'t just simply delete it.')
for c in features_df.columns:
    if (pd.isnull(features_df[c]).sum()!=0):
        a=int(features_df[c].mean())
        print (a)
        features_df[c].fillna(a,inplace=True)
# for c in features_df.columns:
features_df['PClass'].replace(to_replace=['1st','2nd','3rd'],value=[int('1'),int('2'),int('3')],inplace=True)
# features_df['PClass'].replace(to_replace='2nd',value=int(2),inplace=True)
# features_df['PClass'].replace(to_replace='3rd',value=int(3),inplace=True)
# features_df=pd.to_numeric(features_df,downcast='signed')
# features_df['PClass'].astype('int',inplace=True)
print (features_df['PClass'].dtype)
print (features_df)
dtree = tree.DecisionTreeClassifier(criterion='entropy')
print (features_df.dtypes)
print (target_df.dtypes)
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
