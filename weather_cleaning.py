import pandas as pd
import numpy as np

# Load csv
df = pd.read_csv("weather.csv")

# Print csv's first rows
print("Original data: ")
print(df.head())

# Replace -9999 with np.nan
df.replace(-9999, np.nan, inplace=True)

# Check missing values in each column
print("Missing values after replacement: ")
print(df.isnull().sum())

# Delete rows whre UV is missing
df = df.dropna(subset=['UV'])

print("Missing values after dropping rows with missing UV: ")
print(df.isnull().sum())

# Fill missing temperatures with the average temp
avg_temp = df['Temperature'].mean()
df['Temperature'] = df['Temperature'].fillna(avg_temp)

# Fill missing humidity with last known value
df['Humidity'] = df['Humidity'].ffill()

# Print cleaned dataset
print("\nCleand Data: ")
print(df.head())




