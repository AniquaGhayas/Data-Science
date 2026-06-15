import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load Iris Dataset
iris = load_iris()
df = pd.DataFrame(
        iris.data,
        columns=['sepal_length','sepal_width',
                 'petal_length','petal_width'
        ]
)
df['species'] = [iris.target_names[i] for i in iris.target]

# A. X-Y GRAPH (Line Plot)
df_sorted = df.sort_values('sepal_length')

plt.plot(df_sorted['sepal_length'],
         df_sorted['sepal_width'])
plt.title("A. X-Y Graph")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

# B. SCATTER PLOT
species = df['species'].unique()

for s in species:
    subset = df[df['species'] == s]
    plt.scatter(subset['petal_length'],
                subset['petal_width'],
                label=s)

plt.title("B. Scatter Plot")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend()
plt.show()

# C. BAR CHART
avg_petal = df.groupby('species')['petal_length'].mean()

plt.bar(avg_petal.index, avg_petal.values)
plt.title("C. Bar Chart")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.show()

# D. PIE CHART
counts = df['species'].value_counts()

plt.pie(counts,
        labels=counts.index,
        autopct='%1.1f%%')
plt.title("D. Pie Chart")
plt.show()