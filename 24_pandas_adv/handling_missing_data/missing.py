import pandas as pd

data = {
    "Name":[None, 'Ayush', 'Shiv', 'Ankit', 'Sohan', 'Mohan', 'Ankita', 'Tanisha'],
    "Age":[None, 23, 21, 22, 23, 43, 21, 24,],
    "Salary":[None, 2300, 4300, 1200, 3400, 8900, 1400, 2500],
    "Performance Score":[None, 83, 92, 93, 87, 73, 75, 99]
}

df = pd.DataFrame(data)
print(df.isnull().sum())
print(df.isnull())

# drop rows with missing values
df.dropna(axis = 0, inplace=True)
print("Missing values dropped")
print(df)

# fillna(value, inplace=True)

df.fillna(0, inplace=True)
print(df)
df['Age'].fillna(df['Age'].mean(), inplace=True) 
df['Salary'].fillna(df['Salary'].mean(), inplace=True) 
print(df)