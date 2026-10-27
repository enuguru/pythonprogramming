import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [85, 62, 90, 70]
}
df = pd.DataFrame(data)

# Basic statistics
print("Mean age:", df['Age'].mean())
print("Max score:", df['Score'].max())

# Filter rows
print("People with score > 80:")
print(df[df['Score'] > 80])
