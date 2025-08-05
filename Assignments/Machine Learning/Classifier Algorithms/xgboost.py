import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r'D:\fsds\materials\class materials\august\2nd, 4th- ENSAMBLE LEARNING\7.XGBOOST\Churn_Modelling.csv')
X=df.iloc[:,3:-1].values
y=df.iloc[:,-1].values
print(X)
print(y)

#Encoding categorical data
#applying LabelEncoder to gender column
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X[:,2]=le.fit_transform(X[:,2])
print(X)

#applying OneHotEncoder to Geography column
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encodeer', OneHotEncoder(), [1])], remainder='passthrough')
X=np.array(ct.fit_transform(X))
print(X)

#plitting data into train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=0)

from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cf=confusion_matrix(y_test, y_pred)
print(f'here is the confusion matrix: {cf}')

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test, y_pred)
print(f'accuracy score is:{ac}')

bias=classifier.score(X_train, y_train)
print('Bias of the model is: ',bias)

#Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))

from sklearn.metrics import roc_auc_score, roc_curve

# Get predicted probabilities for the positive class
y_probs = classifier.predict_proba(X_test)[:, 1]

# Compute ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = roc_auc_score(y_test, y_probs)

# Plot ROC curve
plt.figure()
plt.plot(fpr, tpr, color='red', label=f'ROC curve (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Characteristic - ROC')
plt.legend(loc="lower right")
plt.grid()
plt.show()