import pandas as pd


data = {
    "Name":['Rohan', 'Ayush', 'Shiv', 'Ankit', 'Sohan', 'Mohan', 'Ankita', 'Tanisha'],
    "Age":[20, 23, 21, 22, 23, 43, 21, 24,],
    "Salary":[4000, 2300, 4300, 1200, 3400, 8900, 1400, 2500],
    "Performance Score":[75, 83, 92, 93, 87, 73, 75, 99]
}

df = pd.DataFrame(data)
# print(df)
df['Bonus'] = df['Salary'] * 0.1
print(df)

# using insert method
# df.insert(loc, 'column_name', some_data)

df.insert(0, "Employee_id", [10, 20, 30, 40, 50, 60, 70, 80])
print(df)