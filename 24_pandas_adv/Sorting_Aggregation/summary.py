import pandas as pd

data = {
    "Name":  ['Arun', 'Varun', 'Karun'],
    "Age": [10, 20, 8],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)
avg_salary = df['Salary'].mean()
print(avg_salary)