import pandas as pd
import numpy as np
import re

# Load CSV (edit this path)
df = pd.read_csv('your_data.csv')
df.head()


# Basic shape and types
print("Shape:", df.shape)
print("\nColumn Types:")
print(df.dtypes)

# Preview rows
df.sample(5)


# Null summary
nulls = df.isnull().sum()
print("Null counts:")
print(nulls[nulls > 0])

# % null
print("\nNull % by column:")
print((df.isnull().mean() * 100).round(1))

# Duplicates
print(f"Duplicate rows: {df.duplicated().sum()}")


# Unique values per column
for col in df.columns:
    unique_vals = df[col].nunique()
    print(f"{col}: {unique_vals} unique values")


# Fill nulls (example)
def fill_nulls(df, strategy='mean', cols=None, value=None):
    if cols is None:
        cols = df.select_dtypes(include=[np.number]).columns
    for col in cols:
        if strategy == 'mean':
            df[col] = df[col].fillna(df[col].mean())
        elif strategy == 'median':
            df[col] = df[col].fillna(df[col].median())
        elif strategy == 'value' and value is not None:
            df[col] = df[col].fillna(value)
    return df


# Text cleaning
def clean_text_cols(df, cols):
    for col in cols:
        df[col] = df[col].astype(str).str.strip().str.lower()
        df[col] = df[col].apply(lambda x: re.sub(r'[\n\r]+', ' ', x))
    return df


# Quick way to rename columns
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.columns


df.to_csv("cleaned_data.csv", index=False)
print("Data exported as 'cleaned_data.csv'")


import pandas as pd
import re

schema_df = pd.read_csv('/Users/jwitch/Downloads/64b70e1b3aecc914857da23e.csv')
schema_df

# Select a specific column and show distinct values
column_to_show = "season"  
distinct_values = schema_df[column_to_show].unique()

# Display the distinct values
print(f"Distinct values in column '{column_to_show}':")
for value in distinct_values:
    print(value)

# Specify the column name you want to modify
column_names = ['copy_meta_data', 'content_tags_meta_data', 'social_post_content']

# Add double quotes around each value, and remove excess whitespace in the specified column
for column_name in column_names:
    schema_df[column_name] = schema_df[column_name].apply(lambda x: f'"{x}"' if pd.notnull(x) else x)
    schema_df[column_name] = schema_df[column_name].apply(lambda x: re.sub(r'\s+', '', x.replace('\n', '')) if pd.notnull(x) else x)

schema_df['copy_meta_data'][9:12]

schema_df.to_csv('organic_twitter_2.csv', index=False)
