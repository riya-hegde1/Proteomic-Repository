# Proteomic-Repository

## Background and Motivation </h2>

Proteomics carries a growing significance in unraveling biological processes involving proteins — a proteomic study analyzes the protein expression of an organism, tissue, cell, or organelle. Mass spectrometry, a central proteomic tool, allows researchers to categorize proteins using their mass and charge. Proteomics has helped researchers make advancements in the fields of disease research, drug development, and functional analysis. Proteomics plays an essential role in deepening our understanding of diseases and biological functions, which can be applied in fields such as medicine and biotechnology. 

We hoped to create a comprehensive compilation of relevant proteomics information aimed at enhancing accessibility and utilization of proteomics data. 

We sought to bridge the gap between intricate proteomic data sets and the scientific community, by synthesizing relevant information from various research papers in a structured and tabulated format. This approach facilitates efficient comprehension and utilization of data, enabling the broader scientific community to extract valuable information, despite barriers created by fragmented data. 

Our motivation stems from the realization that invaluable proteomics data often exists in a scattered state, creating challenges for researchers to effectively utilize this wealth of information. We meticulously curated essential aspects of the study design, such as blah blah (the categories we will do — maybe metadata and analytical tools?) to empower researchers with a tool that expedites data exploration, analysis, and interpretation. In this way, we aspire to contribute to the acceleration of scientific discoveries and proteomic research advancement.

___

## Methods and Procedures

### **Step 1: Search for relevant proteomic articles:**
+ Use keywords such as phosphorylation, phospho-proteomics, proteome, mass spectrometry, protein expression etc.
  + Example study: Temporal and Sex-Linked Protein Expression Dynamics in a Familial Model of [Alzheimer’s Disease paper]([url](https://doi.org/10.1016/j.mcpro.2022.100280))

### **Step 2: Search for peptide and protein-level datasets within the articles:**
+ Within the dataset, we look for a matrix between peptides x samples containing the intensities. This may also be protein x samples as well. 
  + Excel (xlsx) or text file (csv) files are simpler to understand and process; priority goes to these files. 

Example file:


+ Check paper in the order of Supplementary Tables, Supplementary Materials, Data Availability section, and [PRIDE repository](https://www.ebi.ac.uk/pride/archive/)
  + The accession number for the PRIDE repository is usually in the data availability section. 
  + Look for other keywords related to the software used to process this type of data: PEAKS, ProteomeDiscoverer, Scaffold, MaxQuant, OpenMS

### **Step 3: Search for additional information relevant to the study:**
+ After finding some studies and data files, our team attempted to identify sample metadata (i.e. additional sample information, grouping, tissue, time point, etc.). Exact variables will depend on the study. 
+ Goal of finding as many studies and datasets as possible. Our team performed this by identifying Excel files for peptide or protein matrices, downloading them, and noting the source from which they were obtained. 
  + Our aim was to identify and note as much information about the study as possible, such as metadata information about the samples and the experimental design of the study (see the checklist below for some important variables related to the study).

### **Info needed from PRIDE repository/paper (and the experimental design):**
+ Paper info: Paper title, link and PMID ID
+ Data repository: PRIDE ID PXD######
+ Is there Sample annotation file (aka metadata information)?
+ What type of data (Phosphorylation or Expression)?
  + Info about mass-spectrometry experiment:
    + Is it Label-free or Labeled?
    + Is it Unfractionated or fractionated?
+ Is the data matrix Peptide or Protein level?
+ Is the data matrix available for download? If matrix not available, search for the following:
  + TMT lot # (if labeled study)
  + Availability of Search files (.mgf files). (if search files not available look for the following information)
    + Are Enzymes used?
    + Are raw files available? (.raw files)?
+ Link or description to obtain Sample annotation file (if available)
+ Link or description to obtain Data matrix
+ Link or description to obtain Additional files (Search or Raw files)
