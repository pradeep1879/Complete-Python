import pandas as pd


data = {
    "Name":['Rohan', 'Ayush', 'Shiv', 'Ankit', 'Sohan', 'Mohan', 'Ankita', 'Tanisha'],
    "Age":[20, 23, 21, 22, 23, 43, 21, 24,],
    "Salary":[4000, 2300, 4300, 1200, 3400, 8900, 1400, 2500],
    "Performance Score":[75, 83, 92, 93, 87, 73, 75, 99]
}

df = pd.DataFrame(data)

#df.loc[row_index, "Column Name"] = new_value

df.loc[0, 'Salary'] = 4500
print(df)


## increasing salary by 5%
df['Salary'] = df['Salary'] * 1.05
print(df)

# removing 
# df.drop(column = ["ColumnName"], inplace = True)
print("Modified data")
df.drop(columns=['Performance Score'], inplace=True)
print(df)