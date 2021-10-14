"""
CSci 39542:  Introduction to Data Science
Program 2: Senator's Name
Jiaming Zheng
jiaming.zheng745@myhunter.cuny.edu
Resources: https://www.geeksforgeeks.org/how-to-select-multiple-columns-in-a-pandas-dataframe/
"""
import pandas as pd

input_File = input("Enter input file name: ")
output_File = input("Enter output file name: ")
legis = pd.read_csv(input_File)
data = []
for index, row in legis.iterrows():
    if pd.notnull(row['senate_class']):
        data.append([row['first_name'], row['last_name']])
df = pd.DataFrame(data, columns = ['first_name','last_name'])
df.to_csv(output_File, index = False)