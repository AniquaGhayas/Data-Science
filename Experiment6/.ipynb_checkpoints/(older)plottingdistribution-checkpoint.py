import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

# Load Iris Dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=['sepal_length','sepal_width',
             'petal_length','petal_width']
)

df['species'] = [iris.target_names[i] for i in iris.target]

# I. Histogram
plt.hist(df['sepal_length'], bins=10)
plt.title('Distribution of Sepal Length')
plt.show()

# II. Density Plot
df['sepal_width'].plot(kind='density')
plt.title('Density Distribution of Sepal Width')
plt.show()

# III. Box Plot
df.boxplot(column='petal_length', by='species')
plt.title('Petal Length by Species')
plt.suptitle('')
plt.show()

# IV. Bar Plot
avg = df.groupby('species')['petal_width'].mean()

plt.bar(avg.index, avg.values)
plt.title('Average Petal Width')
plt.show()