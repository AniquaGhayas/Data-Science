import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load Iris Dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=['sepal_length', 'sepal_width',
             'petal_length', 'petal_width']
)

# Select Features
X = df[['sepal_length', 'sepal_width']]

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("--- K-Means Clustering Completed ---")
print("Cluster Centers:")
print(centroids)

# Plot Clusters
plt.scatter(X['sepal_length'],
            X['sepal_width'],
            c=labels)

# Plot Centroids
plt.scatter(centroids[:,0],
            centroids[:,1],
            marker='X',
            s=200)

plt.title("K-Means Clustering on Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()