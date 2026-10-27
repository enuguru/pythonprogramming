import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import requests
from io import StringIO

# Load dataset from URL
dataset_url = "https://gist.githubusercontent.com/pravalliyaram/5c05f43d2351249927b8a3f3cc3e5ecf/raw/8bd6144a87988213693754baaa13fb204933282d/Mall_Customers.csv"
response = requests.get(dataset_url)
data = pd.read_csv(StringIO(response.text))

# Select features for clustering
features = data[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

# Elbow method to find optimal clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.savefig('elbow_plot.png')
plt.close()

# Fit KMeans with optimal clusters (let's use 5 as commonly found for this dataset)
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(features)

# Save clustered data for further analysis
data.to_csv('Mall_Customers_Clustered.csv', index=False)

print("KMeans clustering complete. Elbow plot saved as elbow_plot.png. Clustered data saved as Mall_Customers_Clustered.csv.")
