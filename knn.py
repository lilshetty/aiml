from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

iris_datasets = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris_datasets["data"], iris_datasets["target"], random_state=0)
kn = KNeighborsClassifier(n_neighbors=1)
kn.fit(x_train, y_train)

for i in range(len(x_test)):
    x = x_test[i]
    x_new = np.array([x])
    prediction = kn.predict(x_new)
    actual_class = iris_datasets["target_names"][y_test[i]]
    predicted_class = iris_datasets["target_names"][prediction[0]]
    print("\n Actual: {}, Predicted: {}".format(actual_class, predicted_class))

print("\n Test Score [Accuracy]: {:.2f}".format(kn.score(x_test, y_test)))