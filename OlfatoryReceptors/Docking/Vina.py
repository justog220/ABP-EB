import os
import sys
from tqdm import tqdm

def main():
    if len(sys.argv) < 2:
        print("Uso: python script.py <argumento>")
        return

    argument = sys.argv[1]
    ligfile = "Ligandos.txt"

    if not os.path.exists("out"):
        os.makedirs("out")
        
    if not os.path.exists(f"out/{argument}"):
    	os.makedirs(f"out/{argument}")

    try:
        with open(ligfile, 'r') as f:
            arr_file = f.readlines()
    except IOError:
        print("Cannot open file")
        return

    for i in tqdm(range(len(arr_file)), desc="Processing ligands"):
        arr_file[i] = arr_file[i].strip()
        print(arr_file[i])
        cmd = f"vina --config conf.txt --ligand Ligandos/PDBQT/{arr_file[i]} --out out/{argument}/{arr_file[i]}_out.pdbqt > Dockings/{argument}/{arr_file[i]}.log"
        os.system(cmd)

    print("Docking completado.")

if __name__ == "__main__":
    main()
