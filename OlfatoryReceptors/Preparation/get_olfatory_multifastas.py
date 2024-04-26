import pandas as pd

df = pd.read_csv("OlfatorysReceptor.csv")



with open("olfatorys_receptor.multifasta", "w") as multifasta:
    for _, row in df.iterrows():
        multifasta.write(">"+row["fasta_header"]+"\n")
        multifasta.write(row["sequence"]+"\n")
