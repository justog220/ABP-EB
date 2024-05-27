import re

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

# Obtener los datos de la mejor pose
mejor_pose = obtener_mejor_pose(archivo_log)

if mejor_pose:
    mode, affinity, dist_lb, dist_ub = mejor_pose
    print(f"Mejor Pose - Mode: {mode}, Afinidad: {affinity}, Distancia LB: {dist_lb}, Distancia UB: {dist_ub}")
else:
    print("No se encontraron datos de la mejor pose en el archivo de log.")
