import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# import dataset
df = pd.read_csv(r"D:\fsds\projects\datasets\House_data.csv")
space = df["sqft_living"]
price = df["price"]

x = np.array(space).reshape(-1, 1)
y = np.array(price)

# splitting the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# applying linear regression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predicting the prices
pred = regressor.predict(x_test)

# visualizing training data
plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, regressor.predict(x_train), color="blue")
plt.title("House Price Prediction")
plt.xlabel("Square Feet")
plt.ylabel("Price")
plt.show()

# visualizing test data
plt.scatter(x_test, y_test, color="green")
plt.plot(x_test, regressor.predict(x_test), color="orange")
plt.title("House Price Prediction")
plt.xlabel("Square Feet")
plt.ylabel("Price")
plt.show()
