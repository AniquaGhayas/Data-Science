from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd

# Load Iris Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# SVM Classification
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Prediction
y_pred = svm_model.predict(X_test)

print("--- SVM Classification Performance ---")
print("Accuracy Score:", accuracy_score(y_test, y_pred) * 100, "%")