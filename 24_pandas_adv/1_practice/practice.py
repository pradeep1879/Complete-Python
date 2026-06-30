import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "D", "E"],
    "age": [23, 45, 32, 29, 40],
    "salary": [40000, 60000, 52000, 48000, 75000]
})

df[df["salary"] > 50000]