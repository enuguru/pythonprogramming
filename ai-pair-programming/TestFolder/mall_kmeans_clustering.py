import pandas as pd
"""
mall_kmeans_clustering.py
This script performs customer segmentation using K-Means clustering on the Mall Customers dataset.
It includes functions to load data, visualize the optimal number of clusters (Elbow Method), plot clusters,
and visualize relationships between customer features.
Functions:
----------
load_data(file_path='Mall_Customers.csv'):
    Loads the Mall Customers dataset from a CSV file.
plot_elbow(X):
    Plots the Elbow Method graph to help determine the optimal number of clusters for K-Means.
plot_clusters(df, X, y_kmeans):
    Visualizes the clusters formed by K-Means along with their centroids.
plot_income_vs_spending(df):
    Plots a scatter plot of Annual Income vs Spending Score for all customers.
plot_age_vs_spending(df):
    Plots a scatter plot of Age vs Spending Score for all customers.
main():
    Main function to execute the clustering workflow:
    - Loads data
    - Scales features
    - Plots elbow curve
    - Fits K-Means and plots clusters
    - Plots additional feature relationships
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset (Mall Customers)
# You can download the dataset from: https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial
# For this example, we assume the file is named 'Mall_Customers.csv' and is in the same directory.

def load_data(file_path='Mall_Customers.csv'):
    df = pd.read_csv(file_path)
    return df

def plot_elbow(X):
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    plt.figure(figsize=(8,5))
    plt.plot(range(1, 11), wcss, marker='o')
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

def plot_clusters(df, X, y_kmeans):
    plt.figure(figsize=(8,5))
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=100, c='cyan', label='Cluster 4')
    plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=100, c='magenta', label='Cluster 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()

def plot_income_vs_spending(df):
    plt.figure(figsize=(8,5))
    plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c='purple')
    plt.title('Income vs Spending Score')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.show()

def plot_age_vs_spending(df):
    plt.figure(figsize=(8,5))
    plt.scatter(df['Age'], df['Spending Score (1-100)'], c='orange')
    plt.title('Age vs Spending Score')
    plt.xlabel('Age')
    plt.ylabel('Spending Score (1-100)')
    plt.show()

def main():
    df = load_data()
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    plot_elbow(X_scaled)
    # Choose optimal clusters (e.g., 5)
    global kmeans
    kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
    y_kmeans = kmeans.fit_predict(X_scaled)
    plot_clusters(df, X_scaled, y_kmeans)
    plot_income_vs_spending(df)
    plot_age_vs_spending(df)

if __name__ == "__main__":
    main()
