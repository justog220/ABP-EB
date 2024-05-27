import re
import csv

# Leer datos del archivo de texto
with open('tablaPaper.txt', 'r') as file:
    data = file.read()

# Expresión regular para capturar el nombre y el código numérico
pattern = re.compile(r'(.+?)(\d+)$')

# Lista para almacenar los resultados
results = []
codes = []
current_type = "ALCOHOL"  # Valor predeterminado

# Iterar sobre cada línea de datos
for line in data.split('\n'):
    if line.strip():  # Evitar líneas vacías
        match = pattern.match(line)
        if match:
            name = match.group(1).strip()
            code = match.group(2)
            codes.append(code)
            results.append((name, code, current_type))
        else:
            # Si la línea no tiene un código, actualizamos el tipo
            current_type = line.strip()

# Escribir los resultados en un archivo CSV
with open('ligandos.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Escribir el encabezado
    csvwriter.writerow(['Nombre', 'Código', 'Tipo'])
    # Escribir los datos
    csvwriter.writerows(results)


print("Datos guardados en 'ligandos.csv'")
