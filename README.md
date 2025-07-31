# 🧹 Data Cleaning & EDA Tools

This repository contains reusable tools for quick and effective exploratory data analysis (EDA) and data cleaning, built with Python and Pandas. Ideal for analysts, data scientists, or anyone who works with messy tabular data regularly.

---

## 📂 Structure

- `notebooks/`: Interactive `.ipynb` version with full markdown explanations
- `scripts/`: `.py` script version of the cleaning functions for reuse in projects

---

## 🛠 Features

- Load and preview tabular data
- Summarize data shape, types, and nulls
- Count unique values and detect cardinality issues
- Fill or drop missing values using strategies (`mean`, `median`, `value`)
- Clean and standardize text columns
- Rename and normalize column names
- Export cleaned datasets

---

## 🧪 Usage

### In Notebook:
```python
# Load and explore
df = pd.read_csv('your_file.csv')
df.shape
df.isnull().sum()

# Clean text
df = clean_text_cols(df, ['description', 'notes'])

# Fill missing values
df = fill_nulls(df, strategy='mean')
```

### As Script:
Import the `.py` module and reuse functions.

```python
from scripts.data_cleaning_tools import fill_nulls, clean_text_cols
```

---

## 📦 Requirements

- pandas
- numpy
- re (standard lib)

---

## 👤 Author

James Witcher  
[LinkedIn](https://www.linkedin.com/in/james-witcher/)  
