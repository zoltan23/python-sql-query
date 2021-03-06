# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing the df
df = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)
#df_2 = pd.read_csv('reviews.tsv', delimiter = '\t', quoting = 3)

# #Reclassify the Amazon ratings into a binary classification
# recode_dict = { 1:0, 2:0, 3:1, 4:1, 5:1 }
# df_2['Ratings'] = df_2['Liked'].map(recode_dict)
# df_2.drop()
# df = pd.merge(df_1, df_2)

#Clean the data
from NLP_functions import cleanData
corpus = cleanData(df['Review'])

#Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = df.iloc[:, -1].values

# Splitting the df into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Fit the KNN model
from NLP_functions import createKNN, createLogistic, createNaiveBayes,createRandomForest, createSVM

# classifier = createKNN(X_train, y_train, 5, 'minkowski', 2)
# classifier = createLogistic(X_train, y_train, 0)
# classifier = createNaiveBayes(X_train, y_train)
# classifier = createRandomForest(X_train, y_train, 250)
classifier = createSVM(X_train, y_train, 'rbf', 0)

#Create model and send to pickle file
from NLP_functions import createPickleModel
createPickleModel(classifier, 'model')

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(cm)
print(report)
print(accuracy_score(y_test, y_pred))






