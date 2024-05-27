import os
import subprocess


def convertir_sdfs_a_pdbqt(directorio_sdfs, directorio_pdbqts):
    # Verificar si el directorio de salida existe, si no, crearlo
    if not os.path.exists(directorio_pdbqts):
        os.makedirs(directorio_pdbqts)

    # Obtener la lista de archivos SDF en el directorio de entrada
    archivos_sdf = [archivo for archivo in os.listdir(directorio_sdfs) if archivo.endswith(".sdf")]

    # Recorrer cada archivo SDF y convertirlo a PDBQT
    for archivo_sdf in archivos_sdf:
        nombre_base = os.path.splitext(archivo_sdf)[0]
        archivo_entrada = os.path.abspath(os.path.join(directorio_sdfs, archivo_sdf))
        archivo_salida = os.path.abspath(os.path.join(directorio_pdbqts, nombre_base + ".pdbqt"))
        
        # Ejecutar el comando de conversión usando subprocess
        call = f"obabel {archivo_entrada} -O {archivo_salida} -xh"
        subprocess.run([call], check=True, shell=True)

# Directorios de entrada y salida
directorio_sdfs = "PubChem/"
directorio_pdbqts = "PDBQT/"

# Llamar a la función para realizar la conversión
convertir_sdfs_a_pdbqt(directorio_sdfs, directorio_pdbqts)
