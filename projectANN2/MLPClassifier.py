import pandas as pd
#model
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from bootstrap import bootstrap
#get data
df = pd.read_csv("CrohnD.csv", na_values='NA')


# df = df.iloc[:,2:]
#
# #processing data
# df['country'].replace('c1',0,inplace=True)
# df['country'].replace('c2',1,inplace=True)
# df['sex'].replace('M',1,inplace=True)
# df['sex'].replace('F',0,inplace=True)
# X  = df.drop(['treat'],axis=1)
# Y  = df['treat']
#
# #neural neural_network
# print ("************ANN2**************")
# model = MLPClassifier(max_iter = 2000)
#
# #grid search
# param_grid = {'hidden_layer_sizes':[(5,), (6,), (7,), (8,), (9,), (10,),
#                                     (11,), (12,), (13,), (14,), (15,), (16,),
#                                     (17,), (18,), (19,), (20,)]}
# grid = GridSearchCV(model, param_grid, cv=5)
# grid.fit(X,Y)
# print ("Grid Search: best parameters:{}".format(grid.best_params_))
#
# #evaluate the best model
# best_model = grid.best_estimator_
#
# predict_y = best_model.predict(X)
# print("Accuracy:{}".format(accuracy_score(Y,predict_y)))
#
# #build the confusion matrix
# labels=['placebo','d1','d2']
# cm = confusion_matrix(Y,predict_y,labels=labels)
# cm_df = pd.DataFrame(cm, index=labels, columns=labels)
# print("Confusion Matrix:\n{}".format(cm_df))
#
# #bootstrapped confidence interval
# print("Confidence interval best MLP:{}".format(bootstrap(best_model,df,'treat')))
#
# #KNN tree
# print ("************Tree**************")
# model = DecisionTreeClassifier()
#
# #grid search
# param_grid = {'max_depth':list(range(1,31)),'criterion':['entropy','gini']}
# grid = GridSearchCV(model, param_grid, cv=5)
# grid.fit(X,Y)
# print ("Grid Search: best parameters:{}".format(grid.best_params_))
#
# #evaluate the best model
# best_model = grid.best_estimator_
# predict_y = best_model.predict(X)
# print("Accuracy:{}".format(accuracy_score(Y,predict_y)))
#
# #build confusion matrix
# cm = confusion_matrix(Y,predict_y,labels=labels)
# cm_df = pd.DataFrame(cm, index=labels, columns=labels)
# print("Confusion Matrix:\n{}".format(cm_df))
#
# #bootstrapped confidence interval
# print("Confidence interval best MLP:{}".format(bootstrap(best_model,df,'treat')))
#
# #KNN
# #KNN tree
# print ("************KNN**************")
# model = KNeighborsClassifier()
#
# #grid search
# param_grid = {'n_neighbors':list(range(1,31))}
# grid = GridSearchCV(model, param_grid, cv=5)
# grid.fit(X,Y)
# print ("Grid Search: best parameters:{}".format(grid.best_params_))
#
# #evaluate the best model
# best_model = grid.best_estimator_
# predict_y = best_model.predict(X)
# print("Accuracy:{}".format(accuracy_score(Y,predict_y)))
#
# #build confusion matrix
# cm = confusion_matrix(Y,predict_y,labels=labels)
# cm_df = pd.DataFrame(cm, index=labels, columns=labels)
# print("Confusion Matrix:\n{}".format(cm_df))
#
# #bootstrapped confidence interval
# print("Confidence interval best MLP:{}".format(bootstrap(best_model,df,'treat')))
