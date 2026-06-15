from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import seaborn as sns

# Load data
df = sns.load_dataset('iris')
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']

# Split data into training and validation parts
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# A. Classification using SVM
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Predictions
y_pred = svm_model.predict(X_test)

print("--- SVM Classification Performance ---")
print("Accuracy Score:", accuracy_score(y_test, y_pred) * 100, "%")