import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score

# Load clustered data
data = pd.read_csv('Mall_Customers_Clustered.csv')
features = data[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]
labels = data['Cluster']

# Calculate silhouette score
score = silhouette_score(features, labels)
print(f"Silhouette Score for KMeans clusters: {score:.3f}")

# Scatter plot: Age vs Annual Income, colored by Gender
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Annual Income (k$)', hue='Gender', data=data, palette='Set1')
plt.title('Age vs Annual Income by Gender')
plt.savefig('age_vs_annual_income_gender.png')
plt.close()

print("Scatter plot saved as age_vs_annual_income_gender.png. Silhouette score printed above.")
