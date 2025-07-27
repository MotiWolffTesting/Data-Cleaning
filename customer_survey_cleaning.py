import pandas as pd
import numpy as np

# Load csv
df = pd.read_csv('customer_survey.csv')

# Go through the data
print("Inital data info: ")
print(df.info())
print("Missing values per column: ")
print(df.isnull().sum())

# Replace "?", "Unknown", "-1" with np.nan
df.replace(['?', 'Unknown', -1], np.nan, inplace=True)

print("Missing values after replacement: ")
print(df.isnull().sum())

# Delete columns where over 40% of data is missing
thresh = len(df) * 0.4
df = df.loc[:, df.isnull().sum() <= thresh]

print("After getting rid of that: ")
print(df.isnull().sum())

# Drop rows missing both Age and SatisfactionScore
df = df.dropna(subset=['Age', 'SatisfactionScore'], how='all')

print("After dropping rows missing both Age and SatisfactionScore:")
print(df.isnull().sum())

# Fill missing gender with "Other"
df['Gender'] = df['Gender'].fillna('Other')

# Fill missing age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing SatisfactionScore with mode
df['SatisfactionScore'] = df['SatisfactionScore'].fillna(df['SatisfactionScore'].mode()[0])

print("Final missing values per column:")
print(df.isnull().sum())

# Save cleaned DataFrame
df.to_csv('customer_survey_cleaned.csv', index=False)
print("\nCleaned data saved to customer_survey_cleaned.csv")