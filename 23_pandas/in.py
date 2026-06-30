import pandas as pd

df = pd.read_json("output.json")
print('Displaying the info of data set')
print(df.info())