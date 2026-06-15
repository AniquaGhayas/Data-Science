import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")

# A. X–Y GRAPH (Line Plot)

iris_sorted = iris.sort_values(by="sepal_length")
sns.lineplot(data=iris_sorted, x="sepal_length", y="sepal_width")
plt.title("A. X-Y Line Graph: Sepal Length vs Width Trend")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()  

# B. SCATTER PLOT
sns.scatterplot(data=iris, x="petal_length", y="petal_width", hue="species")
plt.title("B. Scatter Plot: Petal Length vs Width Clustered by Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.show()  

# C. BAR CHART
sns.barplot(data=iris, x="species", y="petal_length")
plt.title("C. Bar Chart: Average Petal Length for Each Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show() 

# D. PIE CHART

counts = iris["species"].value_counts()
plt.pie(counts, labels=counts.index, autopct="%1.1f%%")
plt.title("D. Pie Chart: Proportional Breakdown of Species")
plt.show()  