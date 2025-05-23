# Awesome Materials & Chemistry Datasets

A curated list of the most useful datasets in **materials science** and **chemistry** for training **machine learning** and **AI foundation models**. This includes experimental, computational, and literature-mined datasets—prioritizing **open-access** resources and community contributions.

This project aims to:
- Catalog the best datasets by domain, type, quality, and size
- Support reproducible research in AI for chemistry and materials
- Provide a community-driven resource with contributions from researchers and developers

---

## Table of Contents

- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [Datasets](#datasets)
  - [Computational (DFT, MD)](#computational-datasets)
  - [Experimental](#experimental-datasets)
  - [LLM Training](#llm-training-datasets)
  - [Literature-mined & Text](#literature-mined--text-datasets)
  - [Proprietary](#proprietary-datasets)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## How to Use

- Explore datasets by domain or data type using the tables below
- Click the **access links** to explore or download the data
- Sort/filter by quality, size, and suitability for ML models
- Fork the repo and submit a pull request to add new datasets

---

## Contributing

Want to add a new dataset or improve metadata?

1. Fork the repository
2. Edit the appropriate dataset list or add a new entry
3. Submit a pull request with a brief description and source
4. Use the following fields:
   - Dataset Name
   - Domain
   - Type (`Computational`, `Experimental`, `Literature-mined`)
   - Size
   - Access (Open/Restricted/Proprietary)
   - Format (JSON, CSV, CIF, HDF5, SMILES, etc.)
   - License
   - Access Link
   - Notes or Use Cases

---

## Datasets

### Computational Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     | Link |
|--------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|------|
| OMat24 (Meta)                  | Inorganic crystals      | 110M DFT entries         | Computational | JSON/HDF5   | CC BY 4.0   | Open       | [OMat24](https://huggingface.co/datasets/fairchem/OMAT24) |
| OMol25 (Meta)                  | Molecular chemistry     | 100M+ DFT calculations   | Computational | LMDB        | CC BY 4.0   | Open       | [OMol25](https://huggingface.co/facebook/OMol25) |
| Materials Project (LBL)        | Inorganic crystals      | 500k+ compounds          | Computational | JSON/API    | CC BY 4.0   | Open       | [materialsproject.org](https://materialsproject.org) |
| Open Catalyst 2020 (OC20)      | Catalysis (surfaces)    | 1.2M relaxations         | Computational | JSON/HDF5   | CC BY 4.0   | Open       | [opencatalystproject.org](https://opencatalystproject.org) |
| AFLOW                          | Inorganic materials     | 3.5M materials           | Computational | REST API    | Open        | Open       | [aflow.org](https://aflow.org) |
| OQMD                          | Inorganic solids        | 1M+ compounds            | Computational | SQL/CSV     | Open         | Open       | [oqmd.org](https://oqmd.org) |
| JARVIS-DFT (NIST)              | 3D/2D materials          | 40k+ entries             | Computational | JSON/API    | Open       | Open       | [jarvis.nist.gov](https://jarvis.nist.gov) |
| Carolina Materials DB          | Hypothetical crystals   | 214k structures          | Computational | JSON        | CC BY 4.0   | Open       | [carolinamatdb.org](http://www.carolinamatdb.org) |
| NOMAD          | Various DFT/MD   | >19M calculations          | Computational | JSON        | CC BY 4.0   | Open       | [NOMAD Repository](https://nomad-lab.eu/prod/v1/gui/search/entries/search/entries) |
| MatPES | DFT Potential Energy Surfaces | ~400,000 structures from 300K MD simulations | Computational | JSON | | Open | [MatPES](https://matpes.ai)
| Vector-QM24 | Small organic and inorganic molecules | 836k conformational isomers | Computational | JSON | Placeholder | Open | [V-QM24](https://doi.org/10.5281/zenodo.11164951) |
| AIMNet2 Dataset | Non-metallic compounds | 20M hybrid DFT calculations | Computational | JSON | Open | Open | [AIMNet](https://doi.org/10.1184/R1/27629937.v1) |
| RDB7 | Barrier height and enthalpy for small organic reactions | 12k CCSD(T)-F12 calculations | Computational | CSV | Open | Open | [Zenodo](https://zenodo.org/records/13328872) |
| RDB19-Rad | ΔG of activation and of reaction for organic reactions in 40 common solvents | 5.6k DFT + COSMO-RS calculations | Computational | CSV | Open | Open | [Zenodo](https://zenodo.org/records/11493786) |
| QCML | Small molecules consisting of up to 8 heavy atoms | 14.7B Semi-empirical + 33.5M DFT calculations | Computational | TFDS | CC BY-NC 4.0 | Open | [Zenodo](https://zenodo.org/records/14859804) |



---

### Experimental Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     | Link |
|---------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|------|
| Crystallography Open Database (COD) | Crystal structures  | ~525k entries            | Experimental | CIF/SMILES  | CC0 1.0     | Open       | [crystallography.net/cod](https://www.crystallography.net/cod) |
| NIST ICSD (subset)             | Inorganic structures     | ~290k structures         | Experimental  | CIF         | Proprietary | Restricted | [icsd.products.fiz-karlsruhe.de](https://icsd.products.fiz-karlsruhe.de) |
| CSD (Cambridge)                | Organic crystals         | ~1.3M structures         | Experimental  | CIF         | Proprietary | Restricted | [ccdc.cam.ac.uk](https://www.ccdc.cam.ac.uk) |
| [opXRD](https://arxiv.org/abs/2503.05577) | Crystal structures |  92552 (2179 labeled) | Experimental | JSON       | CC BY 4.0 | Open | [zenodo.org](https://doi.org/10.5281/zenodo.14254270) |
| MDR SuperCon | Superconductivity  | legacy superconductor database w/ material composition, structure, properties, and processes | Mixed |  | CC BY 4.0 | Open | [NIMS MDR](https://mdr.nims.go.jp/collections/4c428a0c-d209-4990-ad1f-656d05d1cfe2)|

---

### LLM Training Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     | Link |
|--------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|------|
| ChemPile                       | Chemistry               | 75B+ tokens              | LLM Training | Mixed       | Open        | Open       | [ChemPile](https://huggingface.co/collections/jablonkagroup/chempile-6824e88c60d3286ba9b0dae1) |
| SmolInstruct | Small molecules | 3.3M samples | LLM Training | JSON | CC BY 4.0 | Open | [SmolInstruct](https://huggingface.co/datasets/osunlp/SMolInstruct) |
| CAMEL | Chemistry | 20K problem-solution pairs | LLM Training | JSON | Open | Open | [CAMEL](https://huggingface.co/datasets/camel-ai/chemistry) |
| ChemNLP | Chemistry | Extensive, many combined datasets | LLM Training | JSON | Open | Open | [ChemNLP](https://github.com/OpenBioML/chemnlp) |
| MaScQA | Materials Science | 640 QA pairs | LLM Training | XLSX | Open | Open | [MaScQA](https://github.com/abhijeetgangan/MaSTeA) |
| SciCode | Research Coding in Physics, Math, Material Science, Biology, and Chemistry | 338 subproblems | LLM Training | JSON | Open | Open | [SciCode](https://scicode-bench.github.io) |


---

### Literature-mined & Text Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     | Link |
|--------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|------|
| PubChem                        | Molecules & data        | 119M compounds           | Literature    | SMILES/SDF  | Public Domain | Open    | [pubchem.ncbi.nlm.nih.gov](https://pubchem.ncbi.nlm.nih.gov) |
| USPTO Reactions                | Organic reactions       | 1.8M reactions           | Literature    | RXN/SMILES  | Open        | Open       | [USPTO MIT](http://bit.ly/USPTOpatents) |
| Open Reaction Database (ORD)   | Synthetic reactions     | ~1M reactions            | Experimental/Lit | JSON     | CC BY 4.0   | Open       | [open-reaction-database.org](https://open-reaction-database.org) |
| PatCID (IBM)                   | Chemical image data     | 81M images / 13M mols    | Literature    | PNG/SMILES  | Open        | Open       | [github.com/DS4SD/PatCID](https://github.com/DS4SD/PatCID) |
| MatScholar                     | NLP corpus (materials)  | 5M+ abstracts            | Literature    | JSON/Graph  | Open        | Open       | [matscholar.com](https://matscholar.com) |

---

### Proprietary Datasets (for reference)

| Dataset                         | Domain                  | Size                     | Access      | Use Case Notes |
|--------------------------------|-------------------------|--------------------------|-------------|----------------|
| CAS Registry                   | Chemical substances     | 250M+ substances         | Proprietary | Industry standard for molecule indexing |
| Reaxys (Elsevier)              | Reactions & properties  | Millions of reactions    | Proprietary | Rich curated literature reaction data |
| Citrine Informatics DB         | Experimental materials  | Private                  | Proprietary | Materials ML platform w/ industry data |
| CSD (Cambridge)                | Organic crystals        | 1.3M+                    | Proprietary | Gold-standard X-ray structures |
| [PoLyInfo](https://polymer.nims.go.jp/en/)   | Polymers & properties   | 500k+ data points / Experimental       | Proprietary  | Polymer properties from literature sources |

### Dataset Resources
* [The Materials Data Facility](https://www.materialsdatafacility.org) - Over 100 TB of open materials data. #TODO list some of these in the tables above
* [Foundry-ML](https://materialsdatafacility.org/portal) *search Foundry* - 61 structured datasets ready for download through a Python client #TODO list some of these in the tables above

## TODO
* Classify and add [CRIPT](https://www.criptapp.org) for polymer data
* Classify and add [Polymer Genome](https://khazana.gatech.edu) and other datasets from Khazana
* A dataset on solubilities of gases in polymers (15 000 experimental measurements of 79 gases' uptakes (0.01–50 wt%) in 102 different polymers, pressures from 1 × 10−3 to 7 × 102 bar and temperatures from 233 to 508 K, includes nearly 500 solvent–polymer systems). Optimized structures of various repeating units are included. Should it be of interest for you, it is available here: [Data](https://github.com/Shorku/rhnet/tree/main/data)
* Add [Materials Cloud Datasets](https://www.materialscloud.org/discover/menu)
* Classify [Atomly](https://atomly.net/#/). A bit challenging with non-English
* Look into adding NOMAD for experimental data as well
* Review [Alexandria Materials](https://alexandria.icams.rub.de)
* Add A Quantum-Chemical Bonding Database for Solid-State Materials Part 1: https://zenodo.org/records/8091844 Part 2: https://zenodo.org/records/8092187
* Add QM datasets. http://quantum-machine.org/datasets/
---

### Other Links
* [Awesome Materials Informatics](https://github.com/tilde-lab/awesome-materials-informatics)

---

## License

This project is licensed under the **MIT License**. Each dataset listed has its **own license**, noted in the table. Always check the source's license before using the data in your project.

---

## Acknowledgements

Thanks to the open data and research communities including:
- Meta AI FAIR
- The Materials Data Facility / Foundry-ML
- NIST JARVIS and Materials Project
- LBL, MIT, CCDC, FIZ Karlsruhe
- Contributors to Open Catalyst, PubChem, ORD, and AFLOW
- Developers of open chemistry toolkits (RDKit, Open Babel)

---

## Citation

If this repository was helpful in your work, feel free to cite or star the repo. You can also reference the underlying dataset publications linked above.
