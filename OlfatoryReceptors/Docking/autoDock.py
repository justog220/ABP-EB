import subprocess
import os

receptores = [
    "F1R141",
    "Q2PRI9",
    "Q7TR55",
    "Q7TR84"
]

if not os.path.exists("Dockings"):
    os.makedirs("Dockings")

subprocess.run(["ls Ligandos/PDBQT/ > Ligandos.txt"], shell=True)

for receptor in receptores:
    if not os.path.exists(f"Dockings/{receptor}"):
        os.makedirs(f"Dockings/{receptor}")

    subprocess.run([f"cp configs/{receptor}.txt conf.txt"], shell=True)
    subprocess.run([f"cp Receptor/{receptor}.pdbqt receptor.pdbqt"], shell=True)

    # subprocess.run([f"perl Vina.pl {receptor}"] , shell=True)
    subprocess.run([f"python3 Vina.py {receptor}"], shell=True)