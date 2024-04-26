import sqlite3
import pandas as pd

conn = sqlite3.connect('../../DB/unknome_db_03_Nov_2023.sqlite')

consulta  = "SELECT * FROM Protein WHERE pfam_ids LIKE '%PF13853%' AND knownness is not null"

df = pd.read_sql_query(consulta, conn)

print("Olfatorys receptor DataFrame")
print(df.info())

df.to_csv('OlfatorysReceptor.csv')