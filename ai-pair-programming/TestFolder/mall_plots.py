import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load clustered data
data = pd.read_csv('Mall_Customers_Clustered.csv')

# Age vs Spending Score
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Spending Score (1-100)', hue='Cluster', data=data, palette='Set1')
plt.title('Age vs Spending Score by Cluster')
plt.savefig('age_vs_spending_score.png')
plt.close()
# Conclusion: This plot shows how spending habits vary with age across clusters.

# Age vs Annual Income
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Annual Income (k$)', hue='Cluster', data=data, palette='Set2')
plt.title('Age vs Annual Income by Cluster')
plt.savefig('age_vs_annual_income.png')
plt.close()
# Conclusion: Reveals income distribution among age groups and clusters.

# Annual Income vs Spending Score
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=data, palette='Set3')
plt.title('Annual Income vs Spending Score by Cluster')
plt.savefig('income_vs_spending_score.png')
plt.close()
# Conclusion: Shows how income relates to spending score for each cluster.

# Gender vs Annual Income
plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='Annual Income (k$)', data=data)
plt.title('Gender vs Annual Income')
plt.savefig('gender_vs_annual_income.png')
plt.close()
# Conclusion: Compares income distribution between genders.

# Gender vs Spending Score
plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='Spending Score (1-100)', data=data)
plt.title('Gender vs Spending Score')
plt.savefig('gender_vs_spending_score.png')
plt.close()
# Conclusion: Compares spending score distribution between genders.

print("All plots saved. See PNG files for visualizations and insights.")
