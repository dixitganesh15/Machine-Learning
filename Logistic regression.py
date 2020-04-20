# Logistic Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset[['Age','EstimatedSalary']]
y = dataset['Purchased']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score, r2_score
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)
score = r2_score(y_test, y_pred)

