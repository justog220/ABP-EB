<div align="center">

# ABP Estructuras Biomoleculares

## Garcia - Giorgio


[Descripción](#-descripción) • [Estructura de Directorios](#file_folder-estructura-de-directorios) • [Links de Interés](#paperclip-links-de-interés) • [Roadmap](#world_map-roadmap) • [Contacto](#-contacto) • [Referencias](#-referencias)



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

- **Alineamiento de Secuencias**: Realizamos alineamientos de secuencias para comparar y analizar la similitud entre los receptores olfatorios identificados.
- **Construcción de Árboles Filogenéticos**: Levvamos a cabo la generación de un árbol filogenético a partir del alienamiento del ítem anterior.
- **Reducción de Dimensionalidad**: Aplicamos técnicas de reducción de dimensionalidad para visualizar y comprender mejor la estructura de los receptores olfatorios y las proteínas relacionadas.
- **BlastP**: Utilizamos BlastP para encontrar proteínas similares a los receptores olfatorios presentes en Unknome.
- **RMSD y TM-Score**: Calculamos las raíces de las medias de los cuadrados de las diferencias (RMSD) y los TM-Scores para evaluar la superposición estructural entre los receptores olfatorios y las proteínas identificadas mediante BlastP.
- **Screening de Ligandos**: Realizamos un screening para identificar posibles ligandos que podrían interactuar con los receptores olfatorios, utilizando métodos computacionales.


Este análisis de los receptores olfatorios no solo proporciona información sobre su estructura y potenciales interacciones, sino que también sugiere un enfoque para dilucidar la función de proteínas poco conocidas, como las del proyecto Unknome. Estos procesos podrían ser un paso crucial hacia la comprensión de la biología subyacente y la función de estas proteínas poco estudiadas.

### :file_folder: Estructura de directorios
- /Exploracion: Análisis exploratorio de la base de datos
	- /PFAM: Análisis de familias de proteínas presentes en la base de datos.
- /imgs: Imágenes utilizadas en READMES
- /OlfatoryReceptors: Carpeta con análisis correspondientes a la familia de receptores olfatorios.
	- /Alignment: Alineamiento de las secuencias de receptores olfatorios.
	- /data: Subset de proteínas de receptores olfatorios.
	- /Docking: Desarrollo de scripts para AutoDocking de receptores olfatorios y ligandos.
	- /PhyTree: Creación de árbol filogenético.
	- /Preparation: Obtención de subsets de proteínas de receptores olfatorios.
	- /ReceptoresFiltrados: Reducción de dimensionalidad del árbol filogenético, con la obtención del subset y descarga de las estructuras PDB correspondientes.
		- /Estructuras: Estructuras del PDB.
	- /Treemmer: Módulo utilizado para reducir la dimensionalidad del árbol.



### :computer: Requisitos
- Base de Datos Unknome
- Python
	- Modulos utilizados especificados en cada carpeta en *requirements.txt*.
- Clustal Omega
- Treemmer
- AutoDock Vina
- AutoDock Tools



### :paperclip: Links de interés
- [Unknome](https://unknome.mrc-lmb.cam.ac.uk/)
- [Bitácora](https://docs.google.com/document/d/1hfnAr0R3DH2llRegLN6dVXDsyPDdvUwWzP8I5dPmboY/edit?usp=sharing)
- [Informe](https://docs.google.com/document/d/1W4E4xc-yobJKqFuypAWl4mKD40Bq83cPE_Dq3pm-OxU/edit?usp=sharing)

### :world_map: Roadmap

[Link a Roadmap con lo trabajado en este ABP](https://roadmap.sh/r/abp-eb)

### 📬 Contacto
- Estudiantes a cargo del proyecto
	- justo.garcia@ingenieria.uner.edu.ar
	- giovani.giorgio@ingenieria.uner.edu.ar
- Docente a cargo de la materia
	- pablo.schierloh@uner.edu.ar

### 📚 Referencias

[1.][ref-1] Bioinformatics With BB (Director). (2020, julio 30). Molecular Docking  | Autodock VINA Virtual Screening  | VINA Docking tutorial | Bioinformatics. https://www.youtube.com/watch?v=tFFxNTvvoJI

[2.][ref-2] Eberhardt, J., Santos-Martins, D., Tillack, A. F., & Forli, S. (2021). AutoDock Vina 1.2.0: New Docking Methods, Expanded Force Field, and Python Bindings. Journal of Chemical Information and Modeling, 61(8), 3891-3898. https://doi.org/10.1021/acs.jcim.1c00203

[3.][ref-3] Harini, K., & Sowdhamini, R. (2015). Computational Approaches for Decoding Select Odorant-Olfactory Receptor Interactions Using Mini-Virtual Screening. PLOS ONE, 10(7), e0131077. https://doi.org/10.1371/journal.pone.0131077

[4.][ref-4] Menardo, F., Loiseau, C., Brites, D., Coscolla, M., Gygli, S. M., Rutaihwa, L. K., Trauner, A., Beisel, C., Borrell, S., & Gagneux, S. (2018). Treemmer: A tool to reduce large phylogenetic datasets with minimal loss of diversity. BMC Bioinformatics, 19(1), 164. https://doi.org/10.1186/s12859-018-2164-8

[5.][ref-5] Morris, G. M., Huey, R., Lindstrom, W., Sanner, M. F., Belew, R. K., Goodsell, D. S., & Olson, A. J. (2009). AutoDock4 and AutoDockTools4: Automated Docking with Selective Receptor Flexibility. Journal of computational chemistry, 30(16), 2785-2791. https://doi.org/10.1002/jcc.21256

[6.][ref-6] O’Boyle, N. M., Banck, M., James, C. A., Morley, C., Vandermeersch, T., & Hutchison, G. R. (2011). Open Babel: An open chemical toolbox. Journal of Cheminformatics, 3(1), 33. https://doi.org/10.1186/1758-2946-3-33

[7.][ref-7] Paysan-Lafosse, T., Blum, M., Chuguransky, S., Grego, T., Pinto, B. L., Salazar, G. A., Bileschi, M. L., Bork, P., Bridge, A., Colwell, L., Gough, J., Haft, D. H., Letunić, I., Marchler-Bauer, A., Mi, H., Natale, D. A., Orengo, C. A., Pandurangan, A. P., Rivoire, C., … Bateman, A. (2023). InterPro in 2022. Nucleic Acids Research, 51(D1), D418-D427. https://doi.org/10.1093/nar/gkac993

[8.][ref-8] Price, M. N., Dehal, P. S., & Arkin, A. P. (2010). FastTree 2 – Approximately Maximum-Likelihood Trees for Large Alignments. PLOS ONE, 5(3), e9490. https://doi.org/10.1371/journal.pone.0009490

[9.][ref-9] Rocha, J. J., Jayaram, S. A., Stevens, T. J., Muschalik, N., Shah, R. D., Emran, S., Robles, C., Freeman, M., & Munro, S. (2023). Functional unknomics: Systematic screening of conserved genes of unknown function. PLOS Biology, 21(8), e3002222. https://doi.org/10.1371/journal.pbio.3002222

[10.][ref-10] Sievers, F., Wilm, A., Dineen, D., Gibson, T. J., Karplus, K., Li, W., Lopez, R., McWilliam, H., Remmert, M., Söding, J., Thompson, J. D., & Higgins, D. G. (2011). Fast, scalable generation of high-quality protein multiple sequence alignments using Clustal Omega. Molecular Systems Biology, 7, 539. https://doi.org/10.1038/msb.2011.75

[11.][ref-11] Varadi, M., Bertoni, D., Magana, P., Paramval, U., Pidruchna, I., Radhakrishnan, M., Tsenkov, M., Nair, S., Mirdita, M., Yeo, J., Kovalevskiy, O., Tunyasuvunakool, K., Laydon, A., Žídek, A., Tomlinson, H., Hariharan, D., Abrahamson, J., Green, T., Jumper, J., … Velankar, S. (2024). AlphaFold Protein Structure Database in 2024: Providing structure coverage for over 214 million protein sequences. Nucleic Acids Research, 52(D1), D368-D375. https://doi.org/10.1093/nar/gkad1011

[ref-1]: #ref-1
[ref-2]: #ref-2
[ref-3]: #ref-3
[ref-4]: #ref-4
[ref-5]: #ref-5
[ref-6]: #ref-6
[ref-7]: #ref-7
[ref-8]: #ref-8
[ref-9]: #ref-9
[ref-10]: #ref-10
[ref-11]: #ref-11