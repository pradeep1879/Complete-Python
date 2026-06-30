import pandas as pd
data = {
    "Name": ['Rahul', 'Sohan', 'Mohan', 'Rohit'],
    "Age": [12, 23, 43, 23],
    "City": ['Jaipur', 'Delhi', 'Mumbai', 'Jhunjhunu']  
}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)
