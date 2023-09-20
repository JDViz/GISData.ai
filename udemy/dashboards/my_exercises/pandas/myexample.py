import numpy as np
import pandas as pd

# df stands for DataFrame
df = pd.read_csv('./data/salaries.csv')
# print('------------')
# print(f"Full CSV Data:\n{df}")
# print('------------')
# print(f"Salary Column:\n{df['Salary']}")
# print('------------')
# print(f"Selecting specific columns:\n{df[['Name','Salary']]}")
# print('------------')
# print(f"Min Salary: {df['Salary'].min()}")
# print('------------')
# print(f"Max Salary: {df['Salary'].max()}")
# print('------------')
# print(f"Mean Salary: {df['Salary'].mean()}")
# print('------------')
# true_cols = df['Age'] > 30
# print(f"Boolean response age above 30:\n{true_cols}")
# print(f"Rows where true:\n{df[true_cols]}")
# print('------------')
# print(f"Rows where Age less that 40:\n{df[df['Age'] < 40]}")
# print('------------')
# print(f"Unique values:\n{df['Age'].unique()}")
# print('------------')
# print(f"Number of Unique Age values")
# print(df['Age'].nunique())
# print('------------')
# print(f"Number of Unique Salary values")
# print(f"{df['Salary'].nunique()} :: {df['Salary'].unique()}")
# print('------------')
# print(f"Column Names")
# print(df.columns)
# print('------------')
# print(f"Dataframe Info")
# print(df.info())
# print('------------')
# print(f"Describe")
# print(df.describe())
# print('------------')
# print(f"Index")
# print(df.index)
# print('------------')

print('------------')

arng = np.arange(0, 50)
mat = np.arange(0, 10).reshape(5, 2)

print(arng)
print(mat)

print('------------')

df2 = pd.DataFrame(data=mat)
print(df2)

print('------------')

df3 = pd.DataFrame(data=mat, columns=['Col A', 'Col B'])
print(df3)

print('------------')

df4 = pd.DataFrame(data=mat, columns=['Col A', 'Col B'], index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'])
print(df4)

print('------------')
