import pandas as pd

df = pd.read_csv("data.csv")
print("Average value:", df['value'].mean())
print("Max:", df['value'].max())
print("Min:", df['value'].min())