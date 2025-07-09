import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scipy.stats import variation
from sklearn.metrics import mean_squared_error
import pickle
import os


# import the data
df = pd.read_csv(r"D:\fsds\projects\datasets\salary prediction app\Salary_Data.csv")

# splitting the data into x and y data
x = df.iloc[:, :-1]
y = df.iloc[:, -1]

# splitting into x_train, x_test, y_train, y_test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# building the model
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

# building comparison table
comparison = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(comparison)

# plotting graph for the model
plt.scatter(x_test, y_test, color="blue")
plt.plot(x_train, regressor.predict(x_train), color="red")
plt.title("Salary vs Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()


# caluclating slope value
m_slope = regressor.coef_
print(m_slope)

# calculating c value
c_intercept = regressor.intercept_
print(c_intercept)

# calculating for future
y_12 = m_slope * 12 + c_intercept
print(y_12)

# 8/7/25: stats

mean = df.mean()
df["Salary"].mean()
df["YearsExperience"].mean()

df.median()
df["Salary"].median()
df["YearsExperience"].median()

df["Salary"].mode()
df["YearsExperience"].mode()

df.var()
df["Salary"].var()

df.std()
df["Salary"].std()

# Coeffecient of variance/variation
variation(df.values)
variation(df["Salary"])

# correlation
df.corr()
df["Salary"].corr(df["YearsExperience"])

# skewness
df.skew()
df["Salary"].skew()

# standard error
df.sem()
df["Salary"].sem()

# Z-score
from scipy.stats import stats

df.apply(stats.zscore)
stats.zscore(df["Salary"])

# degree of freeedom
a = df.shape[0]
b = df.shape[1]

degree_of_freedom = a - b
print(degree_of_freedom)

# SSR:
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
y_mean = np.mean(y)
print(y_mean)

SSR = np.sum((y_pred - y_mean) ** 2)
print(SSR)

# SSE
y = y[0:6]
sse = np.sum((y - y_pred) ** 2)
print(sse)

# SST
sst = SSR + sse
print(sst)

# R Square
r_sqaure = 1 - (SSR / sst)
print(r_sqaure)

bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test, y_test)
print(variance)


# MSE
train_mse = mean_squared_error(y_train, regressor.predict(x_train))
test_mse = mean_squared_error(y_test, y_pred)
print(train_mse, test_mse)


# pickle
filename = "linear_regression_model.pkl"
with open(filename, "wb") as file:
    pickle.dump(regressor, file)
print("Model has been picleled and saved as linear_regression_model.pkl")

# all ml algorithms are saved in .pkl format
# pkl files are 1kb which makes them easy to integrate with frontend


os.getcwd()
