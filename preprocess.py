import pandas as pd

df = pd.read_parquet("./datasets/irish_male.parquet")
print (df.head())
# print (df["audio"][1]["bytes"])