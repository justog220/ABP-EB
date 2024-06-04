# Docking

## Descripción
Habiendo seleccionado cuatro receptores olfatorios presentes en el Unknome, a través del enfoque de reducción de dimensionalidad del árbol filogenético obtenido del alineamiento de ellos, realizamos un estudio de docking con diversos ligandos para investigar sus potenciales interacciones.

## Metodología
### 1. Selección de Receptores Olfatorios
La meotodología para la selección de los receptores olfatorios se desarrolla en [el README de la carpeta del nivel superior](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors).

### 2. Selección y Preparación de Ligandos
Tomamos como referencia los ligandos y la clasificación listada en el artículo:

Computational Approaches for Decoding Select Odorant-Olfactory Receptor Interactions Using Mini-Virtual Screening Harini K, Sowdhamini R (2015) Computational Approaches for Decoding Select Odorant-Olfactory Receptor Interactions Using Mini-Virtual Screening. PLOS ONE 10(7): e0131077. https://doi.org/10.1371/journal.pone.0131077

En la carpeta *Ligandos/* desarrollamos tres scripts:
- *preparacionCsv.py:* para convertir la información del artículo a un archivo .csv que permita su posterior manipulación con mayor facilidad.
- *PubChemScraper.py:* sript que declara funciones para bajar una estructura de la API de [PubChem](https://pubchem.ncbi.nlm.nih.gov/) en formato SDF 3D. Luego recorre el csv generado en el script anterior y guarda todas las estructuras en *PubChem/*
- *sdfToPDBQT.py:* Script que implementa la utilización programáticamente de la herramienta [OpenBabel](https://openbabel.org/index.html) para convertir las estructuras de los ligandos de formato SDF 3D a PDBQT y agregarle los hidrógenos polares necesarios.

La ejecución de estos scripts da como resultado la generación de dos carpetas:
- *PubChem/:* Estructuras en formato SDF descargadas de PubChem.
- *PDBQT/:* Estructuras en formato PDBQT generadas por OpenBabel.

### 3. Preparación de Receptores
Los 4 receptores seleccionados fueron preparados para el docking. Esto incluyó la adición de hidrógenos, reconstrucción de átomos faltantes, la asignación de cargas parciales y la generación de archivos PDBQT adecuados para el docking. Para ello se hizo uso de la herramienta [AutoDockTools](https://autodocksuite.scripps.edu/adt/) [5], que forma parte del paquete [MGLTools](https://ccsb.scripps.edu/mgltools/).

### 4. Ejecución del Docking
Desarrollamos scripts automatizados para ejecutar consecutivamente los estudios de docking de cada receptor de todos los ligandos utilizando [AutoDock Vina](https://vina.scripps.edu/) [2]. Para ello se utilizó como referencia [un video de YouTube](https://www.youtube.com/watch?v=tFFxNTvvoJI) que implementaba un algoritmo en Perl, se realizaron los cambios necesarios para poder realizarlo con Python y permitir que se realice para más de un receptor, dado que en la referencia se trabajaba con uno solo.

Para ello se desarrollaron dos scripts principales:
- *Vina.py:* Adaptación del script de perl del video. Permite que se pase como argumento el identificador del receptor a utilizar. Luego va realizando la ejecución de vina para cada uno de los ligandos con el receptor que se haya pasado, guardando los logs en un archivo .log en *Dockings/receptor/* y las poses de los ligandos en *out/receptor/* . Este proceso generó los logs con información sobre la afinidad de los ligandos para cada receptor en distintas poses, e información sobre estas poses.

### 5. Procesamiento y Análisis de Resultados
Una vez completados los estudios de docking, procesamos los logs para extraer las afinidades de la mejor pose de cada ligando-receptor. Ademas, identificamos y eqtiquetamos los outliers, proporcionando una visión más clara de las interacciones más relevantes y significativas.

## Resultados
Este estudio nos proporcionó un paso más hacia la dilucidacióin de las posibles funciones de los receptores olfatorios presentes en la base de datos de partida. Además nos permitió consolidar un flujo de trabajo que podría ser aplicable y generalizado con facilidad a nuevos receptores e incluso ligandos. La modularidad de scripts permite que se vayan modificando o utilizando segun las necesidades de los procesos.

## Referencias
1. Bioinformatics With BB (Director). (2020, julio 30). Molecular Docking  | Autodock VINA Virtual Screening  | VINA Docking tutorial | Bioinformatics. https://www.youtube.com/watch?v=tFFxNTvvoJI

2. Eberhardt, J., Santos-Martins, D., Tillack, A. F., & Forli, S. (2021). AutoDock Vina 1.2.0: New Docking Methods, Expanded Force Field, and Python Bindings. Journal of Chemical Information and Modeling, 61(8), 3891-3898. https://doi.org/10.1021/acs.jcim.1c00203

3. Harini, K., & Sowdhamini, R. (2015). Computational Approaches for Decoding Select Odorant-Olfactory Receptor Interactions Using Mini-Virtual Screening. PLOS ONE, 10(7), e0131077. https://doi.org/10.1371/journal.pone.0131077

4. Menardo, F., Loiseau, C., Brites, D., Coscolla, M., Gygli, S. M., Rutaihwa, L. K., Trauner, A., Beisel, C., Borrell, S., & Gagneux, S. (2018). Treemmer: A tool to reduce large phylogenetic datasets with minimal loss of diversity. BMC Bioinformatics, 19(1), 164. https://doi.org/10.1186/s12859-018-2164-8

5. Morris, G. M., Huey, R., Lindstrom, W., Sanner, M. F., Belew, R. K., Goodsell, D. S., & Olson, A. J. (2009). AutoDock4 and AutoDockTools4: Automated Docking with Selective Receptor Flexibility. Journal of computational chemistry, 30(16), 2785-2791. https://doi.org/10.1002/jcc.21256

6. O’Boyle, N. M., Banck, M., James, C. A., Morley, C., Vandermeersch, T., & Hutchison, G. R. (2011). Open Babel: An open chemical toolbox. Journal of Cheminformatics, 3(1), 33. https://doi.org/10.1186/1758-2946-3-33

7. Rocha, J. J., Jayaram, S. A., Stevens, T. J., Muschalik, N., Shah, R. D., Emran, S., Robles, C., Freeman, M., & Munro, S. (2023). Functional unknomics: Systematic screening of conserved genes of unknown function. PLOS Biology, 21(8), e3002222. https://doi.org/10.1371/journal.pbio.3002222


