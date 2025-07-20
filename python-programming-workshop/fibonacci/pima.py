import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Read training data
train_df = pd.read_csv('pima_indians_diabetes_data_train.csv', header=None)
X_train = train_df.iloc[:, :-1].values  # First 8 columns: features
y_train = train_df.iloc[:, -1].values   # Last column: target

# Optional: Split training data for validation (not required for final prediction)
# X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Select KNN algorithm and train model
k = 5  # You can tune this value
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Read test data
test_df = pd.read_csv('pima_indians_diabetes_data_test.csv', header=None)
X_test = test_df.values  # All columns are features

# Predict using the trained model
y_pred = knn.predict(X_test)

# Print the predictions for the test data
print("Predicted target values for the test data:")
print(y_pred)

# Optional: Visualize the distribution of predictions
plt.hist(y_pred, bins=np.arange(y_pred.min(), y_pred.max()+2)-0.5, rwidth=0.8)
plt.xlabel('Predicted Class')
plt.ylabel('Count')
plt.title('Distribution of Predicted Classes')
plt.show()