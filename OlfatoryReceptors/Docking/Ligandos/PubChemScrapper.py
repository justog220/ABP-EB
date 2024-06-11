import requests
import csv
from tqdm import tqdm

def download_sdf(pubchem_id, filename="compound.sdf"):
    """Descarga la estructura en formato SDF 3D de un compuesto presente en PubChem

    Args:
        pubchem_id (int or string): Identificador de PubChem
        filename (str, optional): Nombre con el que se guarda el archivo. Defaults to "compound.sdf".
    """
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{pubchem_id}/record/SDF/?record_type=3d"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(filename, 'w') as file:
            file.write(response.text)
        # print(f"Estructura 3D descargada con éxito y guardada como {filename}")
    else:
        # print(f"Error al descargar la estructura: {response.status_code}")
        with open("fallidos.txt", "a") as fail:
            fail.write(f"PubChemID: {pubchem_id}\n\t{response.status_code}")
        pass


input_csv = "ligandos.csv"

# Obtener la cantidad total de filas en el archivo CSV
with open(input_csv, 'r') as csvfile:
    num_lines = sum(1 for line in csvfile)

with open(input_csv, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in tqdm(csvreader, total=num_lines, desc="Descargando Ligandos"):
        nombre = row['Nombre']
        codigo = row['Código']

        download_sdf(codigo, f"PubChem/{nombre.replace(" ", "").replace("(", "-").replace(")", "-")}.sdf")


print("Descargas completadas")
