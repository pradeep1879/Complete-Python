import pandas as pd

data = {
    "Name":['Rohan', 'Aayush', 'Shiv', 'Ankit', 'Sohan', 'Mohan', 'Ankita', 'Tanisha'],
    "Age":[20, 23, 21, 22, 23, 43, 21, 24,],
    "Salary":[4000, 2300, 4300, 1200, 3400, 8900, 1400, 2500],
    "Performance Score":[75, 83, 92, 93, 87, 73, 75, 99]
}


df = pd.DataFrame(data)
print('sample dataframe')
print(df)
print('Descriptive Statistics')
print(df.describe())

df = pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Cloumn Names: {df.columns}')

# select specific column(a series, dataframe multiple columns of data), filter rows(boolean indexing),
#  combine multiple conditions()

df = pd.DataFrame(data)
print("Sample dataframe")
print("Names (Single column return series)")
name = df['Name']
print(name)

# selecting multiple columns
subset = df[['Name', 'Salary']]
print('\n Subset with name and salary')
print(subset)


df = pd.DataFrame(data)
high_salary = df[df['Salary'] > 2000]
print('Employes with salary more than 2000 \n')
print(high_salary)

filtered = df[(df['Age'] > 23) & (df['Salary'] > 2000)]
print('Employes with age greater than 23 and salary greater than 2000')
print(filtered)

filtered = df[(df['Age'] > 23) | (df['Performance Score'] > 80)]
print('Employes with age greater than 23 OR salary greater than 2000')
print(filtered)