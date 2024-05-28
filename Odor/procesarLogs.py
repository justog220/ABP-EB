import re
import os
import csv

def obtener_mejor_pose(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        # Inicializar variables para la mejor pose
        mejor_affinity = None
        mejor_pose_data = None
        # Expresión regular para buscar líneas con datos de poses
        pose_pattern = re.compile(r'\s*(\d+)\s+(-?\d+\.\d+)\s+(-?\d+(?:\.\d+)?|\d+)\s+(-?\d+(?:\.\d+)?|\d+)')
        # Iterar sobre cada línea del archivo
        for line in lines:
            # Buscar líneas que contienen datos de poses
            match = pose_pattern.match(line)
            if match:
                # Obtener los datos de la pose
                mode, affinity, dist_lb, dist_ub = match.groups()
                affinity = float(affinity)
                # Si es la primera pose o tiene una afinidad más alta que la mejor hasta ahora
                if mejor_affinity is None or affinity < mejor_affinity:
                    # Actualizar los datos de la mejor pose
                    mejor_affinity = affinity
                    mejor_pose_data = mode, affinity, dist_lb, dist_ub
        return mejor_pose_data

# Archivo de log de AutoDock Vina
archivo_log = "Dockings/F1R141/-Citronellal.pdbqt.log"

receptores = []

ruta_resultados = "Dockings/"

for elemento in os.listdir(ruta_resultados):
    ruta_completa = os.path.join(ruta_resultados, elemento)

    # Verificar si es una carpeta
    if os.path.isdir(ruta_completa):
        receptores.append(elemento)


for receptor in receptores:
    logs = os.listdir(f"{ruta_resultados}{receptor}")

    summary = []

    for log in logs:
        mejor_pose = obtener_mejor_pose(f"{ruta_resultados}{receptor}/{log}")

        if mejor_pose:
            mode, affinity, dist_lb, dist_ub = mejor_pose
            # print(f"Mejor Pose - Mode: {mode}, Afinidad: {affinity}, Distancia LB: {dist_lb}, Distancia UB: {dist_ub}")
            if affinity > 0:
                print(affinity)
            summary.append((log.removesuffix(".pdbqt.log"), affinity))
        else:
            print("No se encontraron datos de la mejor pose en el archivo de log.")

    with open(f'Dockings/{receptor}/summary.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(['Ligando', 'Afinidad'])

        csvwriter.writerows(summary)


