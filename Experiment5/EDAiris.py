import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Using seaborn's quick load for the iris dataframe
df = sns.load_dataset('iris')

print("--- First 5 rows of Iris Dataset ---")
print(df.head())
print()

# A. Variance Calculation
print("--- A. Variance of Features ---")
print(df.var(numeric_only=True))
print()

# B. Standard Deviation Calculation
print("--- B. Standard Deviation of Features ---")
print(df.std(numeric_only=True))
print()

# C. Data Summarization using Pandas
print("--- C. Data Summarization ---")
print(df.describe())
print()

# D. Distribution Analysis
print("--- D. Generating Distribution Analysis Plot ---")
sns.histplot(df['sepal_length'], kde=True)
plt.title("Distribution of Sepal Length")
plt.show()

# E. Statistical Inference (Correlation Matrix)
print("--- E. Statistical Inference (Correlation Matrix) ---")
print(df.corr(numeric_only=True))