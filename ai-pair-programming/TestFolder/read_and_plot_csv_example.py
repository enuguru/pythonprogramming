import pandas as pd
import matplotlib.pyplot as plt

# Read CSV (replace 'your_file.csv' with an actual file path)
df = pd.read_csv('your_file.csv')

# Plot a column
df['some_column'].plot(kind='hist')
plt.title("Histogram of some_column")
plt.show()
