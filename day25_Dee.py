import pandas as pd

df = pd.read_csv("data/hacker_news.csv")

print("First five rows:")
print(df.head())

print("\nLast five rows:")
print(df.tail())

titles = df["title"]
print("\nTitle column:")
print(titles)

rows, columns = df.shape
print(f"\nRows: {rows}")
print(f"Columns: {columns}")

title_text = titles.fillna("").astype(str)
python_titles = df[title_text.str.contains("python", case=False, na=False)]
javascript_titles = df[title_text.str.contains("javascript", case=False, na=False)]

print("\nTitles containing Python:")
print(python_titles["title"])

print("\nTitles containing JavaScript:")
print(javascript_titles["title"])

print("\nData exploration:")
print("Column names:", list(df.columns))
print("Data types:\n", df.dtypes)
print("Missing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Python title matches:", len(python_titles))
print("JavaScript title matches:", len(javascript_titles))
