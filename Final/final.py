import pandas
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from bootstrap import bootstrap

df = pandas.read_csv("meals.csv", sep=';')

per_person = df[df['user_id'] == 1]


#
# print(per_person())

#processing data
print ("************Processing data**************")
new_df = per_person.drop(['id','type','log_date','user_id','mood'],axis=1)
change = []
for i in range(int((len(new_df['weight'])-1)/7)):
    if int(new_df['weight'][i*7+7]) >= int(new_df['weight'][i*7]):
        for j in range(7):
            change.append(1)
    else:
        for j in range(7):
            change.append(-1)
food=[]
food_dict= []
for i in range( len( new_df['food'] )-1 ):
    if new_df['food'][i] not in food_dict:
        food.append(len(food_dict))
        food_dict.append(new_df['food'][i])
    else:
        for j in range(len(food_dict)):
            if new_df['food'][i]==food_dict[j]:
                food.append(j)
size = 7* int((len(new_df['weight'])-1)/7)
working_df = pandas.DataFrame({
    'protein': new_df['protein'][:size],
    'cals': new_df['cals'][:size],
    'fat': new_df['fat'][:size],
    'carbs': new_df['carbs'][:size],
    'food':food[:size],
    'weight':change
})
X  = working_df.drop(['weight'],axis=1)
Y  = working_df['weight']

#neural neural_network
print ("************ANN2**************")
model = MLPClassifier(max_iter = 2000)

#grid search
param_grid = {'hidden_layer_sizes':[(5,), (6,), (7,), (8,), (9,), (10,),
                                    (11,), (12,), (13,), (14,), (15,), (16,),
                                    (17,), (18,), (19,), (20,)]}
grid = GridSearchCV(model, param_grid, cv=5)
grid.fit(X,Y)
print ("Grid Search: best parameters:{}".format(grid.best_params_))

#evaluate the best model
best_model = grid.best_estimator_

predict_y = best_model.predict(X)
print("Accuracy:{}".format(accuracy_score(Y,predict_y)))

#build the confusion matrix
labels=[1,-1]
cm = confusion_matrix(Y,predict_y,labels=labels)
cm_df = pandas.DataFrame(cm, index=labels, columns=labels)
print("Confusion Matrix:\n{}".format(cm_df))

#bootstrapped confidence interval
print("Confidence interval best MLP:{}".format(bootstrap(best_model,working_df,'weight')))

#KNN tree
print ("************Tree**************")
model = DecisionTreeClassifier()

#grid search
param_grid = {'max_depth':list(range(1,31)),'criterion':['entropy','gini']}
grid = GridSearchCV(model, param_grid, cv=5)
grid.fit(X,Y)
print ("Grid Search: best parameters:{}".format(grid.best_params_))

#evaluate the best model
best_model = grid.best_estimator_
predict_y = best_model.predict(X)
print("Accuracy:{}".format(accuracy_score(Y,predict_y)))

#build confusion matrix
cm = confusion_matrix(Y,predict_y,labels=labels)
cm_df = pandas.DataFrame(cm, index=labels, columns=labels)
print("Confusion Matrix:\n{}".format(cm_df))

#bootstrapped confidence interval
print("Confidence interval best MLP:{}".format(bootstrap(best_model,working_df,'weight')))

#KNN
#KNN tree
print ("************KNN**************")
model = KNeighborsClassifier()

#grid search
param_grid = {'n_neighbors':list(range(1,31))}
grid = GridSearchCV(model, param_grid, cv=5)
grid.fit(X,Y)
print ("Grid Search: best parameters:{}".format(grid.best_params_))

#evaluate the best model
best_model = grid.best_estimator_
predict_y = best_model.predict(X)
print("Accuracy:{}".format(accuracy_score(Y,predict_y)))

#build confusion matrix
cm = confusion_matrix(Y,predict_y,labels=labels)
cm_df = pandas.DataFrame(cm, index=labels, columns=labels)
print("Confusion Matrix:\n{}".format(cm_df))

#bootstrapped confidence interval
print("Confidence interval best MLP:{}".format(bootstrap(best_model,working_df,'weight')))


