import pandas as pd

# Load the dataset
df = pd.read_csv('data/drug200.csv')

# Display the first few rows
print(df.head())

# Check the columns
print(df.columns)

# Check the data types
print(df.info())

# Check for missing values
print(df.isnull().sum())