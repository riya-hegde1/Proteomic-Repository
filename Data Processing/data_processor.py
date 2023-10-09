import pandas as pd
path = 'Data Processing/Data Submissions (Responses).xlsx'
df = pd.read_excel(path, header=None)
df.to_markdown("complete-data.md")