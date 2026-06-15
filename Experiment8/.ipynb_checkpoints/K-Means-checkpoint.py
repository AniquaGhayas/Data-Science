import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
# 1. Load the Iris Dataset
df = sns.load_dataset("iris") # Extract the features for clustering (Sepal Length and Sepal Width) # We pick two features so it is easy to plot on a 2D graph
X = df[["sepal_length", "sepal_width"]]
# 2. Apply K-Means Clustering # We set n_clusters=3 because we know there are 3 species in the Iris dataset
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
# Get the cluster assignments for each data point
labels = kmeans.labels_
# Get the coordinates of the cluster centers (centroids)
centroids = kmeans.cluster_centers_
# Add the predicted clusters back to our dataframe for easy plotting
df["cluster_predicted"] = labels

print("--- K-Means Clustering Completed ---")
print("Cluster Centers (Sepal Length, Sepal Width):")
print(centroids)
print()
# 3. Present and Plot the Data Clusters
# Plot the data points colored by their predicted cluster
sns.scatterplot(
    data=df,
    x="sepal_length",
    y="sepal_width",
    hue="cluster_predicted",
    palette="viridis",
    s=70,
)
# Plot the cluster centers (centroids) as large red 'X' marks
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    color="red",
    marker="X",
    s=200,
    label="Centroids",
)
# Add titles and labels
plt.title("K-Means Clustering on Iris Dataset")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend()

# Display the final presentation graph
plt.show()