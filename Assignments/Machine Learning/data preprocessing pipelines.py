import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#import data
dataset = pd.read_csv(r'C:\Users\bhara\Downloads\Data.csv')



x = dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

plt.plot([1,2,3,4],[1,4,9,16])
plt.show()
# raw data is converted to clean data using eda methods
#sklearn has math+linear algebra+ds+stats
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(strategy='most_frequent')

imputer = imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

from sklearn.preprocessing import LabelEncoder
labelencoder_x=LabelEncoder()

labelencoder_x.fit_transform(x[:,0])
x[:,0]=labelencoder_x.fit_transform(x[:,0])

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#data is split into train and test 
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.3, random_state=0) # when random_state is set to 0, same split happens everytime the code is executed. 
