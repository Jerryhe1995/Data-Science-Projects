## Noah Davis & Jie He 
## CSC 392
## Assignment: Regression
## References: Dr. Hamel's slides

# Imports
# import bootstrap
import matplotlib.pyplot as plt
import pandas

from sklearn.linear_model import LinearRegression   # Linear Regression
from sklearn.tree import DecisionTreeRegressor      # Tree Regression
from sklearn.model_selection import GridSearchCV    # For finding optimal depth
from sklearn.neighbors import KNeighborsRegressor   # KNN Regression

## Pre process data

df = pandas.read_csv("cars.csv", na_values='NA')

# Drop first column as directed
df = df.iloc[:,1:]

# Target is 'dist'
x = df.drop(['dist'],axis=1)    # drop distance column from x
y = df.drop(['speed'], axis=1)  # drop speed column from target, leaving only dist

plt.scatter(x, y)
plt.show()

## Linear Regression

model = LinearRegression(fit_intercept=True)
model.fit(x, y)

print("Model slope: ", model.coef_[0])
print("Model intercept:", model.intercept_)

# Prepare data for plotting
xfit = pandas.DataFrame(df.drop(['dist'],axis=1))
yfit = model.predict(xfit)

# Plot data
plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.show()

# Compute & print the R^2 score
print("R^2 score for Linear Regression: {}".format(model.score(x,y)))


## Decision Tree Regression

model = DecisionTreeRegressor(max_depth=None)
model.fit(x, y)

# Redundant, here for example: reset fitting data
xfit = pandas.DataFrame(df.drop(['dist'],axis=1))
yfit = model.predict(xfit)

plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.show()

# Compute & print the R^2 score
print("R^2 score for Decision Tree Regression: {}".format(model.score(x,y)))

## Grid Search for best parameters

# setting up the grid search
model = DecisionTreeRegressor()

param_grid = {'max_depth': list(range(1,25))}

grid = GridSearchCV(model, param_grid, cv=5)

# performing grid search
grid.fit(x,y)

# print out what we found
print("Best parameters: {}".format(grid.best_params_))


# Redundant, here for example: reset fitting data
xfit = pandas.DataFrame(df.drop(['dist'],axis=1))
yfit = grid.predict(xfit)

plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.show()

# Compute & print the R^2 score
print("R^2 score for Decision Tree with optimized depth ({}".format(grid.best_params_)+") is: {}".format(grid.score(x,y)))

## KNN Regression

model = KNeighborsRegressor(n_neighbors=3)
model.fit(x, y)

# Compute & print the R^2 score
print("R^2 score for KNN Regression: {}".format(model.score(x,y)))

# Redundant, here for example: reset fitting data
xfit = pandas.DataFrame(df.drop(['dist'],axis=1))
yfit = model.predict(xfit)

plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.show()
print("************************************************************************")
print("Decision Tree  performs best on this data set")
