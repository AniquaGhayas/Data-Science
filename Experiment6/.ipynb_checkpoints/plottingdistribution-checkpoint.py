import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
iris = sns.load_dataset('iris')

# 2. Set the global aesthetic theme
sns.set_theme(style="darkgrid", palette="muted")


# I. HISTOGRAM
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Count of Samples')
sns.histplot(data=iris, x='sepal_length', color='teal', kde=True)
plt.show()


# II. DENSITY PLOT
plt.title('Density Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Probability Density')
sns.kdeplot(data=iris, x='sepal_width', fill=True, color='purple')
plt.show()


# III. BOX PLOT
plt.title('Analysis of Petal Length by Species')
plt.xlabel('Iris Species')
plt.ylabel('Petal Length (cm)')
sns.boxplot(data=iris, x='species', y='petal_length')
plt.show()


# IV. BAR PLOT
plt.title('Comparison of Mean Petal Width')
plt.xlabel('Iris Species')
plt.ylabel('Average Petal Width (cm)')
sns.barplot(data=iris, x='species', y='petal_width')
plt.show()