import pandas as pd
import time

df = pd.read_csv("df_pfam.csv")

porcentaje_muestra = 50

print("DataFrame previo al muestreo:\n")
df.info()
print("-"*10)

print(f"Procediendo a tomar una muestra aleatoria del {porcentaje_muestra}\% de los datos\n")
inicio = time.time()
df_muestreado = df.sample(frac=porcentaje_muestra/100)
del df 

print("DataFrame post muestreio:\n")
df_muestreado.info()

print("Inicio cálculo correlaciones")
correlation = df_muestreado.corr()
print("Fin cálculo de correlaciones")

correlation.to_csv("correlaciones.csv")



