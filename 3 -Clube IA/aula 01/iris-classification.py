import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split


iris = pd.read_csv('./work/iris.csv')
iris.head()

iris_data = iris.drop(columns='class', axis=1).values
iris_target = iris['class'].values

data_train, data_test, target_train, target_test = train_test_split(iris_data, iris_target, test_size=0.34)

classifier=tree.DecisionTreeClassifier()

classifier.fit(data_train, target_train)

predictions = classifier.predict(data_test)
print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(target_test,predictions))

from sklearn.metrics import confusion_matrix
confusion_matrix(target_test,predictions)

from sklearn.metrics import classification_report
print(classification_report(target_test, predictions))
