import os
from subprocess import call

# Directorios de entrada y salida (rutas absolutas)
ligandos_dir = os.path.abspath("ligandos/")
output_dir = os.path.abspath("resultados/")
os.makedirs(output_dir, exist_ok=True)

# Lista de archivos de ligandos en formato SDF
ligandos = [f for f in os.listdir(ligandos_dir) if f.endswith('.sdf')]

for ligando in ligandos:
    ligando_base = os.path.splitext(ligando)[0]
    ligando_sdf = os.path.join(ligandos_dir, ligando)
    ligando_pdb = os.path.join(ligandos_dir, f"{ligando_base}.pdb")
    ligando_pdbqt = os.path.join(output_dir, f"{ligando_base}.pdbqt")

    # Verificar que el archivo SDF exista
    if not os.path.exists(ligando_sdf):
        print(f"El archivo {ligando_sdf} no existe")
        continue

    # Convertir a PDB usando Open Babel
    print(f"Convirtiendo {ligando_sdf} a {ligando_pdb} usando Open Babel...")
    conversion_result = call(["obabel", ligando_sdf, "-O", ligando_pdb, "--gen3d"])
    if conversion_result != 0:
        print(f"Error en la conversión de {ligando_sdf} a PDB con Open Babel")
        continue

    # Verificar que el archivo PDB se haya creado
    if not os.path.exists(ligando_pdb):
        print(f"No se pudo generar el archivo PDB para {ligando_sdf}")
        continue

    # Convertir a PDBQT usando prepare_ligand4.py de AutoDockTools con rutas absolutas
    print(f"Convirtiendo {ligando_pdb} a {ligando_pdbqt} usando prepare_ligand4.py...")
    prepare_ligand_script = os.path.abspath("/home/justo/MGLTools-1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py")
    conversion_result = call([
        prepare_ligand_script,
        "-l", ligando_pdb,
        "-o", ligando_pdbqt,
        "-A", "hydrogens"
    ])
    if conversion_result != 0:
        print(f"Error en la conversión de {ligando_pdb} a PDBQT con prepare_ligand4.py")
        continue

    # Verificar que el archivo PDBQT se haya creado
    if not os.path.exists(ligando_pdbqt):
        print(f"No se pudo generar el archivo PDBQT para {ligando_pdb}")
        continue

    print(f"Archivo PDBQT generado: {ligando_pdbqt}")

