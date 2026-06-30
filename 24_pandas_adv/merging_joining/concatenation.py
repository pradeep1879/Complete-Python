# vertically (row-wise)
# horizontally (column-wise)
# pd.concate(df1, df2, axis=0, ignore_index=True)

import pandas as pd

df_Region1 = pd.DataFrame({
    'CustomersID': [1, 2],
    'Name': ['Gopal', 'Raju']
})

df_Region2 = pd.DataFrame({
    'CustomersID': [3, 4], 
    'Name': ['Shayam', 'Baburao']
})

# concatenate vertically
df_concate = pd.concat([df_Region1, df_Region2], axis=1,  ignore_index=True)
print(df_concate)

#Ques. 