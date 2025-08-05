import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r'D:\fsds\practice codes\datasets\emp_sal.csv')

x = df.iloc[:, 1:2].values
y=df.iloc[:,2].values

# Linear Regression
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)

plt.scatter(x, y, color='red')
plt.plot(x, lin_reg.predict(x), color='blue')
plt.title("Linear Rgeression Model")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

lin_model_pred=lin_reg.predict([[6]])
lin_model_pred

#Polynimial Regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures()
x_poly=poly_reg.fit_transform(x)

poly_reg.fit(x_poly,y)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)

plt.scatter(x,y,color='red')
plt.plot(x, lin_reg2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Position')
plt.ylabel("Salary")
plt.show()

poly_model_pred=lin_reg2.predict(poly_reg.fit_transform([[6]]))
poly_model_pred

from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(x)

poly_reg.fit(x_poly,y)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)

plt.scatter(x,y,color='red')
plt.plot(x, lin_reg2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Position')
plt.ylabel("Salary")
plt.show()

poly_model_pred=lin_reg2.predict(poly_reg.fit_transform([[6]]))
poly_model_pred

from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=5)
x_poly=poly_reg.fit_transform(x)

poly_reg.fit(x_poly,y)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)

plt.scatter(x,y,color='red')
plt.plot(x, lin_reg2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Position')
plt.ylabel("Salary")
plt.show()

poly_model_pred=lin_reg2.predict(poly_reg.fit_transform([[6]]))
poly_model_pred

#SVR model

from sklearn.svm import SVR
svr_reg= SVR()
svr_reg.fit(x,y)

svr_pred=svr_reg.predict([[6]])
print(svr_pred)

svr_reg= SVR(kernel='poly', degree=4)
svr_reg.fit(x,y)

svr_pred=svr_reg.predict([[6]])
print(svr_pred)


svr_reg= SVR(kernel='poly', degree=5)
svr_reg.fit(x,y)

svr_pred=svr_reg.predict([[6]])
print(svr_pred)


svr_reg= SVR(kernel='linear', degree=4, gamma='scale')
svr_reg.fit(x,y)

svr_pred=svr_reg.predict([[6]])
print(svr_pred)

# KNN(K Nearest Nrighbour)

from sklearn.neighbors import KNeighborsRegressor

kn_reg=KNeighborsRegressor()
kn_reg.fit(x, y)

kn_pred= kn_reg.predict([[6]])
print(kn_pred)

# after hyperparameter tuning
kn_reg=KNeighborsRegressor(n_neighbors=3)
kn_reg.fit(x, y)

kn_pred= kn_reg.predict([[6]])
print(kn_pred)

# decision tree

from sklearn.tree import DecisionTreeRegressor
dt_reg=DecisionTreeRegressor()
dt_reg.fit(x,y)

dt_pred=dt_reg.predict([[6]])
print(dt_pred)

#random forest

from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(random_state=0)
rf_reg.fit(x,y)

rf_pred=rf_reg.predict([[6]])
print(rf_pred)


