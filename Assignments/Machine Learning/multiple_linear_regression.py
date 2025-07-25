import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

df=pd.read_csv(r'D:\fsds\projects\datasets\Multiple linear regression for investments\Investment.csv')

x = df.iloc[:,:-1]
y = df.iloc[:,4]

x = pd.get_dummies(x, dtype=int)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

bias = regressor.score(x_train, y_train)
bias

variance = regressor.score(x_test, y_test)
variance

m_slope = regressor.coef_
print(m_slope)

intercept = regressor.intercept_
print(intercept)

x = np.append(arr=np.ones((50,1)).astype(int), values=x, axis=1)

x_opt = x[:,[0,1,2,3,4,5]]
regressor_ols=sm.OLS(endog=y, exog=x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,1,2,3,5]]
regressor_ols=sm.OLS(endog=y, exog=x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,1,2,3]]
regressor_ols=sm.OLS(endog=y, exog=x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,1,3]]
regressor_ols=sm.OLS(endog=y, exog=x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,1]]
regressor_ols=sm.OLS(endog=y, exog=x_opt).fit()
regressor_ols.summary()


