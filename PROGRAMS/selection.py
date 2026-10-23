import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Arun', 'Priya', 'Kumar', 'Divya'],
    'Age': [22, 28, 35, 24],
    'City': ['Chennai', 'Madurai', 'Coimbatore', 'Salem']
}

df = pd.DataFrame(data)

# Selecting a column
ages = df['Age']
print("Ages column:")
print(ages)

print("\n")

# Filtering rows
above_25 = df[df['Age'] > 25]
print("People with Age > 25:")
print(above_25)

print("\n")

# iloc (integer-based indexing)
row_0 = df.iloc[0]
print("First row using iloc (row index 0):")
print(row_0)

print("\n")

# loc (label-based indexing)
specific_val = df.loc[0, 'Name']
print("Name of the person at index 0:")
print(specific_val)