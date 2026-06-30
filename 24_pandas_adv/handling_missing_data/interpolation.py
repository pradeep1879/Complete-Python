import pandas as pd

data = {
    "Name":[None, 'Ayush', 'Shiv', 'Ankit', 'Sohan', 'Mohan', 'Ankita', 'Tanisha'],
    "Age":[None, 23, 21, 22, 23, 43, 21, 24,],
    "Salary":[None, 2300, 4300, 1200, 3400, 8900, 1400, 2500],
    "Performance Score":[None, 83, 92, 93, 87, 73, 75, 99]
}

df = pd.DataFrame(data)
print(df)
# linear, polynomial, time
df.interpolate(method="linear", axis=0, inplace=True)
