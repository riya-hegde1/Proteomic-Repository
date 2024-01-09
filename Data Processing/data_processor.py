import pandas as pd
import os 


path = 'Data Processing/Data Submissions (Responses).xlsx'
df = pd.read_excel(path, header=None)
df.to_markdown("complete-data.md")

other_path = os.path.realpath('README.md')
with open(other_path, 'r') as f:
    text = f.readlines()

exists = False
with open(other_path, 'a') as f:
    for row in range(1, len(df.index)):
        exists = False
        for x in text:
            if x == ("* [" + str(df.loc[row,1]) + "](" + str(df.loc[row,20]) + ")") or x == ("* [" + str(df.loc[row,1]) + "](" + str(df.loc[row, 24]) + ")"):
                exists = True
        if exists == False:
            peptide = False
            f.write("\n\n#### ")
            if df.loc[row,14] == "Phosphorylation":
                f.write("Phosphorylation Data ") 
            else:
                f.write("Expression Data ")
            if str(df.loc[row,19]).lower() == "y" or str(df.loc[row,19]).lower() == "yes":
                f.write("(Peptide-level)\n* [" + df.loc[row,1] + "](" + df.loc[row,20] + ")\n\t* ")
                if len(str(df.loc[row,4])) < 1:
                    f.write("No PRIDE ID, ")
                else:
                    f.write(str(df.loc[row,4]) + ", ")
                f.write(str(df.loc[row,5]) + ", " + str(df.loc[row,7]) + ", " + str(df.loc[row,21]))
                peptide = True
            if df.loc[row,22].lower() == "y" or df.loc[row,22].lower() == "yes":
                if peptide == True:
                    f.write("\n\n#### ")
                    if df.loc[row,14] == "Phosphorylation":
                        f.write("Phosphorylation Data ") 
                    else:
                        f.write("Expression Data ")
                f.write("(Protein-level)\n* [" + df.loc[row,1] + "](" + df.loc[row,24] + ")\n\t* ")
                if len(str(df.loc[row,3])) < 4:
                    f.write("No PRIDE ID, ")
                else:
                    f.write(str(df.loc[row,4]) + ", ")
                f.write(str(df.loc[row,5]) + ", " + str(df.loc[row,7]) + ", " + str(df.loc[row,23]))
