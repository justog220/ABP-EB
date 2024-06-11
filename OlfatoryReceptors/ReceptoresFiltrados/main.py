import pandas as pd
import sqlite3
import requests

conn = sqlite3.connect('../../DB/unknome_db_03_Nov_2023.sqlite')
# conn = sqlite3.connect('../../')

final_5 = ["tr|Q7TR84|Q7TR84_MOUSE",
           "tr|Q7TR55|Q7TR55_MOUSE", 
           "tr|Q2PRI9|Q2PRI9_DANRE", 
           "tr|A0A8V0XJH9|A0A8V0XJH9_CHICK", 
           "tr|F1R141|F1R141_DANRE"]


final_5 = [f'%{valor}%' for valor in final_5]

consulta = "SELECT * FROM Protein WHERE fasta_header LIKE ?"

dfs = []
for valor in final_5:
    dfs.append(pd.read_sql_query(consulta, conn, params=[valor]))

df = pd.concat(dfs)

df.to_csv("cinco_finales_subset.csv")


def get_protein_PDB(uniprot_accession):
    """Obtiene una estructura PDB a partir de la API de AlphaFold

    Args:
        uniprot_accession (string or int): Identificador de UniProt de la proteína

    Returns:
        string: Data del PDB
    """
    api_endpoint = "https://alphafold.ebi.ac.uk/api/prediction/"
    url = f"{api_endpoint}{uniprot_accession}"  # Construct the URL for API

    try:
        # Use a timeout to handle potential connection issues
        response = requests.get(url, timeout=10)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            result = response.json()
            pdb_url = result[0].get('pdbUrl')
            pdb_data = requests.get(pdb_url).text
            return pdb_data
        else:
            # Raise an exception for better error handling
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

uniprots_id = df["accessions"]

for uid in uniprots_id:
    uid = uid.split(sep=";")[0]

    pdb_data = get_protein_PDB(uid)

    if pdb_data:
        with open(f"Estructuras/{uid}.pdb", "w") as archi:
            archi.write(pdb_data)




        