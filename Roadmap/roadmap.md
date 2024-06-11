---
title: ABP Estructuras Biomoléculares
markmap:
  colorFreezeLevel: 2
---

## 1. Elección de la temática <!-- markmap: foldAll -->
- Clase
- Discusión con profesores y pares


## 2. Exploración de [Unknome](https://unknome.mrc-lmb.cam.ac.uk/) <!-- markmap: foldAll -->
- Lectura del [artículo](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002222)
- Bajar [BD](https://unknome.mrc-lmb.cam.ac.uk/download/)
- Analizar [diagrama de tablas](https://github.com/justog220/ABP-EB/blob/main/Exploracion/DiagramaDeTablas.pdf)
- Llevar a cabo [análisis exploratorio](https://github.com/justog220/ABP-EB/tree/main/Exploracion)


## 3. Elección de PFAM <!-- markmap: foldAll -->
- Familiarizarse con PFAM e [InterPro](https://www.ebi.ac.uk/interpro/)
- [Scrapping de nombres cotidianos](https://github.com/justog220/ABP-EB/tree/main/Exploracion#2-an%C3%A1lisis-de-pfam)
- Análisis de [Receptores Olfatorios](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors)


## 4. Creación de subset de Receptores Olfatorioss <!-- markmap: foldAll -->
- Consultas con SQL al Unknome


## 5. Alineamiento <!-- markmap: fold -->
- [Creación multifasta](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors/Alignment#1-generaci%C3%B3n-del-multifasta)
    - Familiarización con el formato
    - Extracción de la información necesaria de la BD
- Instalación [Clustal Omega](http://www.clustal.org/omega/)
- [Ejecución del alineamiento](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors/Alignment#2-alineamiento) <!-- markmap: fold -->
    - ```bash clustalo -i olfatorys_receptor.multifasta -o olfatorys_alignment.fa --verbose```


## 6. Árbol Filogenético <!-- markmap: foldAll -->
- Instalación [FastTree](http://www.microbesonline.org/fasttree/)
- [Ejecución de FastTree](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors/PhyTree#metodolog%C3%ADa)
    - ```bash fasttreeMP ../Alignment/olfatorys_alignment.fa > olfatorys_receptor.tree```
- [Visualización](https://github.com/justog220/ABP-EB/blob/main/OlfatoryReceptors/PhyTree/README.md#2-visualizaci%C3%B3n)


## 7. [Filtrado del Árbol](https://github.com/justog220/ABP-EB/blob/main/OlfatoryReceptors/PhyTree/README.md#3-reducci%C3%B3n-de-dimensionalidad) <!-- markmap: foldAll -->
- [Treemmer](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2164-8)
- [Obtención del subset](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors/ReceptoresFiltrados#1-generaci%C3%B3n-del-subset)

## 8. Obtención de estructuras de receptores <!-- markmap: fold -->
- Scrapping de [AlphaFold](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors/ReceptoresFiltrados#2-obtenci%C3%B3n-de-estructuras)
    - Creación de archivos PDB


## 9. [BlastP](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors/ReceptoresFiltrados#3-blastp) <!-- markmap: fold -->

### Selección de homólogas <!-- markmap: fold -->

|Receptor|Ligando|Olor|Especie|
|:---:|:---:|:---:|:---:|
|8HTI|Ácido octanoico|Rancio, quemado, grasiento|Homo Sapiens|
|8F76|Ácido propanoico|Acre|Homo Sapiens|
|8J46|Apo State|-|Homo Sapiens|


### Análisis de métricas 
- [RMSD](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors/ReceptoresFiltrados#rmsd)
    - Alineamiento estructural
- [TM-Score](https://github.com/justog220/ABP-EB/tree/main/OlfatoryReceptors/ReceptoresFiltrados#tm-score)

## 11. Docking <!-- markmap: foldAll -->

### [Descarga de ligandos](https://github.com/justog220/ABP-EB/blob/main/OlfatoryReceptors/Docking/README.md#2-selecci%C3%B3n-y-preparaci%C3%B3n-de-ligandos) <!-- markmap: foldAll -->
- Scrapping de PubChem


### [Preparación de ligandos](https://github.com/justog220/ABP-EB/blob/main/OlfatoryReceptors/Docking/README.md#2-selecci%C3%B3n-y-preparaci%C3%B3n-de-ligandos) <!-- markmap: foldAll -->
- Conversión a PDBQT con OpenBabel
- Adición de hidrógenos polares


### [Preparación de receptores](https://github.com/justog220/ABP-EB/blob/main/OlfatoryReceptors/Docking/README.md#3-preparaci%C3%B3n-de-receptores) <!-- markmap: foldAll -->
- Añadir hidrógenos
- Añadir átomos faltantes
- Añadir cargas parciales
- Definir GridBox
- [Creación de archivos .config](https://github.com/justog220/ABP-EB/blob/main/OlfatoryReceptors/Docking/README.md#4-declaraci%C3%B3n-de-configuraciones)


### [Codificación screening](https://github.com/justog220/ABP-EB/blob/main/OlfatoryReceptors/Docking/README.md#5-ejecuci%C3%B3n-del-docking) <!-- markmap: foldAll -->
- Traducción de scripts a Python
- Preparación de scripts para trabajar con múltiples receptores


### [Procesamiento de logs](https://github.com/justog220/ABP-EB/blob/main/OlfatoryReceptors/Docking/README.md#6-procesamiento-y-an%C3%A1lisis-de-resultados) <!-- markmap: foldAll -->
- Obtención de afinidades de mejor polares
- Gráfico de BoxPlots
- Obtención de outliers


## [ ] 12. Análisis outliers  <!-- markmap: fold -->
### Encontrar alguno con uso conocido
### Analizar sus poses
### Ver si hay drogas similares en [ZINC](https://zinc.docking.org/)