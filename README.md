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

## Contributing

Want to add a new dataset or improve metadata?

1. Fork the repository
2. Edit the appropriate dataset list or add a new entry
3. Submit a pull request with a brief description and download link
OR
4. Submit as an issue
---

## Datasets

### Computational Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     |
|--------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|
| [OMat24 (Meta)](https://huggingface.co/datasets/fairchem/OMAT24)                  | Inorganic crystals      | 110M DFT entries         | Computational | JSON/HDF5   | CC BY 4.0   | Open       |
| [OMol25 (Meta)](https://huggingface.co/facebook/OMol25)                  | Molecular chemistry     | 100M+ DFT calculations   | Computational | LMDB        | CC BY 4.0   | Open       |
| [Materials Project (LBL)](https://materialsproject.org)        | Inorganic crystals      | 500k+ compounds          | Computational | JSON/API    | CC BY 4.0   | Open       |
| [Open Catalyst 2020 (OC20)](https://opencatalystproject.org)      | Catalysis (surfaces)    | 1.2M relaxations         | Computational | JSON/HDF5   | CC BY 4.0   | Open       |
| [AFLOW](https://aflow.org)                          | Inorganic materials     | 3.5M materials           | Computational | REST API    | Open        | Open       |
| [OQMD](https://oqmd.org)                          | Inorganic solids        | 1M+ compounds            | Computational | SQL/CSV     | Open         | Open       |
| [JARVIS-DFT (NIST)](https://jarvis.nist.gov)              | 3D/2D materials          | 40k+ entries             | Computational | JSON/API    | Open       | Open       |
| [Carolina Materials DB](http://www.carolinamatdb.org)          | Hypothetical crystals   | 214k structures          | Computational | JSON        | CC BY 4.0   | Open       |
| [NOMAD](https://nomad-lab.eu/prod/v1/gui/search/entries/search/entries)          | Various DFT/MD   | >19M calculations          | Computational | JSON        | CC BY 4.0   | Open       |
| [MatPES](https://matpes.ai) | DFT Potential Energy Surfaces | ~400,000 structures from 300K MD simulations | Computational | JSON | | Open |
| [Vector-QM24](https://doi.org/10.5281/zenodo.11164951) | Small organic and inorganic molecules | 836k conformational isomers | Computational | JSON | Placeholder | Open |
| [AIMNet2 Dataset](https://doi.org/10.1184/R1/27629937.v1) | Non-metallic compounds | 20M hybrid DFT calculations | Computational | JSON | Open | Open |
| [RDB7](https://zenodo.org/records/13328872) | Barrier height and enthalpy for small organic reactions | 12k CCSD(T)-F12 calculations | Computational | CSV | Open | Open |
| [RDB19-Rad](https://zenodo.org/records/11493786) | ΔG of activation and of reaction for organic reactions in 40 common solvents | 5.6k DFT + COSMO-RS calculations | Computational | CSV | Open | Open |
| [QCML](https://zenodo.org/records/14859804) | Small molecules consisting of up to 8 heavy atoms | 14.7B Semi-empirical + 33.5M DFT calculations | Computational | TFDS | CC BY-NC 4.0 | Open |
| [QM9](http://quantum-machine.org/datasets/) | Small organic molecules | 134k molecules with quantum properties | Experimental | SDF/CSV | CC BY 4.0 | Open |
| [QM7/QM7b](http://quantum-machine.org/datasets/) | Small molecules | 7k molecules with atomization energies | Experimental | SDF/CSV | CC BY 4.0 | Open |
| [QMugs](https://www.openqdc.io/datasets/qmugs) | Drug-like molecules | 665 k mol / 2 M conf | Computational | HDF5 | CC BY 4.0 | Open |
| [C2DB](https://c2db.fysik.dtu.dk) | 2-D materials | ~4 000 entries | Computational | JSON/API | CC BY 4.0 | Open |
| [ANI-1x / 1ccx](https://qcawebapps.molssi.org/ml_datasets/) | Small organic mol | 5 M (DFT) + 0.5 M (CCSD) | Computational | HDF5 | CC BY-NC 4.0 | Open |
| [CoRE MOF 2019](https://pubs.acs.org/doi/10.1021/acs.jced.9b00835) | Metal-organic frameworks | 14 763 structures | Computational | CIF/JSON | CC BY 4.0 | Open |
| [QMOF Database](https://figshare.com/articles/dataset/QMOF_Database/13147324) | Metal-organic frameworks | 20k+ structures (DFT) | Computational | CIF/JSON | CC BY 4.0 | Open |
| [Catalysis-Hub](https://www.catalysis-hub.org) | Surface reactions | >100 k energies | Computational | JSON/API | CC BY 4.0 | Open |
| [ODAC23](https://fair-chem.github.io/dac/datasets/odac.html) | MOF + CO₂/H₂O adsorption | 38 M DFT calcs | Computational | HDF5 | CC BY 4.0 | Open |
| [MOFX-DB](https://doi.org/10.1021/acs.jced.2c00583) | Gas adsorption in MOFs | 3 M isotherm pts | Computational | CSV/HDF5 | CC BY 4.0 | Open |
| [LeMat-Bulk](https://huggingface.co/datasets/LeMaterial/LeMat-Bulk) | Inorganic materials (bulk) | 6.7M structures (5.9M materials) | Computational | HuggingFace Dataset | CC BY 4.0 | Open |
| [LeMat-Traj](https://huggingface.co/datasets/LeMaterial/LeMat-Traj) | Inorganic materials (trajectories) | 113M structures | Computational | HuggingFace Dataset | CC BY 4.0 | Open |
| [NeurIPS Open Polymer Prediction 2025](https://www.kaggle.com/competitions/neurips-open-polymer-prediction-2025/data) | Polymers | ~1,500 test polymers with MD-derived properties | Computational | CSV | Open | Open |
| [Carbon Data](https://github.com/jla-gardner/carbon-data) | Carbon materials | 22.9M atoms, 546 trajectories | Computational | EXTXYZ | Open | Open |
| [MSR-ACC/TAE25](https://zenodo.org/records/15387280) | Small molecules (up to Ar) | 76,879 total atomization energies | Computational | HDF5/CSV | Open | Open |
| [DFT Solvation Energy Dataset](https://www.doi.org/10.18126/jos5-wj65) | Small molecules | 651,290 solvation energies in 5 solvents | Computational | CSV/JSON | Open | Open |
| [MD Simulated Monomer Properties](https://doi.org/10.18126/8p6m-e135) | Small molecules | 410 molecules with thermodynamic properties | Computational | CSV/JSON | Open | Open |
| [Multimodal Spectroscopic Dataset](https://github.com/rxn4chemistry/multimodal-spectroscopic-dataset) | Molecular spectroscopy | 790k molecules with simulated spectra | Computational | HDF5/JSON | Open | Open |



---

### Experimental Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     |
|---------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|
| [Crystallography Open Database (COD)](https://www.crystallography.net/cod) | Crystal structures  | ~525k entries            | Experimental | CIF/SMILES  | CC0 1.0     | Open       |
| [NIST ICSD (subset)](https://icsd.products.fiz-karlsruhe.de)             | Inorganic structures     | ~290k structures         | Experimental  | CIF         | Proprietary | Restricted |
| [CSD (Cambridge)](https://www.ccdc.cam.ac.uk)                | Organic crystals         | ~1.3M structures         | Experimental  | CIF         | Proprietary | Restricted |
| [opXRD](https://doi.org/10.5281/zenodo.14254270) | Crystal structures |  92552 (2179 labeled) | Experimental | JSON       | CC BY 4.0 | Open |
| [MDR SuperCon](https://mdr.nims.go.jp/collections/4c428a0c-d209-4990-ad1f-656d05d1cfe2) | Superconductivity  | legacy superconductor database w/ material composition, structure, properties, and processes | Mixed |  | CC BY 4.0 | Open |
| [ChEMBL](https://www.ebi.ac.uk/chembl/) | Bioactive molecules | 2.3M+ compounds with bioactivity data | Experimental | JSON/SDF | CC BY-SA 3.0 | Open |
| [MoleculeNet](http://moleculenet.org/) | Molecular properties | 700k+ compounds across 17 datasets | Mixed | CSV/SDF | Various | Open |
| [ESOL](http://moleculenet.org/) | Aqueous solubility | 1,128 compounds with solubility data | Experimental | CSV | Open | Open |
| [FreeSolv](https://github.com/MobleyLab/FreeSolv) | Hydration free energy | 643 molecules with experimental data | Experimental | CSV | CC BY 4.0 | Open |
| [Lipophilicity](https://www.ebi.ac.uk/chembl/) | Octanol/water distribution | 4,200 compounds with logD values | Experimental | CSV | Open | Open |
| [PCBA](https://pubchem.ncbi.nlm.nih.gov/bioassay) | Bioassay screening | 400k+ compounds, 128 bioassays | Experimental | CSV | Open | Open |
| [HIV](https://wiki.nci.nih.gov/display/NCIDTPdata/AIDS+Antiviral+Screen+Data) | Antiviral screening | 41k compounds with HIV inhibition data | Experimental | CSV | Open | Open |
| [BACE](http://moleculenet.org/) | Beta-secretase inhibitors | 1,522 compounds with IC50 data | Experimental | CSV | Open | Open |
| [BBBP](http://moleculenet.org/) | Blood-brain barrier permeability | 2,053 compounds with permeability data | Experimental | CSV | Open | Open |
| [Tox21](https://tripod.nih.gov/tox21/challenge/) | Toxicity screening | 8k compounds, 12 toxicity targets | Experimental | CSV | Open | Open |
| [ToxCast](https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data) | High-throughput toxicity | 8k compounds, 600+ assays | Experimental | CSV | Open | Open |
| [SIDER](http://sideeffects.embl.de/) | Drug side effects | 1,427 drugs with adverse reactions | Experimental | CSV | Open | Open |
| [ClinTox](http://moleculenet.org/) | Clinical trial toxicity | 1,491 compounds with FDA approval status | Experimental | CSV | Open | Open |
| [PDBbind](http://www.pdbbind.org.cn/) | Protein-ligand binding | 19k complexes with binding affinities | Experimental | PDB/SDF | Open | Open |
| [BindingDB](https://www.bindingdb.org/) | Protein-ligand binding | 2.8M+ binding data points | Experimental | CSV/SDF | CC BY 4.0 | Open |
| [ProtBENCH](https://github.com/hevalatas/ProtBENCH) | Drug-target interactions | Protein family-specific datasets | Experimental | CSV | GPL-3.0 | Open |
| [PDBench](https://github.com/wells-wood-research/PDBench) | Protein sequence design | 595 protein structures, 40 architectures | Experimental | PDB | MIT | Open |
| [PDB-Struct](https://github.com/WANG-CR/PDB-Struct) | Structure-based protein design | Comprehensive protein design benchmark | Experimental | PDB | Open | Open |
| [HTEM-DB](https://htem.nrel.gov) | Thin-film composition libraries | 140 k+ samples | Experimental | JSON/API | CC0 | Open |
| [OCx24](https://github.com/facebookresearch/fairchem/tree/main/src/fairchem/applications/ocx/data) | Electrocatalyst inks | 572 samples (+DFT) | Experimental | CSV | CC BY 4.0 | Open |
| [Polymer Genome](https://khazana.gatech.edu/dataset/) | Polymers | 20 k polymers | Experimental + Comp | CSV/JSON | CC BY 4.0 | Open |
| [CoRE MOF 2024](https://www.ccdc.cam.ac.uk/support-and-resources/downloads/) | Metal-organic frameworks | 40k+ experimental MOFs | Experimental | CIF | Open | Open |
| [SAIR](https://www.sandboxaq.com/sair) | Protein-ligand binding | 1M+ complexes, 5.2M structures, 2.5TB | Experimental | 3D/CSV | CC BY-NC-SA 4.0 | Open |



---

### LLM Training Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     |
|--------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|
| [ChemPile](https://huggingface.co/collections/jablonkagroup/chempile-6824e88c60d3286ba9b0dae1)                       | Chemistry               | 75B+ tokens              | LLM Training | Mixed       | Open        | Open       |
| [SmolInstruct](https://huggingface.co/datasets/osunlp/SMolInstruct) | Small molecules | 3.3M samples | LLM Training | JSON | CC BY 4.0 | Open |
| [CAMEL](https://huggingface.co/datasets/camel-ai/chemistry) | Chemistry | 20K problem-solution pairs | LLM Training | JSON | Open | Open |
| [ChemNLP](https://github.com/OpenBioML/chemnlp) | Chemistry | Extensive, many combined datasets | LLM Training | JSON | Open | Open |
| [ChemQA](https://github.com/ChemFoundationModels/ChemLLMBench) | Chemistry | Multimodal QA dataset | LLM Training | JSON | Open | Open |
| [ChemLLMBench](https://github.com/ChemFoundationModels/ChemLLMBench) | Chemistry | 8 chemistry tasks benchmark | LLM Training | JSON | Open | Open |
| [ChemistryQA](https://github.com/microsoft/chemistry-qa) | Chemistry | 4,500 questions across 200 topics | LLM Training | JSON | Open | Open |
| [MaScQA](https://github.com/abhijeetgangan/MaSTeA) | Materials Science | 640 QA pairs | LLM Training | XLSX | Open | Open |
| [SciCode](https://scicode-bench.github.io) | Research Coding in Physics, Math, Material Science, Biology, and Chemistry | 338 subproblems | LLM Training | JSON | Open | Open |
| [ChemData 700K](https://huggingface.co/datasets/AI4Chem/ChemData700K) | Chemistry (9 core tasks) | 730K Q-A instruction pairs | LLM Training | JSON | CC BY-NC 4.0 | Open |
| [MatSci-Instruct (HoneyBee)](https://zenodo.org/record/10119842) | Materials science | ≈55K verified instructions | LLM Training | JSON | CC BY 4.0 | Open |
| [MoleculeQA](https://huggingface.co/datasets/hcaoaf/MoleculeQA) | Molecular properties & safety | 62K multiple-choice QA pairs | LLM Training | JSON | MIT | Open |
| [BioInstruct 25K](https://huggingface.co/datasets/bio-nlp-umass/bioinstruct) | Biomedical / biochemistry | 25K GPT-4 generated instructions | LLM Training | JSON | MIT | Open |
| [Lab-Bench](https://huggingface.co/datasets/futurehouse/lab-bench) | Biology | 2,400+ questions for biology agents | LLM Training | JSON | Open | Open |
| [ChemBench 4K](https://huggingface.co/datasets/AI4Chem/ChemBench4K) | Chemistry competency benchmark | 4,100 single-choice questions | LLM Training | JSON | CC BY-NC 4.0 | Open |
| [GPQA Diamond](https://github.com/idavidrein/gpqa) | Biology, Physics, Chemistry | 448 multiple-choice questions | LLM Training | JSON | Open | Open |
| [SciAssess](https://github.com/sci-assess/SciAssess) | Scientific literature analysis | Benchmark for LLMs in science | LLM Training | JSON | Open | Open |
| [ZINC20-ML](https://files.docking.org/zinc20-ML/) | Drug-like molecules (SMILES) | ≈1B molecules | LLM Training | SMILES | ZINC License | Open |
| [PMC Open Access Subset](https://huggingface.co/datasets/pmc/open_access) | Biomedical full-text | 3.4M+ articles | LLM Training | XML | Various CC | Open |
| [MatScholar Task-Schema QA (MatSci-NLP)](https://github.com/BangLab-UdeM-Mila/NLP4MatSci-ACL23) | Materials science (7 NLP tasks) | Tens of thousands of examples | LLM Training | JSON | CC BY 4.0 | Open |
| [Mol-Instructions](https://huggingface.co/collections/zjunlp/mol-instructions-662e0b9435ab6df9593e8ea0) | Chemistry | molecular, protein, and biochemical instructions | LLM Training | HuggingFace Dataset  |  Open | Open |
| [USPTO-LLM](https://zenodo.org/records/14396156) | Chemical reactions | 247K reactions | LLM Training | JSON/Graph | CC BY 4.0 | Open |
| [ChemRxivQuest](https://arxiv.org/abs/2505.05232) | Chem literature QA | 970 QA pairs | LLM Training | JSON | CC BY 4.0 | Open |
| [USPTO-Lowe](https://figshare.com/articles/dataset/5104873) | Patent reactions | 1.8 M reactions | Literature-mined | RXN/SMILES | CC BY 4.0 | Open |
| [MolTextNet](https://huggingface.co/datasets/liuganghuggingface/moltextnet) | Small molecules with text | 2.5M molecule-text pairs | LLM Training | HuggingFace Dataset | Open | Open |
| [MolOpt-Instructions](https://huggingface.co/datasets/blazerye/MolOpt-Instructions) | Molecule optimization | 1.18M instruction-based optimization tasks | LLM Training | HuggingFace Dataset | Open | Open |
| [TextEdge](https://drive.google.com/drive/folders/1YCDBzwjwNRIc1FRkB662G3Y5AOWaokUG?ths=true) | Crystal properties | Crystal text descriptions with properties | LLM Training | JSON | Open | Open |
| [LAMBench-TrainingSet-v1](https://aissquare.com/datasets/detail?pageType=datasets&name=LAMBench-TrainingSet-v1&id=308) | Materials structures | 19.8M structures for Large Atom Models | LLM Training | Various | Open | Open |
| [LLM4Mat](https://drive.google.com/drive/folders/1HpGhuNHG4EQCQMZaKPwEQNH9stJKw-ht?dmr%20=%201%26ec%20=%20wgc-drive-hero-goto) | Materials property prediction | 1.9M crystal structures, 45 properties, 3 modalities | LLM Training | Various | Open | Open |

---

### Literature-mined & Text Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     |
|--------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|
| [PubChem](https://pubchem.ncbi.nlm.nih.gov)                        | Molecules & data        | 119M compounds           | Literature    | SMILES/SDF  | Public Domain | Open    |
| [Open Reaction Database (ORD)](https://open-reaction-database.org)   | Synthetic reactions     | ~1M reactions            | Experimental/Lit | JSON     | CC BY 4.0   | Open       |
| [PatCID (IBM)](https://github.com/DS4SD/PatCID)                   | Chemical image data     | 81M images / 13M mols    | Literature    | PNG/SMILES  | Open        | Open       |
| [MatScholar](https://matscholar.com)                     | NLP corpus (materials)  | 5M+ abstracts            | Literature    | JSON/Graph  | Open        | Open       |
| [MatSciKB](TBD)                            | Materials science KB    | 38.5k entries (20k papers, 3.6k Wikipedia, 1.9k textbooks, 10.5k datasets) | Literature    | Structured text  | Open        | Open       |

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
* Add StarryData2: [https://github.com/starrydata/starrydata_datasets](Dataset Link)
* Add all OpenQDC datasets https://www.openqdc.io/datasets
* Classify and add [CRIPT](https://www.criptapp.org) for polymer data
* A dataset on solubilities of gases in polymers (15 000 experimental measurements of 79 gases' uptakes (0.01–50 wt%) in 102 different polymers, pressures from 1 × 10−3 to 7 × 102 bar and temperatures from 233 to 508 K, includes nearly 500 solvent–polymer systems). Optimized structures of various repeating units are included. Should it be of interest for you, it is available here: [Data](https://github.com/Shorku/rhnet/tree/main/data)
* Add [Materials Cloud Datasets](https://www.materialscloud.org/discover/menu)
* Classify [Atomly](https://atomly.net/#/). A bit challenging with non-English
* Look into adding NOMAD for experimental data as well
* Review [Alexandria Materials](https://alexandria.icams.rub.de)
* Add A Quantum-Chemical Bonding Database for Solid-State Materials Part 1: https://zenodo.org/records/8091844 Part 2: https://zenodo.org/records/8092187
* Add QM datasets. http://quantum-machine.org/datasets/
* Find link for | ChemRxivQuest | Chemistry literature QA | 970 curated QA pairs | LLM Training | JSON | CC BY 4.0 | Open | [ChemRxivQuest](https://arxiv.org/abs/2505.05232) |
* Find new link for USPTO-Reactions | [USPTO Reactions]()                | Organic reactions       | 1.8M reactions           | Literature    | RXN/SMILES  | Open        | Open       |

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

## Changelog

### 2024 and Earlier
For changes made before today, please see the [repository commit history](https://github.com/blaiszik/awesome-matchem-datasets/commits/main/).

### June 2025

Added 28 new high-quality datasets spanning polymer science, drug discovery, carbon materials, spectroscopy, MOF databases, foundation model training, and materials knowledge bases:

#### 🧮 Computational Datasets (15 datasets)
- **NeurIPS Open Polymer Prediction 2025**: Kaggle competition dataset for predicting 5 key polymer properties (Tg, FFV, Tc, density, Rg) from SMILES structures using MD simulation ground truth. Includes ~1,500 test polymers.
- **Carbon Data**: 22.9 million atom dataset with synthetic energy labels from C-GAP-17 potential, featuring 546 carbon trajectories across diverse densities and temperatures. Captures nanotubes, graphitic films, diamond, and amorphous carbon environments.
- **MSR-ACC/TAE25**: Microsoft Research's comprehensive dataset of 76,879 total atomization energies computed at CCSD(T)/CBS level using W1-F12 protocol. Exhaustively covers chemical space for elements up to argon with sub-chemical accuracy (±1 kcal/mol).
- **DFT Solvation Energy Dataset**: 651,290 computed solvation energies for 130,258 molecules from QM9 dataset across 5 solvents (acetone, ethanol, acetonitrile, DMSO, water). Achieves 0.5 kcal/mol MAE for small molecules with accompanying ML models and web interface.
- **MD Simulated Monomer Properties**: GPU-accelerated molecular dynamics dataset of thermodynamic properties for 410 molecules, generated through active learning pipeline. Includes validation against experimental data and automated simulation workflow.
- **Multimodal Spectroscopic Dataset**: Comprehensive spectroscopic dataset with simulated 1H-NMR, 13C-NMR, HSQC-NMR, Infrared, and Mass spectra for 790k molecules from patent reactions. Enables multimodal foundation model development for structure elucidation and functional group prediction.
- **QMugs**: 665k drug-like molecules with ~2M conformers, featuring quantum mechanical properties at both semi-empirical (GFN2-xTB) and DFT (ωB97X-D/def2-SVP) levels.
- **C2DB (Computational 2D Materials Database)**: ~4,000 two-dimensional materials with computed structural, electronic, magnetic, and optical properties.
- **ANI-1x / ANI-1ccx**: 5 million DFT and 500k CCSD(T) calculations for organic molecules, supporting machine learning potential development.
- **CoRE MOF 2019**: 14,763 computation-ready metal-organic frameworks with solvent and charge balancing, suitable for high-throughput screening.
- **QMOF Database**: Comprehensive database of quantum-chemical properties for 20,000+ metal-organic frameworks derived from high-throughput periodic density functional theory calculations.
- **Catalysis-Hub Surface Reactions**: Over 100,000 adsorption and reaction energies on catalytic surfaces, accessible via a Python/GraphQL API.
- **ODAC23 (Open DAC 2023)**: 38 million DFT calculations of CO₂/H₂O adsorption on 8,400 MOFs, aimed at direct-air-capture sorbent discovery.
- **MOFX-DB**: Over 3 million simulated adsorption data points across 160,000 MOFs and 286 zeolites for various gases.
- Enhanced **QCML** dataset entry with more comprehensive description of coverage and properties

#### 🧪 Experimental Datasets (5 datasets)
- **SAIR (Structurally Augmented IC50 Repository)**: Largest public protein–ligand binding dataset with over 1 million complexes and 5.2 million cofolded 3D structures (2.5TB total). Combines experimental binding affinities from ChEMBL/BindingDB with Boltz-1x predicted structures.
- **CoRE MOF 2024**: Updated database of over 40,000 experimentally reported metal-organic frameworks from literature through early 2024. Includes pre-computed material properties for high-throughput material-process screening and carbon-capture applications.
- **HTEM-DB (High-Throughput Experimental Materials Database)**: More than 140,000 composition–process–property data points from combinatorial sputtering experiments, with optical, electrical, and structural measurements.
- **OCx24 (Open Catalyst Experiments 2024)**: 572 synthesized catalyst inks evaluated with matched XRF/XRD and DFT adsorption energies, bridging the gap between simulation and laboratory data.
- **Khazana / Polymer Genome**: Approximately 20,000 polymers with DFT-calculated properties and experimental dielectric data, supporting machine learning on soft materials.

#### 📚 LLM Training Datasets (5 datasets)
- **MolTextNet**: 2.5 million high-quality molecule-text pairs from ChEMBL35, featuring GPT-4o-mini generated descriptions 10x longer than existing datasets. Integrates structural features, computed properties, bioactivity data, and synthetic complexity for multimodal molecular modeling.
- **MolOpt-Instructions**: 1.18 million instruction-based molecule optimization tasks for fine-tuning LLMs on drug discovery. Supports interactive human-machine dialogue for molecule optimization through the DrugAssist framework, enabling expert feedback integration and iterative refinement.
- **TextEdge**: Benchmark dataset for predicting crystal properties from natural language text descriptions. Demonstrates superior performance of LLM-based approaches over traditional GNN methods, with improvements of 8% on band gap prediction and 65% on unit cell volume prediction.
- **LAMBench-TrainingSet-v1**: Massive training dataset for Large Atom Models (LAMs) containing 19.8 million valid structures from the OpenLAM Initiative. Includes 1 million structures on the convex hull for advancing generative modeling and materials science applications.
- **LLM4Mat**: Comprehensive benchmark dataset for evaluating LLMs in materials property prediction, containing 1.9M crystal structures from 10 data sources with 45 distinct properties. Features three input modalities (crystal composition, CIF, text description) with 4.7M, 615.5M, and 3.1B tokens respectively.

#### 📖 Literature-mined & Text Datasets (3 datasets)
- **MatSciKB**: Comprehensive materials science knowledge base with 38,469 curated entries across 16 categories. Integrates ArXiv papers (20,384), Wikipedia articles (3,620), textbooks (1,930), datasets (10,473), formulas (57), and GPT-generated examples (2,005) with efficient CRUD operations for research applications.
- **ChemRxivQuest**: 970 curated question–answer pairs spanning 17 chemistry subfields, designed for retrieval-augmented generation and factuality assessments.
- **USPTO-Lowe Reactions (1976–2016)**: 1.8 million atom-mapped reactions extracted from US patents, serving as a benchmark for reaction prediction and retrosynthesis models.

⸻
