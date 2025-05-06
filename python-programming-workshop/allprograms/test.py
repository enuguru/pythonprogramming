import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

# Load the dataset from the internet
url = "https://raw.githubusercontent.com/selva86/datasets/master/Salary_Data.csv"
data = pd.read_csv(url)

# Extract features (YearsExperience) and target (Salary)
X = data[['YearsExperience']].values
y = data['Salary'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict salaries for the test set
y_pred = model.predict(X_test)

# Calculate and print the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Visualize the regression line
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience')
plt.legend()
plt.show()

# Predict the salary for 7 years of experience
years_of_experience = 7
predicted_salary = model.predict([[years_of_experience]])
print(f"Predicted Salary for {years_of_experience} years of experience: {predicted_salary[0]:.2f}")