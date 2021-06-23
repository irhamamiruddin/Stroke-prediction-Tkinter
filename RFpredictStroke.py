
#Random Forest to predict positive symptoms of Covid19

from sklearn import datasets
import pandas as pd
import pickle
data = pd.read_csv('healthcare-dataset.csv')
print(data)

# Import train_test_split function
from sklearn.model_selection import train_test_split
X=data.drop('stroke',axis=1) # Features
y=data['stroke']  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=10) # 70% training and 30% test

#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

clf=RandomForestClassifier(n_estimators=100)

clf.fit(X_train,y_train)  #train model on training set
y_pred=clf.predict(X_test) #predict model on test set

# save the model to disk
filename = 'randomForest_model.sav'
pickle.dump(clf, open(filename, 'wb'))

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

feature_imp = pd.Series(clf.feature_importances_,index=X_train.columns).sort_values(ascending=False)
feature_imp

import matplotlib.pyplot as plt
import seaborn as sns

# Creating a bar plot
sns.barplot(x=feature_imp, y=feature_imp.index)
# Add labels to graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
#plt.legend()
plt.show()
