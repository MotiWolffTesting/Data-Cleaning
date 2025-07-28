import pandas as pd
import numpy as np

# Load csv
df = pd.read_csv('customer_purchases.csv')

# Look for missing values
print("Initial missing data per column: ")
print(df.isnull().sum())

# Fill age and purchaseAmount by region and gender
for col in ['Age', 'PurchaseAmount']:
    df[col] = df.groupby(['Region', 'Gender'])[col].transform(
        lambda x: x.fillna(x.median())
    )
    
# For categorical columns, fill with mode
if 'ProductCategory' in df.columns:
    df['ProductCategory'] = df.groupby(['Region', 'Gender'])['ProductCategory'].transform(
        lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "Unknown")
    )
    
# Fill any remaining missing values with overall median/mode
for col in df.columns:
    if df[col].dtype in [np.float64, np.int64]:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])
        
# Ensure no missing values remain
print("Missing values after cleaning:")
print(df.isnull().sum())

# Another print check
print(df.head())

# Save cleaned DataFrame
df.to_csv('customer_purchases_cleaned.csv', index=False)
print("\nCleaned data saved to customer_purchases_cleaned.csv")