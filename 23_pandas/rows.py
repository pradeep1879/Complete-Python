import pandas as pd

df = pd.read_json("output.json")
print("Display first 10 rows")
print(df.head(2))


print("Display last 10 rows")
print(df.tail(1))