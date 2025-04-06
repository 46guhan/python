#pandas

import pandas as pd
import numpy as np

data={
    'Name':['harish','rajesh','kathir',"jarvis"],
    'Age':[25,23,0,20],
    'Salary':[5000,6000,7000,7000],
    'Department':["HR","IT","TESTING","IT"]
}

data=pd.DataFrame(data)

#print(data.groupby("Department")["Salary"].mean())
# data.loc[2, 'Age'] = np.nan
# print(data)
# data["Age"].fillna(data["Age"].mean(),inplace=True)
# print(data)

#data.to_csv("output.csv",index=False)

""" datafile=pd.read_csv("output.csv")
print(datafile) """

print(data.sort_values(by="Salary",ascending=False))