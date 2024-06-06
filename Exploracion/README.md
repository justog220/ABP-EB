# Exploración

## Metodología

### 1. Exploración de la Base de Datos
Se comenzó explorando la base de datos utilizando tanto Pandas como SQL. Se realizaron consultas SQL para obtener una visión general de los diferentes atributos presentes en la base de datos y para realizar recuentos de parámetros relevantes, como el grado de conocimiento y las especies presentes.

Este análisis se puede ver en el archivo [exploracion.ipynb](https://github.com/justog220/ABP-EB/blob/main/Exploracion/exploracion.ipynb).

### 2. Análisis de PFAM
Se realizó un análisis específico de los identificadores PFAM presentes en la base de datos. Para esto, se implementaron funciones para realizar scraping en la base de datos de InterPro con el fin de obtener los nombres cotidianos asociados a los identificadores PFAM. Posteriormente, se exploró la distribución de familias de proteínas en la base de datos utilizando esta información.

![Distribución de PFAMs](../imgs/pfam.png)

Como se puede observar en la imágen anterior, la segunda familia más presente es la de los receptores olfatorios. Este dato llamó nuestra atención por los procesos en los que están involucrados, potenciales aplicaciones con ellos y porque era un número suficientemente elevado como para llevar a cabo distintos análisis.