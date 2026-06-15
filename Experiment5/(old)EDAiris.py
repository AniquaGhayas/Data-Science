import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris Dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=[
        'sepal_length',
        'sepal_width',
        'petal_length',
        'petal_width'
    ]
)

df['species'] = [iris.target_names[i] for i in iris.target]

# Display first 5 rows
print("--- First 5 Rows of Iris Dataset ---")
print(df.head())

# A. Variance Calculation
print("\n--- Variance ---")
print(df.iloc[:, 0:4].var())

# B. Standard Deviation Calculation
print("\n--- Standard Deviation ---")
print(df.iloc[:, 0:4].std())

# C. Data Summarization
print("\n--- Data Summarization ---")
print(df.describe())

# D. Distribution Analysis
print("\n--- Distribution Analysis ---")

plt.hist(df['sepal_length'], bins=10)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# E. Statistical Inference (Correlation Matrix)
print("\n--- Correlation Matrix ---")
print(df.iloc[:, 0:4].corr())