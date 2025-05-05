import pandas as pd
import numpy as np

# Create DataFrame
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# 1. Rename column names using function
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# 2. Print the first 3 rows of the DataFrame
print("First 3 rows:")
print(df.head(3))

# 3. Find the mean age of the individuals
mean_age = df['age'].mean()
print(f"\nMean Age: {mean_age}")

# 4. Select and print only the 'first_name' and 'City' columns
print("\nSelected 'first_name' and 'City' columns:")
print(df[['first_name', 'City']])

# 5. Add a new column 'Salary' with random salary values
df['Salary'] = np.random.randint(40000, 100000, size=len(df))
print("\nDataFrame with new 'Salary' column:")
print(df)

# 6. Display summary statistics of the DataFrame
print("\nSummary statistics:")
print(df.describe())

