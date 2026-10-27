
# write a python program to generate synthetic data as a csv with 5 columns and 20 rows with a mixuture of stirngs and integers
# write a python program to read the csv file 
import pandas as pd 
import random
def generate_synthetic_data(file_path):
    # Define the number of rows and columns
    num_rows = 20
    num_columns = 5
    # Set a random seed for reproducibility (optional)
    random.seed(42)
    # Generate synthetic data
    data = {
        f'Column_{i+1}': [random.choice([random.randint(1, 100), f'String_{j+1}']) for j in range(num_rows)]
        for i in range(num_columns)
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    print(df.head())  # Print the first few rows of the DataFrame for verification
    
    # Save to CSV
    df.to_csv(file_path, index=False)
    print(f"Synthetic data generated and saved to {file_path}") 
    # Example usage
file_path = 'synthetic_data.csv'
generate_synthetic_data(file_path)
