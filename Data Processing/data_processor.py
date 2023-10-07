import pandas as pd
path = 'Data Submissions (Responses).xlsx'
df = pd.read_excel('Data Submissions (Responses).xlsx')
col = 66
array = [[0]]
while col < 91:
    titles = pd.read_excel(path, usecols = chr(col)).to_numpy()
    i = 0
    while i < len(titles):
        array[col-66][i] = titles[i][0]
        i += 1
    col += 1

for x in array:
    for a in x:
        print(a)
