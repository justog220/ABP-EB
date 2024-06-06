<div align="center">

# ABP Estructuras Biomoleculares

## Garcia - Giorgio

[Descripción](#descripcion) • [Estructura de Directorios](#estructura-de-directorios) • [Links de Interés](#links-de-interes) • [Roadmap](#roadmap) • [Contacto](#contacto) • [Referencias](#referencias)



<div style="text-align: center;">
    <div style="display: inline-flex; align-items: center;">
        <img src="imgs/logo_eb.png" alt="Logo EB" style="height: 50px;margin-right: 20px;">
        <img src="imgs/logouner.png" alt="Logo UNER" style="height: 50px;">
    </div>
</div>


</div>



### 📖 Descripción
Este proyecto es el resultado de un proceso de aprendizaje basado en problemas en la materia de Estructuras Biomoléculares.

Partiendo de la base de datos de proteínas poco estudiadas, conocida como Unknome, realizamos un análisis exploratorio para comprender la composición y distribución de las proteínas presentes. Durante este proceso, identificamos una presencia significativa de receptores olfatorios.

Decidimos profundizar en el estudio de estos receptores olfatorios y llevamos a cabo una serie de análisis, que incluyeron:

- **BlastP**: Utilizamos BlastP para encontrar proteínas similares a los receptores olfatorios presentes en Unknome.
- **Alineamiento de Secuencias**: Realizamos alineamientos de secuencias para comparar y analizar la similitud entre los receptores olfatorios identificados.
- **RMSD y TM-Score**: Calculamos las raíces de las medias de los cuadrados de las diferencias (RMSD) y los TM-Scores para evaluar la superposición estructural entre los receptores olfatorios y las proteínas identificadas mediante BlastP.
- **Reducción de Dimensionalidad**: Aplicamos técnicas de reducción de dimensionalidad para visualizar y comprender mejor la estructura de los receptores olfatorios y las proteínas relacionadas.
- **Screening de Ligandos**: Realizamos un screening para identificar posibles ligandos que podrían interactuar con los receptores olfatorios, utilizando métodos computacionales.


Este análisis de los receptores olfatorios no solo proporciona información sobre su estructura y potenciales interacciones, sino que también sugiere un enfoque para dilucidar la función de proteínas poco conocidas, como las del proyecto Unknome. Estos procesos podrían ser un paso crucial hacia la comprensión de la biología subyacente y la función de estas proteínas poco estudiadas.

### :file_folder: Estructura de directorios
- /Corr: Análisis de correlaciones de parámetros
- /DB: Base de datos del proyecto
- /Docking: Desarrollo de scripts para AutoDocking de receptores olfatorios y ligandos.
- /Exploracion: Análisis exploratorio de la base de datos
	- /PFAM: Análisis de familias de proteínas presentes en la base de datos.
- /imgs: Imágenes utilizadas en READMES
- /OlfatoryReceptors: Carpeta con análisis correspondientes a la familia de receptores olfatorios.
	- /Alignment: Alineamiento de las secuencias de receptores olfatorios.
	- /data: Subset de proteínas de receptores olfatorios.
	- /PhyTree: Creación de árbol filogenético.
	- /Preparation: Obtención de subsets de proteínas de receptores olfatorios.
	- /ReceptoresFiltrados: Reducción de dimensionalidad del árbol filogenético, con la obtención del subset y descarga de las estructuras PDB correspondientes.
		- /Estructuras: Estructuras del PDB.
	- /Treemmer: Módulo utilizado para reducir la dimensionalidad del árbol.



### :paperclip: Links de interés
- [Unknome](https://unknome.mrc-lmb.cam.ac.uk/)
- [Bitácora](https://docs.google.com/document/d/1hfnAr0R3DH2llRegLN6dVXDsyPDdvUwWzP8I5dPmboY/edit?usp=sharing)
- [Informe](https://docs.google.com/document/d/1W4E4xc-yobJKqFuypAWl4mKD40Bq83cPE_Dq3pm-OxU/edit?usp=sharing)

### :world_map: Roadmap

[Link a Roadmap con lo trabajado en este ABP](https://roadmap.sh/r/abp-eb)

### 📬 Contacto
- Alumnos a cargo del proyecto
	- justo.garcia@ingenieria.uner.edu.ar
	- giovani.giorgio@ingenieria.uner.edu.ar
- Docente a cargo de la materia
	- pablo.schierloh@uner.edu.ar




### 📚 Referencias
- Rocha, J. J., Jayaram, S. A., Stevens, T. J., Muschalik, N., Shah, R. D., Emran, S., Robles, C., Freeman, M., & Munro, S. (2023). Functional unknomics: Systematic screening of conserved genes of unknown function. PLOS Biology, 21(8), e3002222. https://doi.org/10.1371/journal.pbio.3002222

- Menardo, F., Loiseau, C., Brites, D., Coscolla, M., Gygli, S. M., Rutaihwa, L. K., Trauner, A., Beisel, C., Borrell, S., & Gagneux, S. (2018). Treemmer: A tool to reduce large phylogenetic datasets with minimal loss of diversity. BMC Bioinformatics, 19(1), 164. https://doi.org/10.1186/s12859-018-2164-8

- Typhaine Paysan-Lafosse, Matthias Blum, Sara Chuguransky, Tiago Grego, Beatriz Lázaro Pinto, Gustavo A Salazar, Maxwell L Bileschi, Peer Bork, Alan Bridge, Lucy Colwell, Julian Gough, Daniel H Haft, Ivica Letunić, Aron Marchler-Bauer, Huaiyu Mi, Darren A Natale, Christine A Orengo, Arun P Pandurangan, Catherine Rivoire, Christian J A Sigrist, Ian Sillitoe, Narmada Thanki, Paul D Thomas, Silvio C E Tosatto, Cathy H Wu, Alex Bateman, InterPro in 2022, Nucleic Acids Research, Volume 51, Issue D1, 6 January 2023, Pages D418–D427, https://doi.org/10.1093/nar/gkac993