import sqlite3
import pandas as pd
from tqdm import tqdm

conn = sqlite3.connect('../DB/unknome_db_03_Nov_2023.sqlite')

data_interes = ['accessions',
                'subcell_locs',
                'species',
                'pfam_ids',
                'knownness']

select = ''
for i in data_interes:
    select += i + ", "
select = select[:len(select)-2]


consulta  = f"SELECT {select} FROM Protein WHERE knownness is not null"

df = pd.read_sql_query(consulta, conn)

df.info()

df_pfam = df[["accessions", "pfam_ids", "knownness"]].copy()
df_pfam.dropna(inplace=True)
df_pfam['pfam_ids'] = df_pfam["pfam_ids"].str.split(";")

df_pfam

df_pfam["pfam_ids"] = df_pfam["pfam_ids"].str.join(";")
pfam_dummies = df_pfam["pfam_ids"].str.get_dummies(sep=";")

pfam_dummies.info()

for column in tqdm(pfam_dummies.columns, desc="Procesando columnas"):
    pfam_dummies[column] = pfam_dummies[column].astype(bool)

pfam_dummies.info()

df_pfam = pd.concat([df_pfam, pfam_dummies], axis=1)
del pfam_dummies
df_pfam.info()

df_pfam.drop(["pfam_ids", 'accessions'], axis=1, inplace=True)
df_pfam.head(1)

df_pfam.to_csv("df_pfam.csv", index=False)
