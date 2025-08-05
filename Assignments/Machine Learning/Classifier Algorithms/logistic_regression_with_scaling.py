import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"D:\fsds\projects\datasets\logditic regression\logit classification.csv")

X= df.iloc[:,[2,3]].values
y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

'''from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train= sc.fit_transform(X_train)
X_test=sc.transform(X_test)'''


from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(solver='liblinear', penalty="l1")
classifier.fit(X_train, y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cn=confusion_matrix(y_test, y_pred)
print(f'Here is the confusion matrix: \n{cn}')

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test, y_pred)
print('Accuracy of the model is: ',ac)

from sklearn.metrics import classification_report
cr=classification_report(y_pred, y_pred)
print('Below is the Classification Report: \n',cr)

bias=classifier.score(X_test, y_test)
print('Bias of the model is: ',bias)

variance=classifier.score(X_test, y_test)
print('Variance of the model is: ',variance)


# prediction woth validation data

val_df= pd.read_csv(r'D:\fsds\projects\datasets\logditic regression\final1.csv')
df1=val_df.copy()

val_df=val_df.iloc[:,[3,4]].values

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
m=sc.fit_transform(val_df)
y1_pred=pd.DataFrame()
df1['y1_pred']=classifier.predict(m)

'''df1.to_csv('validation data.csv')

import os
os.getcwd()'''

from sklearn.svm import SVR
classifier=SVR()
classifier.fit(X_train, y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cn=confusion_matrix(y_test, y_pred)
print(f'Here is the confusion matrix: \n{cn}')

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test, y_pred)
print('Accuracy of the model is: ',ac)

from sklearn.metrics import classification_report
cr=classification_report(y_pred, y_pred)
print('Below is the Classification Report: \n',cr)

bias=classifier.score(X_test, y_test)
print('Bias of the model is: ',bias)

variance=classifier.score(X_test, y_test)
print('Variance of the model is: ',variance)
