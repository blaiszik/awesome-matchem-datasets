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
  - [Physics & Engineering (PDE, CFD)](#physics--engineering-pde-cfd-datasets)
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
| [BOOM: Benchmarks for Out-Of-distribution Molecules](https://github.com/FLASK-LLNL/BOOM) | Small molecules | 10 Out-Of-Distribution Tasks (1M+ entries) | Computational | CSV | Apache 2.0 | Open |
| [MSR-ACC/TAE25](https://doi.org/10.5281/zenodo.15387279) | Small molecules | 77k CCSD(T)/CBS atomization energies | Computational | JSON | CDLA 2.0 | Open |
| [OMat24 (Meta)](https://huggingface.co/datasets/fairchem/OMAT24)                  | Inorganic crystals      | 110M DFT entries         | Computational | JSON/HDF5   | CC BY 4.0   | Open       |
| [OMol25 (Meta)](https://huggingface.co/facebook/OMol25)                  | Molecular chemistry     | 100M+ DFT calculations   | Computational | LMDB        | CC BY 4.0   | Open       |
| [OMC25](https://huggingface.co/facebook/OMC25) | Molecular crystals | >27M structures | Computational | Zarr | CC BY-NC 4.0 | Open |
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
| [PubChemQCR](https://huggingface.co/datasets/divelab/PubChemQCR) | Small molecules (relaxation) | 3.5M trajectories / 300M conformations | Computational | HuggingFace Dataset | Apache-2.0 | Open |
| [MP-ALOE](https://figshare.com/articles/dataset/MP-ALOE_An_r2SCAN_dataset_for_universal_machine_learning_interatomic_potentials/29452190) | Universal MLIPs (89 elements) | ~1M r2SCAN DFT calculations | Computational | JSONL/MACE | Open | Open |
| [Alexandria DB](https://alexandria.icams.rub.de) | Inorganic (1D–3D) | >5 M DFT calcs (PBE) | Computational | JSON/OPTIMADE/LMDB | Open | Open |
| [Quantum‑Chemical Bonding DB (LOBSTER)](https://zenodo.org/records/8091844) | Solid‑state bonding analysis | 1,520 compounds | Computational | JSON | CC BY 4.0 | Open |
| [MultixcQM9 (OpenQDC)](https://www.openqdc.io/datasets) | Small molecules (QM9, multi‑XC) | 133k molecules | Computational | Torch/NumPy | Open | Open |
| [SPICE (OpenQDC)](https://www.openqdc.io/datasets) | Drug‑like molecules | 1 M conformers (energies & forces) | Computational | Torch/ASE | Open | Open |
| [Matbench v0.1](https://matbench.materialsproject.org/) | Benchmarks (13 tasks) | 10 datasets | Benchmark/Comp | CSV/HDF5 | BSD‑3 | Open |
| [Matbench Discovery](https://matbench-discovery.materialsproject.org/data) | Stability, κ, structures | Multiple files | Benchmark/Comp | CSV/ZIP | BSD‑3 | Open |
| [Materials Cloud Archives](https://archive.materialscloud.org) | Various DFT/MD workflows | 1,000+ datasets | Computational | HDF5/JSON/CIF | Various CC | Open |
| [MS25](https://zenodo.org/records/10901820) | MLIP benchmark (6 material systems) | Multi-system benchmark suite | Computational/Benchmark | HDF5 | Open | Open |
| [RadonPy Polymer Properties Data](https://github.com/RadonPy/RadonPy/blob/648c9a492808339c9bb7ad2c1137e5a7b07614ca/data/PI1070.csv) | Polymer | ~1070 MD-calculated Properties | Computational | CSV | BSD-3 | Open |
| [SHNITSEL Data](https://doi.org/10.5281/zenodo.15482819) | Organic Molecules | 418,870 Post-HF-calculated Ground- and Excited-states Properties | Computational | XARRAY | CC BY 4.0 | Open |
| [Frustrated Lewis Pairs Database](https://jingyun-ye.github.io/FLPDB/) | Small Molecules | 146 Metal-free FLPs | Computational | HTML | Open | Open |
| [AQCat25](https://huggingface.co/datasets/SandboxAQ/aqcat25) | Catalysis | 11.1M frames / 5K materials | Computational | Parquet/ASE DB | | Open |
| [OMol25 Electronic Structures](https://github.com/facebookresearch/fairchem/blob/main/docs/molecules/datasets/omol25_elec.md) | Molecular chemistry | 4M+ calculations | Computational | Raw DFT outputs | | Open |
| [Unrestricted CCSD(T) Dataset For Organic Molecule Reactions](https://figshare.com/articles/dataset/Unrestricted_CCSD_T_Dataset_For_Organic_Molecule_Reactions/30267877?file=58465231) | Organic reactions | 3119 configurations | Computational | | CC BY 4.0 | Open |
| [MC-PDFT-OPESf](https://github.com/Ferg-Lab/PDFT_OPESf) | Reaction kinetics | Diels-Alder reaction | Computational | | | Open |
| [Quantum Cluster Database](https://muellergroup.jhu.edu/qcd/) | Nanoclusters | 63,015 clusters | Computational | CSV/JSON | CC BY 4.0 | Open |

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
| [SAIR](https://pub.sandboxaq.com/data/ic50-dataset) | Protein-ligand binding | 1M+ complexes, 5.2M structures, 2.5TB | Experimental | 3D/CSV | CC BY-NC-SA 4.0 | Open |
| [Anion Solvation DB](https://doi.org/10.5281/zenodo.13987781) | Anion solvation | ~26k properties | Mixed | CSV | CC BY 4.0 | Open |
| [BigSolDB](https://doi.org/10.5281/zenodo.6809668) | Organic molecule solubility | ~54k exp. values | Experimental | CSV | CC BY 4.0 | Open |
| [StarryData2](https://github.com/starrydata/starrydata_datasets) | Experimental properties | Figshare dump (2023/2024) | Experimental | CSV/JSON | CC BY 4.0 | Open |
| [CRIPT Polymer Data](https://www.criptapp.org) | Polymers (synthesis, properties) | Growing community DB | Mixed | JSON/API | CC BY 4.0 | Open |
| [Catechol Benchmark](https://www.kaggle.com/datasets/aichemy/catechol-benchmark) | Solvent selection / Reaction yield | 1200+ process conditions | Experimental | CSV | CC BY-SA 4.0 | Open |
| [Leeds Solubility Data](https://doi.org/10.5281/zenodo.3686213) | Solubility | 2.3k measurements | Experimental | CSV | CC BY 4.0 | Open |
| [BigSolDB 2.0](https://doi.org/10.5281/zenodo.15094979) | Solubility | 103k+ values | Experimental | CSV/XLSX | CC BY 4.0 | Open |


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
| [MaCBench](https://macbench.lamalab.org) | Chemistry and materials science | Vision-language tasks | LLM Training | JSON | Open | Open |
| [ChemBench](https://chembench.lamalab.org) | Chemistry | 2,700+ question-answer pairs | LLM Training | JSON | Open | Open |
| [MatText](https://huggingface.co/datasets/n0w0f/MatText) | Materials property prediction | 2M structures | LLM Training | HuggingFace Dataset | Open | Open |
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
| [LLM-EO](https://github.com/deepprinciple/llmeo) | Transition metal complexes / Optimization | 1.37M TMC space explored | LLM Training | GitHub | Apache-2.0 | Open |
| [Flavor Analysis and Recognition Transformer](https://github.com/fart-lab/fart/tree/main/dataset) | Molecular taste prediction | Multi-class taste classification dataset | LLM Training | SMILES/JSON | Open | Open |
| [SCQA (Solar Cell QA)](https://huggingface.co/collections/CambridgeMolecularEngineering/solar-cell-qa-datasets-67b398f1b9c0f0dd7600a159) | Solar cells | 47K QA pairs | LLM Training | JSON | Open | Open |
| [ScienceQA](https://scienceqa.github.io/) | K–12 science, multimodal MCQs w/ lectures & explanations | 21,208 Qs | LLM Training/Eval | JSON | MIT | Open |
| [SciBench](https://scibench-ucla.github.io) | College-level scientific problem solving (math/chem/phys) | Open & closed sets | LLM Eval | PDF/JSON | Open | Open |
| [MegaScience](https://huggingface.co/MegaScience) | Scientific reasoning (7 disciplines) | 1.25M instances (650k reasoning questions from 12k textbooks) | LLM Training | HuggingFace Dataset | Open | Open |

---

### Literature-mined & Text Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     |
|--------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|
| [PubChem](https://pubchem.ncbi.nlm.nih.gov)                        | Molecules & data        | 119M compounds           | Literature    | SMILES/SDF  | Public Domain | Open    |
| [Open Reaction Database (ORD)](https://open-reaction-database.org)   | Synthetic reactions     | ~1M reactions            | Experimental/Lit | JSON     | CC BY 4.0   | Open       |
| [PatCID (IBM)](https://github.com/DS4SD/PatCID)                   | Chemical image data     | 81M images / 13M mols    | Literature    | PNG/SMILES  | Open        | Open       |
| [MatScholar](https://matscholar.com)                     | NLP corpus (materials)  | 5M+ abstracts            | Literature    | JSON/Graph  | Open        | Open       |
| [Matbench (metadata/text tasks)](https://matbench.materialsproject.org/) | Text/meta ML tasks | 13 tasks | Literature/Benchmark | CSV | BSD‑3 | Open |
| [OpenQDC Hub](https://github.com/valence-labs/openQDC) | QM molecules & reactions | 1.5 B geometries | Literature/Computational | Python API/NPZ | MIT | Open |

---

### 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets

| Dataset                         | Domain                  | Size                     | Type         | Format      | License     | Access     |
|---------------------------------|-------------------------|--------------------------|--------------|-------------|-------------|------------|
| [PDEBench](https://github.com/pdebench/PDEBench) | PDE solving / Scientific ML | Multiple datasets | Benchmark / Simulation | HDF5/PyTorch | Apache-2.0 | Open |
| [BLASTNet](https://blastnet.github.io) | Fluid mechanics / Reacting flows | 17 TB | Simulation / CFD | HDF5/NPY | Open | Open |
| [Johns Hopkins Turbulence DB (JHTDB)](https://turbulence.pha.jhu.edu) | DNS/LES turbulence (9 canonical flows) | ≈ 350 TB | Simulation | Web API / HDF5 cutouts | Public Domain | Open |
| [Airfoil CFD 2k](https://data.openei.org/submissions/5970) | 1,830 airfoils × 25 AoA × 3 Re | ~6 GB (250 k cases) | Simulation | HDF5 | CC BY 4.0 | Open |
| [PDEArena (collection)](https://huggingface.co/pdearena) | 2-D Navier–Stokes, Shallow-Water, 3-D Maxwell | ≈ 100 GB (4 datasets) | Simulation | Torch / HDF5 | MIT | Open |
| [WeatherBench 2](https://github.com/pangeo-data/WeatherBench) | Global weather reanalysis (ERA5, 1979-2023) | ≈ 5 TB | Reanalysis | NetCDF/Zarr | MIT | Open |
| [UT Austin Channel-DNS Suite](https://turbulence.oden.utexas.edu) | Incompressible channel flow Re<sub>τ</sub> 180 – 5200 | ≈ 10 TB | Simulation | Binary / ASCII | Research-Free | Open |
| [Compressible TPC DNS DB](https://data.mendeley.com/datasets/wt8t5kxzbs) | Compressible channel flow (25 M, Re<sub>τ*</sub>) | ~2 GB | Simulation | TXT tables | CC BY 4.0 | Open |
| [Curated RANS ↔ DNS Dataset](https://doi.org/10.34740/kaggle/dsv/2637500) | 29 geometries, 4 RANS models w/ DNS/LES labels | 1.1 GB | Simulation | HDF5/CSV | CC BY 4.0 | Open |
| [NASA Common Research Model (CRM)](https://commonresearchmodel.larc.nasa.gov) | Aircraft CRM geom. + wind-tunnel & CFD results | Multi-GB | Mixed (Exp + Sim) | CAD / CSV / Tecplot | NASA PDL | Open |
| [Darcy-Flow (FNO)](https://github.com/neuraloperator/neuraloperator) | 2-D porous-media pressure fields (∇·k∇u = f) | ≈ 1 GB (10 k samples) | Simulation | HDF5 | Apache-2.0 | Open |
| [HiFi-TURB LES/DNS](https://cordis.europa.eu/project/id/814837) | High-fidelity LES/DNS for complex 3D flows | Multi-case suite | Simulation (DNS/LES) | HDF5/NetCDF | Open | Open |
| [NASA High Lift Prediction Workshop (HLPW)](https://hiliftpw.larc.nasa.gov/) | High-lift aircraft configurations | Multi-GB | Mixed (exp + CFD) | CAD/CSV/Tecplot | NASA PDL | Open |
| [High-Speed TBL DNS DB](https://arc.aiaa.org/doi/10.2514/1.J063456) | Compressible turbulent boundary layers | DNS database | Simulation | HDF5 | Open | Access w/ paper |
| [ML Turbulence (Kaggle)](https://www.kaggle.com/datasets/ryleymcconkey/ml-turbulence-dataset) | RANS Reynolds stress tensor data | ~GB scale | Benchmark/Simulation | CSV/HDF5 | CC BY 4.0 | Open |

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
* Add all OpenQDC datasets https://www.openqdc.io/datasets
* A dataset on solubilities of gases in polymers (15 000 experimental measurements of 79 gases' uptakes (0.01–50 wt%) in 102 different polymers, pressures from 1 × 10−3 to 7 × 102 bar and temperatures from 233 to 508 K, includes nearly 500 solvent–polymer systems). Optimized structures of various repeating units are included. Should it be of interest for you, it is available here: [Data](https://github.com/Shorku/rhnet/tree/main/data)
* Add [Materials Cloud Datasets](https://www.materialscloud.org/discover/menu)
* Classify [Atomly](https://atomly.net/#/). A bit challenging with non-English
* Look into adding NOMAD for experimental data as well
* Add A Quantum-Chemical Bonding Database for Solid-State Materials Part 1: https://zenodo.org/records/8091844 Part 2: https://zenodo.org/records/8092187
* Add QM datasets. http://quantum-machine.org/datasets/
* Find link for | ChemRxivQuest | Chemistry literature QA | 970 curated QA pairs | LLM Training | JSON | CC BY 4.0 | Open | [ChemRxivQuest](https://arxiv.org/abs/2505.05232) |
* Find new link for USPTO-Reactions | [USPTO Reactions]()                | Organic reactions       | 1.8M reactions           | Literature    | RXN/SMILES  | Open        | Open       |
* Find dataset link for | [SciCUEval](https://arxiv.org/abs/2505.15094) | Multidomain scientific comprehension (bio/chem/phys/matsci) | 10 sub-datasets | LLM Eval | JSON/PDF | Open | Open |
* Find dataset for | [MatSciKB](TBD)                            | Materials science KB    | 38.5k entries (20k papers, 3.6k Wikipedia, 1.9k textbooks, 10.5k datasets) | Literature    | Structured text  | Open        | Open       |


---

### Other Links
* [Awesome Materials Informatics](https://github.com/tilde-lab/awesome-materials-informatics)

---

## License

This project is licensed under the **MIT License**. Each dataset listed has its **own license**, noted in the table. Always check the source's license before using the data in your project.

---

## Acknowledgements

The primary effort of Ben Blaiszik on this project was performed under financial assistance award 70NANB24H049 / MML24-1001 from the National Institute of Standards and Technology (NIST).


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
This Changelog is autogenerated, there may be errors.

### October 2025

Added 7 new datasets focusing on catalysis, reaction kinetics, and experimental solubility to enhance resources for computational chemistry and machine learning applications.

#### 🧮 Computational Datasets (4 datasets)
- **AQCat25**: This dataset provides a large and diverse collection of DFT calculation trajectories for heterogeneous catalysis research. It encompasses a wide range of adsorbates and catalyst surfaces. The data is designed for training and testing machine learning interatomic potentials. AQCat25 consists of approximately 5K materials, 40K intermediate-catalyst systems, and 11.1M frames.
- **OMol25 Electronic Structures Dataset**: The OMol25 Electronic Structures dataset includes the raw DFT outputs, electronic densities, wavefunctions, and molecular orbital information for over 4M million high-accuracy quantum chemical calculations. We see this as a transformative opportunity to develop higher quality partial charges, partial spins, and advanced electronic features to unlock the next generation of physics-informed ML models.
- **Unrestricted CCSD(T) Dataset For Organic Molecule Reactions**: Dataset of 3119 organic molecule configurations at gold-standard quantum accuracy with automated workflows for unrestricted CCSD(T) calculations. Includes a transferable MLIP trained on UCCSD(T) data, showing significant improvements in force and activation energy accuracy.
- **MC-PDFT-OPESf**: This work combines multi-configuration pair-density functional theory (MC-PDFT) as an accurate and eﬃcient multireference electronic structure method with on-the-fly probability enhanced sampling flooding (OPESf) as an enhanced sampling method capable of accelerating reactive transitions. MC-PDFT–OPESf provides reaction rates in agreement with experiments at a fraction of the computational cost required by conventional unbiased ab-initio calculations.

#### 🧪 Experimental Datasets (3 datasets)
- **Catechol Benchmark**: Time-series Solvent Selection Data for Few-shot Machine Learning, providing the first-ever transient flow dataset for machine learning benchmarking, covering over 1200 process conditions. This dataset focuses on solvent selection, a task that is particularly difficult to model theoretically.
- **BNNLab/Solubility_data: Leeds Solubility Data**: Curated solubility data in organic solvents and water and descriptors for solubility prediction.
- **BigSolDB 2.0**: A comprehensive dataset of 103,944 experimentally measured solubility values of 1,448 organic compounds in 213 solvents reported in 1,595 literature peer-reviewed articles.

### August 2025

Enhanced scientific reasoning capabilities and machine learning interatomic potential benchmarking with 6 new high-quality datasets for AI scientists and materials researchers.

#### 🧮 Computational Datasets (3 datasets)
- **OMC25**: A collection of over 27 million molecular crystal structures containing 12 elements and up to 300 atoms in the unit cell. The dataset was generated from dispersion-inclusive density functional theory (DFT) relaxation trajectories of over 230,000 randomly generated molecular crystal structures of around 50,000 organic molecules.
- **MS25**: Comprehensive benchmark dataset for evaluating machine learning interatomic potentials (MLIPs) across 6 diverse materials systems including MgO surfaces, liquid water, zeolites, catalytic Pt surface reactions, high-entropy alloys, and disordered Zr-oxides. Evaluates 5 MLIP architectures (MACE, NequIP, Allegro, MTP, Torch-ANI) with focus on derived physical observables beyond traditional energy/force metrics. Demonstrates that equivariant MLIPs offer 1.5-2× improvements over nonequivariant models in complex systems, while highlighting the importance of explicit validation of physical properties rather than relying solely on error metrics.
- Added the * Frustrated Lewis Pairs Database ** of 146 Metal-free FLPs


#### 📚 LLM Training Datasets (4 datasets)
- **MaCBench**: A comprehensive benchmark for evaluating how vision-language models handle real-world chemistry and materials science tasks across three core aspects: data extraction, experimental understanding, and results interpretation. Reveals fundamental limitations in spatial reasoning and cross-modal information synthesis in leading models.
- **ChemBench**: A cutting-edge framework to evaluate the chemical knowledge and reasoning capabilities of large language models (LLMs). It includes over 2,700 curated question-answer pairs across diverse chemistry topics and uniquely encodes chemical semantics, enabling models to process and reason about molecules and equations.
- **MatText**: A comprehensive benchmarking framework spanning multiple representations and model scales, which finds that LLMs consistently fail to capture coordinate information while excelling at category patterns. This geometric blindness persists regardless of model size, dataset scale, or text representation strategy.
- **MegaScience**: Large-scale scientific reasoning dataset featuring 1.25 million high-quality instances across 7 scientific disciplines. Includes TextbookReasoning component with 650k reasoning questions extracted from 12,000 university-level textbooks, providing truthful reference answers for training AI scientists. Developed through systematic ablation studies and comprehensive evaluation across 15 benchmarks, demonstrating superior performance and training efficiency compared to existing open-source scientific datasets.

### July 2025

Expanded the collection into new scientific domains with 31 new datasets, introducing benchmarks for physics-based machine learning, adding comprehensive quantum mechanics datasets, expanding materials science resources, and enhancing scientific evaluation benchmarks.

#### 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets (15 datasets)
- **PDEBench**: A comprehensive benchmark suite for scientific machine learning featuring a wide range of Partial Differential Equations. It provides large, ready-to-use datasets for challenging physics problems, supporting both forward and inverse modeling.
- **BLASTNet**: A 17 TB collection of high-fidelity fluid mechanics simulation datasets for ML applications in automotive, propulsion, and energy sectors. It includes code and pre-trained models for tasks like turbulence modeling and spatio-temporal prediction.
- **JHTDB**: multi-terabyte DNS/LES portal with isotropic, channel, MHD, boundary-layer and atmospheric datasets.
- **Airfoil CFD 2k**: DOE/NREL benchmark: 1,830 shapes × 250 k RANS simulations; HDF5 + AWS mirror.
- **PDEArena**: Hugging-Face org offering Navier–Stokes, Shallow-Water & Maxwell tensors; MIT license.
- **WeatherBench 2**: ERA5-derived Zarr cubes for data-driven medium-range forecasting; MIT.
- **UT Austin DNS Suite**: public HTTP server with Reτ 180–5200 channel data & statistics.
- **Compressible TPC DNS DB**: 25 Reynolds–Mach cases, plain-text statistics (Mendeley Data).
- **Curated RANS ↔ DNS**: Scientific Data descriptor + Kaggle mirror for ML turbulence closures.
- **NASA CRM**: open CAD, grids, wind-tunnel Cp & force/moment datasets for the community benchmark.
- **Darcy Flow (FNO)**: canonical permeability→pressure dataset used in FNO/PINO papers.
- **HiFi-TURB LES/DNS**: EU-funded project providing high-fidelity Large Eddy Simulation and Direct Numerical Simulation datasets for complex 3D turbulent flows, supporting advanced turbulence modeling and AI/ML applications in computational fluid dynamics.
- **NASA High Lift Prediction Workshop (HLPW)**: Multi-phase workshop datasets featuring high-lift aircraft configurations with comprehensive experimental validation data, CAD geometries, and CFD solutions for aerodynamic modeling and validation.
- **High-Speed TBL DNS DB**: Specialized database of Direct Numerical Simulation data for compressible turbulent boundary layers, providing detailed flow field information for high-speed aerodynamic applications and turbulence model development.
- **ML Turbulence (Kaggle)**: Community-contributed dataset featuring RANS Reynolds stress tensor data with ground truth labels, providing a standardized benchmark for machine learning approaches to turbulence modeling.


#### 🧮 Computational Datasets (7 datasets)
- **PubChemQCR**: A massive dataset of molecular relaxation trajectories for ~3.5 million small molecules, containing over 300 million conformations with energy and force labels. It is the largest public dataset of its kind, designed to accelerate the development of machine learning interatomic potentials (MLIPs).
- **MP-ALOE**: Nearly 1 million DFT calculations using the accurate r2SCAN meta-generalized gradient approximation, covering 89 elements. Created using active learning and primarily consisting of off-equilibrium structures, MP-ALOE is designed for training universal machine learning interatomic potentials (UMLIPs) with strong performance on thermochemical properties, force prediction, and physical soundness under extreme conditions.
- **Alexandria DB**: Massive computational materials database containing over 5 million DFT calculations using PBE functional for 1D-3D inorganic materials. Provides OPTIMADE-compliant API access and LMDB format for high-performance materials screening and property prediction workflows.
- **Quantum-Chemical Bonding DB (LOBSTER)**: Specialized dataset providing detailed bonding analysis for 1,520 solid-state compounds using LOBSTER methodology. Enables understanding of chemical bonding in crystalline materials through projected crystal orbital Hamilton populations and related descriptors.
- **MultixcQM9 & SPICE (OpenQDC)**: Enhanced quantum chemistry datasets within the OpenQDC framework. MultixcQM9 provides multi-exchange correlation functional data for 133k small molecules, while SPICE offers 1 million conformers with energies and forces for drug-like molecules, both optimized for machine learning applications.
- **Matbench v0.1 & Discovery**: Comprehensive benchmarking suites for materials property prediction featuring 13 standardized tasks across 10 datasets. Matbench Discovery specifically targets stability prediction, thermal conductivity, and structure generation with rigorous evaluation protocols.
- **Materials Cloud Archives**: Centralized repository of over 1,000 computational datasets from various DFT and molecular dynamics workflows. Provides standardized access to diverse materials science calculations with comprehensive metadata and version control.

#### 📚 LLM Training Datasets (5 datasets)
- **LLM-EO (Evolutionary Optimization)**: A framework that integrates LLMs into evolutionary algorithms for optimizing transition metal complexes. This approach leverages the chemical knowledge of LLMs to surpass traditional genetic algorithms, enabling flexible, multi-objective optimization without complex mathematical formulations.
- **Flavor Analysis and Recognition Transformer**: A state-of-the-art machine learning model dataset for predicting molecular taste from chemical structures. Built on ChemBERTa transformer architecture, it classifies molecules across four taste categories (sweet, bitter, sour, umami) with >91% accuracy, enabling interpretability through gradient-based visualizations and applications in flavor compound discovery and rational food design.
- **SCQA (Solar Cell QA)**: Domain-specific question-answering dataset containing 47,268 QA pairs about solar cell properties, auto-generated using ChemDataExtractor. Fine-tuning language models on this dataset achieves F1-scores exceeding general-English QA datasets by 10-20%, demonstrating the value of domain-specific training data for specialized scientific applications.
- **ScienceQA**: Comprehensive K-12 science education dataset with 21,208 multimodal multiple-choice questions including lectures and explanations. Supports development of educational AI systems and scientific reasoning capabilities in language models.
- **SciBench**: College-level scientific problem-solving benchmark covering mathematics, chemistry, and physics with both open and closed evaluation sets. Enables systematic assessment of LLM performance on advanced scientific reasoning tasks.

#### 🧪 Experimental Datasets (4 datasets)
- **Anion Solvation DB**: Comprehensive compilation of 26,000+ solvation properties including 8,241 experimental pKa values across 8 solvents, 5,536 computed gas-phase acidities, and over 12,000 solvation energies for anions and neutral compounds computed using COSMO-RS. Bridges experimental and computational approaches for understanding anion behavior in different solvation environments.
- **BigSolDB**: Extensive experimental solubility database containing 54,273 measured solubility values across temperature range 243.15-403.15 K in various organic solvents and water. Features diverse chemical space coverage with interactive t-SNE exploration tool and comprehensive statistical analysis for QSPR model development.
- **StarryData2**: Large-scale experimental properties dataset from Figshare spanning 2023-2024, providing comprehensive experimental measurements across diverse materials and chemical systems for machine learning model validation and training.
- **CRIPT Polymer Data**: Community-driven polymer database featuring synthesis procedures, characterization data, and properties. Enables standardized data sharing and collaborative research in polymer science through structured JSON API access.


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

#### 📚 Enhanced Literature & Benchmark Resources (2 datasets)
- **Matbench (metadata/text tasks)**: Extended benchmarking suite providing 13 standardized tasks for text-based and metadata-driven materials property prediction. Enables systematic evaluation of natural language processing approaches in materials science applications.
- **OpenQDC Hub**: Comprehensive quantum chemistry database aggregating 1.5 billion molecular geometries and quantum mechanical properties. Provides unified Python API access to diverse quantum chemistry datasets with standardized formats for large-scale machine learning applications.

⸻

### Earlier Updates
For changes made earlier than the changelog entries, please see the [repository commit history](https://github.com/your-repo/commits).

