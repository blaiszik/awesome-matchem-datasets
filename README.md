# Awesome Materials & Chemistry Datasets

## About

A curated list of the most useful datasets in **materials science** and **chemistry** for training **machine learning** and **AI foundation models**. This includes experimental, computational, and literature-mined datasets—prioritizing **open-access** resources and community contributions.

This project aims to:
- Catalog the best datasets by domain, type, quality, and size
- Support reproducible research in AI for chemistry and materials
- Provide a community-driven resource with contributions from researchers and developers

---

## Table of Contents

- [About](#about)
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

| Dataset | Domain | Size | Type | Format |
| -------------------------------- | ------------------------- | -------------------------- | -------------- | ------------- |
| [BOOM: Benchmarks for Out-Of-distribution Molecules](https://github.com/FLASK-LLNL/BOOM) | Small molecules | 10 Out-Of-Distribution Tasks (1M+ entries) | Computational | CSV |
| [MSR-ACC/TAE25](https://doi.org/10.5281/zenodo.15387279) | Small molecules | 77k CCSD(T)/CBS atomization energies | Computational | JSON |
| [OMat24 (Meta)](https://huggingface.co/datasets/fairchem/OMAT24) | Inorganic crystals | 110M DFT entries | Computational | JSON/HDF5 |
| [OMol25 (Meta)](https://huggingface.co/facebook/OMol25) | Molecular chemistry | 100M+ DFT calculations | Computational | LMDB |
| [OMC25](https://huggingface.co/facebook/OMC25) | Molecular crystals | >27M structures | Computational | Zarr |
| [Materials Project (LBL)](https://materialsproject.org) | Inorganic crystals | 500k+ compounds | Computational | JSON/API |
| [Open Catalyst 2020 (OC20)](https://opencatalystproject.org) | Catalysis (surfaces) | 1.2M relaxations | Computational | JSON/HDF5 |
| [AFLOW](https://aflow.org) | Inorganic materials | 3.5M materials | Computational | REST API |
| [OQMD](https://oqmd.org) | Inorganic solids | 1M+ compounds | Computational | SQL/CSV |
| [JARVIS-DFT (NIST)](https://jarvis.nist.gov) | 3D/2D materials | 40k+ entries | Computational | JSON/API |
| [Carolina Materials DB](http://www.carolinamatdb.org) | Hypothetical crystals | 214k structures | Computational | JSON |
| [NOMAD](https://nomad-lab.eu/prod/v1/gui/search/entries/search/entries) | Various DFT/MD | >19M calculations | Computational | JSON |
| [MatPES](https://matpes.ai) | DFT Potential Energy Surfaces | ~400,000 structures from 300K MD simulations | Computational | JSON |
| [Vector-QM24](https://doi.org/10.5281/zenodo.11164951) | Small organic and inorganic molecules | 836k conformational isomers | Computational | JSON |
| [AIMNet2 Dataset](https://doi.org/10.1184/R1/27629937.v1) | Non-metallic compounds | 20M hybrid DFT calculations | Computational | JSON |
| [RDB7](https://zenodo.org/records/13328872) | Barrier height and enthalpy for small organic reactions | 12k CCSD(T)-F12 calculations | Computational | CSV |
| [RDB19-Rad](https://zenodo.org/records/11493786) | ΔG of activation and of reaction for organic reactions in 40 common solvents | 5.6k DFT + COSMO-RS calculations | Computational | CSV |
| [QCML](https://zenodo.org/records/14859804) | Small molecules consisting of up to 8 heavy atoms | 14.7B Semi-empirical + 33.5M DFT calculations | Computational | TFDS |
| [QM9](http://quantum-machine.org/datasets/) | Small organic molecules | 134k molecules with quantum properties | Computational | SDF/CSV |
| [QM7/QM7b](http://quantum-machine.org/datasets/) | Small molecules | 7k molecules with atomization energies | Experimental | SDF/CSV |
| [QMugs](https://www.openqdc.io/datasets/qmugs) | Drug-like molecules | 665 k mol / 2 M conf | Computational | HDF5 |
| [C2DB](https://c2db.fysik.dtu.dk) | 2D materials | ~4 000 entries | Computational | JSON/API |
| [ANI-1x / 1ccx](https://qcawebapps.molssi.org/ml_datasets/) | Small organic mol | 5 M (DFT) + 0.5 M (CCSD) | Computational | HDF5 |
| [CoRE MOF 2019](https://pubs.acs.org/doi/10.1021/acs.jced.9b00835) | Metal-organic frameworks | 14 763 structures | Computational | CIF/JSON |
| [QMOF Database](https://figshare.com/articles/dataset/QMOF_Database/13147324) | Metal-organic frameworks | 20k+ structures (DFT) | Computational | CIF/JSON |
| [Catalysis-Hub](https://www.catalysis-hub.org) | Surface reactions | >100 k energies | Computational | JSON/API |
| [ODAC23](https://fair-chem.github.io/dac/datasets/odac.html) | MOF + CO₂/H₂O adsorption | 38 M DFT calcs | Computational | HDF5 |
| [MOFX-DB](https://doi.org/10.1021/acs.jced.2c00583) | Gas adsorption in MOFs | 3 M isotherm pts | Computational | CSV/HDF5 |
| [LeMat-Bulk](https://huggingface.co/datasets/LeMaterial/LeMat-Bulk) | Inorganic materials (bulk) | 6.7M structures (5.9M materials) | Computational | HuggingFace Dataset |
| [LeMat-Traj](https://huggingface.co/datasets/LeMaterial/LeMat-Traj) | Inorganic materials (trajectories) | 113M structures | Computational | HuggingFace Dataset |
| [NeurIPS Open Polymer Prediction 2025](https://www.kaggle.com/competitions/neurips-open-polymer-prediction-2025/data) | Polymers | ~1,500 test polymers with MD-derived properties | Computational | CSV |
| [Carbon Data](https://github.com/jla-gardner/carbon-data) | Carbon materials | 22.9M atoms, 546 trajectories | Computational | EXTXYZ |
| [MSR-ACC/TAE25](https://zenodo.org/records/15387280) | Small molecules (up to Ar) | 76,879 total atomization energies | Computational | HDF5/CSV |
| [DFT Solvation Energy Dataset](https://www.doi.org/10.18126/jos5-wj65) | Small molecules | 651,290 solvation energies in 5 solvents | Computational | CSV/JSON |
| [MD Simulated Monomer Properties](https://doi.org/10.18126/8p6m-e135) | Small molecules | 410 molecules with thermodynamic properties | Computational | CSV/JSON |
| [Multimodal Spectroscopic Dataset](https://github.com/rxn4chemistry/multimodal-spectroscopic-dataset) | Molecular spectroscopy | 790k molecules with simulated spectra | Computational | HDF5/JSON |
| [PubChemQCR](https://huggingface.co/datasets/divelab/PubChemQCR) | Small molecules (relaxation) | 3.5M trajectories / 300M conformations | Computational | HuggingFace Dataset |
| [MP-ALOE](https://figshare.com/articles/dataset/MP-ALOE_An_r2SCAN_dataset_for_universal_machine_learning_interatomic_potentials/29452190) | Universal MLIPs (89 elements) | ~1M r2SCAN DFT calculations | Computational | JSONL/MACE |
| [Alexandria DB](https://alexandria.icams.rub.de) | Inorganic (1D–3D) | >5 M DFT calcs (PBE) | Computational | JSON/OPTIMADE/LMDB |
| [Quantum‑Chemical Bonding DB (LOBSTER)](https://zenodo.org/records/8091844) | Solid‑state bonding analysis | 1,520 compounds | Computational | JSON |
| [MultixcQM9 (OpenQDC)](https://www.openqdc.io/datasets) | Small molecules (QM9, multi‑XC) | 133k molecules | Computational | Torch/NumPy |
| [SPICE (OpenQDC)](https://www.openqdc.io/datasets) | Drug‑like molecules | 1 M conformers (energies & forces) | Computational | Torch/ASE |
| [Matbench v0.1](https://matbench.materialsproject.org/) | Benchmarks (13 tasks) | 10 datasets | Benchmark/Comp | CSV/HDF5 |
| [Matbench Discovery](https://matbench-discovery.materialsproject.org/data) | Stability, κ, structures | Multiple files | Benchmark/Comp | CSV/ZIP |
| [Materials Cloud Archives](https://archive.materialscloud.org) | Various DFT/MD workflows | 1,000+ datasets | Computational | HDF5/JSON/CIF |
| [MS25](https://zenodo.org/records/10901820) | MLIP benchmark (6 material systems) | Multi-system benchmark suite | Computational/Benchmark | HDF5 |
| [RadonPy Polymer Properties Data](https://github.com/RadonPy/RadonPy/blob/648c9a492808339c9bb7ad2c1137e5a7b07614ca/data/PI1070.csv) | Polymer | ~1070 MD-calculated Properties | Computational | CSV |
| [SHNITSEL Data](https://doi.org/10.5281/zenodo.15482819) | Organic Molecules | 418,870 Post-HF-calculated Ground- and Excited-states Properties | Computational | XARRAY |
| [Frustrated Lewis Pairs Database](https://jingyun-ye.github.io/FLPDB/) | Small Molecules | 146 Metal-free FLPs | Computational | HTML |
| [AQCat25](https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset) | Catalysis | 13.5M frames / 5K materials | Computational | Parquet/ASE DB |
| [OMol25 Electronic Structures](https://github.com/facebookresearch/fairchem/blob/main/docs/molecules/datasets/omol25_elec.md) | Molecular chemistry | 4M+ calculations | Computational | Raw DFT outputs |
| [Unrestricted CCSD(T) Dataset For Organic Molecule Reactions](https://figshare.com/articles/dataset/Unrestricted_CCSD_T_Dataset_For_Organic_Molecule_Reactions/30267877?file=58465231) | Organic reactions | 3119 configurations | Computational |  |
| [MC-PDFT-OPESf](https://github.com/Ferg-Lab/PDFT_OPESf) | Reaction kinetics | Diels-Alder reaction | Computational |  |
| [Quantum Cluster Database](https://muellergroup.jhu.edu/qcd/) | Nanoclusters | 63,015 clusters | Computational | CSV/JSON |
| [The Cambridge Cluster Database](https://www-wales.ch.cam.ac.uk/CCD.html) | Mixed Clusters | Multiple Files | Computational | Multiple Types |
| [Battery Electrolyte Solvation/Ionization](https://doi.org/10.5281/zenodo.15252439) | Organic molecules | Thousands of molecules | Computational | |
| [van der Waals Bilayer Database (BiDB)](https://bidb.fysik.dtu.dk/) | 2D vdW Bilayers | 12,138 entries | Computational | DB | 
| [Van der Waals 2D Heterostructure Database (HetDB)](https://hetdb.fysik.dtu.dk/) | 2D vdW Heterostructures | 336 entries | Computational | DB |
| [Quantum Point Defects Database (QPOD)](https://qpod.fysik.dtu.dk/) | Point Defects in 2D Materials | 24,399 entries | Computational | DB |
| [2D Alloy Database](https://cmrdb.fysik.dtu.dk/2dalloys/)| 2D TMDC Alloys | 400 alloy monolayers | Computational | DB |
| [OC25 (Open Catalyst 2025)](https://huggingface.co/facebook/OC25) | Catalysis (solid–liquid interfaces) | 7.8M DFT calcs / 1.5M solvent environments | Computational | ASE/LMDB |
| [OPoly26 (Open Polymers 2026)](https://huggingface.co/datasets/colabfit/OPoly26-train) | Polymers | 6.57M DFT calcs (2,444 monomers) | Computational | HuggingFace/ASE |
| [MAD (Massive Atomic Diversity)](https://archive.materialscloud.org/records/xdsbt-a3r17) | Universal (organic + inorganic) | 95,595 structures (85 elements) | Computational | EXTXYZ |
| [qcMol](https://structpred.life.tsinghua.edu.cn/qcmol/) | Drug-like molecules, metabolites | 1.2M molecules / 31 QM descriptors | Computational | CSV/JSON |
| [Transition1x](https://doi.org/10.6084/m9.figshare.19614657) | Reaction paths / transition states (organic) | 9.6M DFT energies & forces (~10k NEB paths) | Computational | HDF5 |


---

### Experimental Datasets

| Dataset | Domain | Size | Type | Format |
| --------------------------------- | ------------------------- | -------------------------- | -------------- | ------------- |
| [Crystallography Open Database (COD)](https://www.crystallography.net/cod) | Crystal structures | ~525k entries | Experimental | CIF/SMILES |
| [NIST ICSD (subset)](https://icsd.products.fiz-karlsruhe.de) | Inorganic structures | ~290k structures | Experimental | CIF |
| [CSD (Cambridge)](https://www.ccdc.cam.ac.uk) | Organic crystals | ~1.3M structures | Experimental | CIF |
| [opXRD](https://doi.org/10.5281/zenodo.14254270) | Crystal structures | 92552 (2179 labeled) | Experimental | JSON |
| [MDR SuperCon](https://mdr.nims.go.jp/collections/4c428a0c-d209-4990-ad1f-656d05d1cfe2) | Superconductivity | legacy superconductor database w/ material composition, structure, properties, and processes | Mixed |  |
| [ChEMBL](https://www.ebi.ac.uk/chembl/) | Bioactive molecules | 2.3M+ compounds with bioactivity data | Experimental | JSON/SDF |
| [MoleculeNet](http://moleculenet.org/) | Molecular properties | 700k+ compounds across 17 datasets | Mixed | CSV/SDF |
| [ESOL](http://moleculenet.org/) | Aqueous solubility | 1,128 compounds with solubility data | Experimental | CSV |
| [FreeSolv](https://github.com/MobleyLab/FreeSolv) | Hydration free energy | 643 molecules with experimental data | Experimental | CSV |
| [Lipophilicity](https://www.ebi.ac.uk/chembl/) | Octanol/water distribution | 4,200 compounds with logD values | Experimental | CSV |
| [PCBA](https://pubchem.ncbi.nlm.nih.gov/bioassay) | Bioassay screening | 400k+ compounds, 128 bioassays | Experimental | CSV |
| [HIV](https://wiki.nci.nih.gov/display/NCIDTPdata/AIDS+Antiviral+Screen+Data) | Antiviral screening | 41k compounds with HIV inhibition data | Experimental | CSV |
| [BACE](http://moleculenet.org/) | Beta-secretase inhibitors | 1,522 compounds with IC50 data | Experimental | CSV |
| [BBBP](http://moleculenet.org/) | Blood-brain barrier permeability | 2,053 compounds with permeability data | Experimental | CSV |
| [Tox21](https://tripod.nih.gov/tox21/challenge/) | Toxicity screening | 8k compounds, 12 toxicity targets | Experimental | CSV |
| [ToxCast](https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data) | High-throughput toxicity | 8k compounds, 600+ assays | Experimental | CSV |
| [SIDER](http://sideeffects.embl.de/) | Drug side effects | 1,427 drugs with adverse reactions | Experimental | CSV |
| [ClinTox](http://moleculenet.org/) | Clinical trial toxicity | 1,491 compounds with FDA approval status | Experimental | CSV |
| [PDBbind](http://www.pdbbind.org.cn/) | Protein-ligand binding | 19k complexes with binding affinities | Experimental | PDB/SDF |
| [BindingDB](https://www.bindingdb.org/) | Protein-ligand binding | 2.8M+ binding data points | Experimental | CSV/SDF |
| [ProtBENCH](https://github.com/hevalatas/ProtBENCH) | Drug-target interactions | Protein family-specific datasets | Experimental | CSV |
| [PDBench](https://github.com/wells-wood-research/PDBench) | Protein sequence design | 595 protein structures, 40 architectures | Experimental | PDB |
| [PDB-Struct](https://github.com/WANG-CR/PDB-Struct) | Structure-based protein design | Comprehensive protein design benchmark | Experimental | PDB |
| [HTEM-DB](https://htem.nrel.gov) | Thin-film composition libraries | 140 k+ samples | Experimental | JSON/API |
| [OCx24](https://github.com/facebookresearch/fairchem/tree/main/src/fairchem/applications/ocx/data) | Electrocatalyst inks | 572 samples (+DFT) | Experimental | CSV |
| [Polymer Genome](https://khazana.gatech.edu/dataset/) | Polymers | 20 k polymers | Experimental + Comp | CSV/JSON |
| [CoRE MOF 2024](https://www.ccdc.cam.ac.uk/support-and-resources/downloads/) | Metal-organic frameworks | 40k+ experimental MOFs | Experimental | CIF |
| [SAIR](https://pub.sandboxaq.com/data/ic50-dataset) | Protein-ligand binding | 1M+ complexes, 5.2M structures, 2.5TB | Experimental | 3D/CSV |
| [Anion Solvation DB](https://doi.org/10.5281/zenodo.13987781) | Anion solvation | ~26k properties | Mixed | CSV |
| [BigSolDB](https://doi.org/10.5281/zenodo.6809668) | Organic molecule solubility | ~54k exp. values | Experimental | CSV |
| [StarryData2](https://github.com/starrydata/starrydata_datasets) | Experimental properties | Figshare dump (2023/2024) | Experimental | CSV/JSON |
| [CRIPT Polymer Data](https://www.criptapp.org) | Polymers (synthesis, properties) | Growing community DB | Mixed | JSON/API |
| [Catechol Benchmark](https://www.kaggle.com/datasets/aichemy/catechol-benchmark) | Solvent selection / Reaction yield | 1200+ process conditions | Experimental | CSV |
| [Leeds Solubility Data](https://doi.org/10.5281/zenodo.3686213) | Solubility | 2.3k measurements | Experimental | CSV |
| [BigSolDB 2.0](https://doi.org/10.5281/zenodo.15094979) | Solubility | 103k+ values | Experimental | CSV/XLSX |
| [OpenExp](https://osf.io/e68v4/files/3dv4k) | Chemical reactions | 274k pairs | Experimental | Varies |
| [Battery Imaging Library (BIL)](https://www.batteryimaginglibrary.com) | Battery imaging | 80+ scans, >500B voxels | Experimental | Various |
| [Experimental 2D Materials Database (X2DB)](https://x2db.fysik.dtu.dk/)| Experimentally realized 2D materials | 603 entries | Experimental | |
| [NMRexp](https://zenodo.org/records/17296666) | Experimental NMR spectra | 3.37M records (6 nuclei) | Experimental | JSON/CSV |
| [OpenBind (first release)](https://openbind.uk) | Protein–ligand binding (structure + affinity) | 925 binding events / 699 compounds | Experimental | CIF/CSV |
| [SAFE Database (LANL)](https://safe.lanl.gov) | Actinide/lanthanide separation chemistry | 18,367 records (41 metals, 323 extractants) | Mixed | CSV |
| [ARROWS³ Synthesis Dataset](https://doi.org/10.5281/zenodo.8331001) | Solid-state synthesis (precursor × temperature sweeps) | ~241 experiments w/ XRD phase fractions | Experimental | JSON |
| [NIST AM-Bench](https://www.nist.gov/ambench/am-bench-2025-measurements-and-challenge-problems) | Additive manufacturing (LPBF/DED) process–structure–property | Multi-benchmark suite | Experimental | Various |
| [Ti-6Al-4V LPBF Process–Structure–Property](https://zenodo.org/records/6587905) | Additive manufacturing (Ti-6Al-4V) | 42 param sets / 168 specimens (3.5 TB) | Experimental | XLSX/XCT |
| [AlSi10Mg LPBF Process–Structure–Property](https://zenodo.org/records/10008435) | Additive manufacturing (AlSi10Mg) | 60 parameter sets | Experimental | XLSX/Images |
| [UHCSDB (Ultra-High Carbon Steel Micrographs)](http://uhcsdb.materials.cmu.edu) | Steel microstructure vs heat treatment | 961 micrographs (598 labeled) | Experimental | Images/SQLite |
| [Aurora Robotic Battery Platform](https://zenodo.org/records/15481956) | Autonomous battery assembly + cycling | 199 cells / 1,000 cycles (704 GB) | Experimental | CSV/Parquet/JSON-LD |
| [A-Lab (Autonomous Inorganic Synthesis)](https://www.nature.com/articles/s41586-023-06734-w) | Autonomous solid-state synthesis campaign | 57 targets / 36 realized | Experimental | CIF/XRD |
| [AlphaFlow](https://github.com/AbolhasaniLab/AlphaFlow) | Self-driving QD shell-growth synthesis (RL) | ~9,000+ condition–outcome spectra | Experimental | Code/Data |
| [Swiss Cat+ CO₂ Hydrogenation HTE](https://zenodo.org/doi/10.5281/zenodo.8314734) | Catalysis (Bayesian-opt campaign) | 144 catalysts / 6 generations | Experimental | CSV/XLSX |
| [CAMEO (Closed-Loop Autonomous Exploration)](https://data.nist.gov/od/ds/mds2-2480/CAMEO_NComm-master.zip) | Autonomous phase mapping (Fe-Ga-Pd) | Composition-spread XRD + loop | Experimental | Python/XRD |
| [Olympus SDL Benchmarks](https://github.com/aspuru-guzik-group/olympus) | Self-driving lab optimization benchmarks | 33 experimental datasets | Experimental | Python |
| [Perovskite Database Project](https://nomad-lab.eu/prod/v1/gui/search/perovskite-solar-cells-database) | Perovskite solar cells (fabrication → PCE) | 43,398 cells × 410 attributes | Experimental | CSV |
| [Dreher–Doyle Buchwald–Hartwig HTE](https://github.com/rxn4chemistry/rxn_yields) | Reaction yield (C–N coupling) | 3,955 reactions | Experimental | XLSX |
| [Pfizer Suzuki–Miyaura HTE](https://github.com/rxn4chemistry/rxn_yields) | Reaction yield (Suzuki coupling) | 5,760 reactions | Experimental | XLSX/CSV |
| [Pfizer HiTEA](https://github.com/emmaking-smith/HiTEA) | High-throughput experimentation (4 reaction classes) | 39,000+ reactions | Experimental | CSV |
| [AstraZeneca ELN Buchwald–Hartwig](https://github.com/nsf-c-cas) | Real-world ELN reactions (C–N coupling) | 781 reactions | Experimental | UDM/CSV |
| [Minerva HTE](https://github.com/schwallergroup/minerva) | Multi-objective reaction optimization | 1,632 reactions | Experimental | SURF/JSON |

---

### LLM Training Datasets

| Dataset | Domain | Size | Type | Format |
| -------------------------------- | ------------------------- | -------------------------- | -------------- | ------------- |
| [ChemPile](https://huggingface.co/collections/jablonkagroup/chempile-6824e88c60d3286ba9b0dae1) | Chemistry | 75B+ tokens | LLM Training | Mixed |
| [SmolInstruct](https://huggingface.co/datasets/osunlp/SMolInstruct) | Small molecules | 3.3M samples | LLM Training | JSON |
| [CAMEL](https://huggingface.co/datasets/camel-ai/chemistry) | Chemistry | 20K problem-solution pairs | LLM Training | JSON |
| [ChemNLP](https://github.com/OpenBioML/chemnlp) | Chemistry | Extensive, many combined datasets | LLM Training | JSON |
| [ChemQA](https://github.com/ChemFoundationModels/ChemLLMBench) | Chemistry | Multimodal QA dataset | LLM Training | JSON |
| [ChemLLMBench](https://github.com/ChemFoundationModels/ChemLLMBench) | Chemistry | 8 chemistry tasks benchmark | LLM Training | JSON |
| [ChemistryQA](https://github.com/microsoft/chemistry-qa) | Chemistry | 4,500 questions across 200 topics | LLM Training | JSON |
| [MaScQA](https://github.com/abhijeetgangan/MaSTeA) | Materials Science | 640 QA pairs | LLM Training | XLSX |
| [SciCode](https://scicode-bench.github.io) | Research Coding in Physics, Math, Material Science, Biology, and Chemistry | 338 subproblems | LLM Training | JSON |
| [ChemData 700K](https://huggingface.co/datasets/AI4Chem/ChemData700K) | Chemistry (9 core tasks) | 730K Q-A instruction pairs | LLM Training | JSON |
| [MatSci-Instruct (HoneyBee)](https://zenodo.org/record/10119842) | Materials science | ≈55K verified instructions | LLM Training | JSON |
| [MoleculeQA](https://huggingface.co/datasets/hcaoaf/MoleculeQA) | Molecular properties & safety | 62K multiple-choice QA pairs | LLM Training | JSON |
| [BioInstruct 25K](https://huggingface.co/datasets/bio-nlp-umass/bioinstruct) | Biomedical / biochemistry | 25K GPT-4 generated instructions | LLM Training | JSON |
| [Lab-Bench](https://huggingface.co/datasets/futurehouse/lab-bench) | Biology | 2,400+ questions for biology agents | LLM Training | JSON |
| [ChemBench 4K](https://huggingface.co/datasets/AI4Chem/ChemBench4K) | Chemistry competency benchmark | 4,100 single-choice questions | LLM Training | JSON |
| [GPQA Diamond](https://github.com/idavidrein/gpqa) | Biology, Physics, Chemistry | 448 multiple-choice questions | LLM Training | JSON |
| [MaCBench](https://macbench.lamalab.org) | Chemistry and materials science | Vision-language tasks | LLM Training | JSON |
| [ChemBench](https://chembench.lamalab.org) | Chemistry | 2,700+ question-answer pairs | LLM Training | JSON |
| [MatText](https://huggingface.co/datasets/n0w0f/MatText) | Materials property prediction | 2M structures | LLM Training | HuggingFace Dataset |
| [SciAssess](https://github.com/sci-assess/SciAssess) | Scientific literature analysis | Benchmark for LLMs in science | LLM Training | JSON |
| [ZINC20-ML](https://files.docking.org/zinc20-ML/) | Drug-like molecules (SMILES) | ≈1B molecules | LLM Training | SMILES |
| [PMC Open Access Subset](https://huggingface.co/datasets/pmc/open_access) | Biomedical full-text | 3.4M+ articles | LLM Training | XML |
| [MatScholar Task-Schema QA (MatSci-NLP)](https://github.com/BangLab-UdeM-Mila/NLP4MatSci-ACL23) | Materials science (7 NLP tasks) | Tens of thousands of examples | LLM Training | JSON |
| [Mol-Instructions](https://huggingface.co/collections/zjunlp/mol-instructions-662e0b9435ab6df9593e8ea0) | Chemistry | molecular, protein, and biochemical instructions | LLM Training | HuggingFace Dataset |
| [USPTO-LLM](https://zenodo.org/records/14396156) | Chemical reactions | 247K reactions | LLM Training | JSON/Graph |
| [ChemRxivQuest](https://arxiv.org/abs/2505.05232) | Chem literature QA | 970 QA pairs | LLM Training | JSON |
| [USPTO-Lowe](https://figshare.com/articles/dataset/5104873) | Patent reactions | 1.8 M reactions | Literature-mined | RXN/SMILES |
| [MolTextNet](https://huggingface.co/datasets/liuganghuggingface/moltextnet) | Small molecules with text | 2.5M molecule-text pairs | LLM Training | HuggingFace Dataset |
| [MolOpt-Instructions](https://huggingface.co/datasets/blazerye/MolOpt-Instructions) | Molecule optimization | 1.18M instruction-based optimization tasks | LLM Training | HuggingFace Dataset |
| [TextEdge](https://drive.google.com/drive/folders/1YCDBzwjwNRIc1FRkB662G3Y5AOWaokUG?ths=true) | Crystal properties | Crystal text descriptions with properties | LLM Training | JSON |
| [LAMBench-TrainingSet-v1](https://aissquare.com/datasets/detail?pageType=datasets&name=LAMBench-TrainingSet-v1&id=308) | Materials structures | 19.8M structures for Large Atom Models | LLM Training | Various |
| [LLM4Mat](https://drive.google.com/drive/folders/1HpGhuNHG4EQCQMZaKPwEQNH9stJKw-ht?dmr%20=%201%26ec%20=%20wgc-drive-hero-goto) | Materials property prediction | 1.9M crystal structures, 45 properties, 3 modalities | LLM Training | Various |
| [LLM-EO](https://github.com/deepprinciple/llmeo) | Transition metal complexes / Optimization | 1.37M TMC space explored | LLM Training | GitHub |
| [Flavor Analysis and Recognition Transformer](https://github.com/fart-lab/fart/tree/main/dataset) | Molecular taste prediction | Multi-class taste classification dataset | LLM Training | SMILES/JSON |
| [SCQA (Solar Cell QA)](https://huggingface.co/collections/CambridgeMolecularEngineering/solar-cell-qa-datasets-67b398f1b9c0f0dd7600a159) | Solar cells | 47K QA pairs | LLM Training | JSON |
| [ScienceQA](https://scienceqa.github.io/) | K–12 science, multimodal MCQs w/ lectures & explanations | 21,208 Qs | LLM Training/Eval | JSON |
| [SciBench](https://scibench-ucla.github.io) | College-level scientific problem solving (math/chem/phys) | Open & closed sets | LLM Eval | PDF/JSON |
| [MegaScience](https://huggingface.co/MegaScience) | Scientific reasoning (7 disciplines) | 1.25M instances (650k reasoning questions from 12k textbooks) | LLM Training | HuggingFace Dataset |
| [Mat-Instructions](https://github.com/AI4MOL/Mat-Instruction) | Inorganic materials | ~30k instructions | LLM Training | JSON |
| [Open Materials Guide (OMG)](https://huggingface.co/datasets/iknow-lab/open-materials-guide-2024) | Materials synthesis | 17K synthesis recipes | LLM Training | JSON |
| [ChemDFM](https://github.com/OpenDFM/ChemDFM) | Chemistry | 34B tokens / 2.7M instructions | LLM Training | HuggingFace |
| [ChemTable](https://github.com/lqzxt/ChemTable) | Chemistry Tables | Large-scale benchmark | LLM Training/Benchmark | JSON |
| [ChemCoTBench](https://huggingface.co/datasets/OpenMol/ChemCoTDataset) | Molecular reasoning | Annotated datasets | LLM Training/Benchmark | HuggingFace Dataset |
| [SciCUEval](https://arxiv.org/abs/2505.15094) | Scientific context understanding (bio/chem/phys/matsci) | 10 sub-datasets | LLM Eval | JSON |
| [MatSciBench](https://arxiv.org/abs/2510.12171) | Materials science reasoning | 1,340 problems (6 fields/31 subfields) | LLM Training/Benchmark | JSON |
| [MolecularIQ](https://github.com/ml-jku/moleculariq) | Molecular structure reasoning | Symbolically-verified graph tasks | LLM Eval | JSON |
| [MatSyn25](https://huggingface.co/datasets/MatSynAI/MatSyn25) | 2D materials synthesis | 163,240 synthesis processes / 182,299 materials | LLM Training | HuggingFace/JSON |


---

### Literature-mined & Text Datasets

| Dataset | Domain | Size | Type | Format |
| -------------------------------- | ------------------------- | -------------------------- | -------------- | ------------- |
| [PubChem](https://pubchem.ncbi.nlm.nih.gov) | Molecules & data | 119M compounds | Literature | SMILES/SDF |
| [Open Reaction Database (ORD)](https://open-reaction-database.org) | Synthetic reactions | ~1M reactions | Experimental/Lit | JSON |
| [PatCID (IBM)](https://github.com/DS4SD/PatCID) | Chemical image data | 81M images / 13M mols | Literature | PNG/SMILES |
| [MatScholar](https://matscholar.com) | NLP corpus (materials) | 5M+ abstracts | Literature | JSON/Graph |
| [Matbench (metadata/text tasks)](https://matbench.materialsproject.org/) | Text/meta ML tasks | 13 tasks | Literature/Benchmark | CSV |
| [OpenQDC Hub](https://github.com/valence-labs/openQDC) | QM molecules & reactions | 1.5 B geometries | Literature/Computational | Python API/NPZ |
| [L2M3 - Large Language Model MOF Miner](https://figshare.com/articles/dataset/L2M3_Database/27187917) | Metal-organic frameworks | from >40k articles | Literature-mined | CSV |
| [RetroRules 2026](https://retrorules.org) | Reaction templates (biochemical + organic) | 1.17M templates / 92,698 reactions | Literature-mined | TSV/CSV/JSON |
| [Text-Mined Solid-State Synthesis (CederGroup)](https://github.com/CederGroupHub/text-mined-synthesis_public) | Inorganic solid-state synthesis recipes | 30,031 reactions | Literature-mined | JSON |
| [Text-Mined Solution-Based Synthesis (CederGroup)](https://github.com/CederGroupHub/text-mined-solution-synthesis_public) | Inorganic solution synthesis (hydrothermal/precipitation) | 35,675 procedures | Literature-mined | JSON |
| [Solid-State Synthesis w/ Impurity Phases](https://doi.org/10.6084/m9.figshare.30423274) | Inorganic synthesis + impurity/secondary phases | 80,806 reactions | Literature-mined | JSON |
| [ZeoSyn](https://github.com/eltonpan/zeosyn_dataset) | Zeolite hydrothermal synthesis routes | 23,961 routes / 233 frameworks | Literature-mined | CSV/JSON |
| [PaRoutes](https://github.com/MolecularAI/PaRoutes) | Multi-step retrosynthesis routes (benchmark) | 2×10k route test sets / ~150k train | Literature-mined/Benchmark | JSON |
| [USPTO-50k (Schneider)](https://figshare.com/articles/dataset/USPTO-50K_raw_/25459573) | Single-step retrosynthesis (benchmark) | 50,016 reactions / 10 classes | Literature-mined/Benchmark | SMILES/CSV |
| [Syntheseus](https://github.com/microsoft/syntheseus) | Retrosynthesis benchmarking framework | Single + multi-step harness | Literature-mined/Benchmark | Python |
| [mech-USPTO-31k](https://doi.org/10.6084/m9.figshare.24797220) | Reaction mechanisms (arrow-pushing) | 31,364 reactions | Literature-mined | CSV/SMILES |
| [PMechDB (Polar Mechanism DB)](https://deeprxn.ics.uci.edu/pmechdb/download) | Elementary polar reaction steps | ~103k steps | Literature-mined | SMIRKS/JSON |
| [RMechDB (Radical Mechanism DB)](https://deeprxn.ics.uci.edu/rmechdb) | Elementary radical reaction steps | ~5,500 steps | Literature-mined | SMIRKS |

---

### 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets

| Dataset | Domain | Size | Type | Format |
| --------------------------------- | ------------------------- | -------------------------- | -------------- | ------------- |
| [PDEBench](https://github.com/pdebench/PDEBench) | PDE solving / Scientific ML | Multiple datasets | Benchmark / Simulation | HDF5/PyTorch |
| [BLASTNet](https://blastnet.github.io) | Fluid mechanics / Reacting flows | 17 TB | Simulation / CFD | HDF5/NPY |
| [Johns Hopkins Turbulence DB (JHTDB)](https://turbulence.pha.jhu.edu) | DNS/LES turbulence (9 canonical flows) | ≈ 350 TB | Simulation | Web API / HDF5 cutouts |
| [Airfoil CFD 2k](https://data.openei.org/submissions/5970) | 1,830 airfoils × 25 AoA × 3 Re | ~6 GB (250 k cases) | Simulation | HDF5 |
| [PDEArena (collection)](https://huggingface.co/pdearena) | 2-D Navier–Stokes, Shallow-Water, 3-D Maxwell | ≈ 100 GB (4 datasets) | Simulation | Torch / HDF5 |
| [WeatherBench 2](https://github.com/pangeo-data/WeatherBench) | Global weather reanalysis (ERA5, 1979-2023) | ≈ 5 TB | Reanalysis | NetCDF/Zarr |
| [UT Austin Channel-DNS Suite](https://turbulence.oden.utexas.edu) | Incompressible channel flow Re<sub>τ</sub> 180 – 5200 | ≈ 10 TB | Simulation | Binary / ASCII |
| [Compressible TPC DNS DB](https://data.mendeley.com/datasets/wt8t5kxzbs) | Compressible channel flow (25 M, Re<sub>τ*</sub>) | ~2 GB | Simulation | TXT tables |
| [Curated RANS ↔ DNS Dataset](https://doi.org/10.34740/kaggle/dsv/2637500) | 29 geometries, 4 RANS models w/ DNS/LES labels | 1.1 GB | Simulation | HDF5/CSV |
| [NASA Common Research Model (CRM)](https://commonresearchmodel.larc.nasa.gov) | Aircraft CRM geom. + wind-tunnel & CFD results | Multi-GB | Mixed (Exp + Sim) | CAD / CSV / Tecplot |
| [Darcy-Flow (FNO)](https://github.com/neuraloperator/neuraloperator) | 2-D porous-media pressure fields (∇·k∇u = f) | ≈ 1 GB (10 k samples) | Simulation | HDF5 |
| [HiFi-TURB LES/DNS](https://cordis.europa.eu/project/id/814837) | High-fidelity LES/DNS for complex 3D flows | Multi-case suite | Simulation (DNS/LES) | HDF5/NetCDF |
| [NASA High Lift Prediction Workshop (HLPW)](https://hiliftpw.larc.nasa.gov/) | High-lift aircraft configurations | Multi-GB | Mixed (exp + CFD) | CAD/CSV/Tecplot |
| [High-Speed TBL DNS DB](https://arc.aiaa.org/doi/10.2514/1.J063456) | Compressible turbulent boundary layers | DNS database | Simulation | HDF5 |
| [ML Turbulence (Kaggle)](https://www.kaggle.com/datasets/ryleymcconkey/ml-turbulence-dataset) | RANS Reynolds stress tensor data | ~GB scale | Benchmark/Simulation | CSV/HDF5 |

---

### Proprietary Datasets (for reference)

| Dataset | Domain | Size | Use Case Notes |
| -------------------------------- | ------------------------- | -------------------------- | ---------------- |
| CAS Registry | Chemical substances | 250M+ substances | Industry standard for molecule indexing |
| Reaxys (Elsevier) | Reactions & properties | Millions of reactions | Rich curated literature reaction data |
| Citrine Informatics DB | Experimental materials | Private | Materials ML platform w/ industry data |
| CSD (Cambridge) | Organic crystals | 1.3M+ | Gold-standard X-ray structures |
| [PoLyInfo](https://polymer.nims.go.jp/en/) | Polymers & properties | 500k+ data points / Experimental | Polymer properties from literature sources |

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

### June 2026

**This update at a glance.** The June 2026 cycle adds 45 datasets that together span the full materials/chemistry ML stack: foundation-model training data (OC25, OPoly26, MAD), 2D-materials databases, experimental spectroscopy and binding data, separation chemistry, reasoning benchmarks, and three new applied tracks — **materials synthesis**, **processing→structure→property causality**, and **reaction & synthesis planning**. The value compounds when they are paired: text-mined synthesis recipes (CederGroup, ZeoSyn) feeding processing-causality sets (AM-Bench, LPBF) to learn synthesis→structure→property end-to-end; HTE yield data (Dreher–Doyle, Pfizer Suzuki, HiTEA) combined with mechanism datasets (PMechDB, mech-USPTO-31k, Transition1x) for mechanistically-grounded yield/condition prediction; retrosynthesis routes (PaRoutes, USPTO-50k, benchmarked via Syntheseus) joined with condition/feasibility data (HiTEA, AstraZeneca ELN) for planners that propose *executable* routes; self-driving-lab campaigns (A-Lab, Aurora, Swiss Cat+) supplying closed-loop priors over those same reaction/synthesis spaces; and reactive MLIPs (Transition1x) extending the foundation potentials (OC25/OPoly26/MAD) into transition-state regions. The LLM benchmarks (MatSciBench, MolecularIQ, SciCUEval) give held-out evaluation for models trained on any of the above.

Added 45 new datasets covering releases since the October 2025 cutoff: universal/foundation-model training data (catalysis, polymers, molecules), the DTU/CAMD family of 2D-materials databases, experimental NMR and protein–ligand binding data, actinide/lanthanide separation chemistry, reaction templates, a new generation of chemistry/materials LLM reasoning benchmarks, a focused set of **materials synthesis, processing-causality, and self-driving-lab** datasets (synthesis recipes, process→structure→property, and autonomous-experimentation campaigns), and a **reaction & synthesis-planning** track (HTE yields, retrosynthesis routes, and reaction mechanisms). Each entry below carries a **🔗 Verify** line with a direct source link and the key figures so additions can be checked quickly. (A few notable Sept–Oct 2025 datasets missed in the prior update are included; the five DTU/CAMD 2D-materials databases — BiDB, HetDB, QPOD, 2D Alloy, X2DB — were contributed by the community via PR.)

#### 🧮 Computational Datasets (8 datasets)
- **OC25 (Open Catalyst 2025)**: Meta FAIR's solid–liquid interface dataset — 7,801,261 DFT calculations across 1,511,270 unique explicit-solvent environments spanning 88 elements, extending OC20/OC22 from solid–gas to electrified solid–liquid interfaces (solvent + ion effects, off-equilibrium sampling). 🔗 Verify: https://huggingface.co/facebook/OC25 · paper arXiv:2509.17862 · 7.8M DFT calcs.
- **OPoly26 (Open Polymers 2026)**: LLNL + Meta FAIR polymer dataset of 6,573,000 ωB97M-V/def2-TZVPD DFT calculations on clusters up to 360 atoms (>1.2B atoms total) sourced from 2,444 unique monomers; OMol25-compatible and ~10× the next-largest polymer dataset. CC-BY-4.0. 🔗 Verify: https://huggingface.co/datasets/colabfit/OPoly26-train · paper arXiv:2512.23117 (also deposited at https://huggingface.co/facebook/OMol25).
- **MAD (Massive Atomic Diversity)**: A deliberately compact universal MLIP dataset — just 95,595 structures across 85 elements (bulk crystals, surfaces, clusters, 2D, molecules), generated by aggressively distorting stable configurations, yet sufficient to train universal potentials (PET-MAD) that rival models trained on 100–1000× more data. PBEsol (Quantum ESPRESSO); EXTXYZ with energies/forces/stresses. 🔗 Verify: https://archive.materialscloud.org/records/xdsbt-a3r17 · paper arXiv:2506.19674 · Sci. Data DOI:10.1038/s41597-025-06109-y.
- **qcMol**: 1.2 million molecules (drug-like compounds, metabolites, experimentally-matched molecules; 247,448 scaffolds), each annotated with 31 quantum-chemical descriptors (15 global, 16 local) at B3LYP-D3/def2-SV(P)//GFN2-xTB, for molecular representation learning. 🔗 Verify: https://structpred.life.tsinghua.edu.cn/qcmol/ · Commun. Chem. DOI:10.1038/s42004-026-02076-6.
- **BiDB (van der Waals Bilayer Database)**: 12,138 homobilayer entries enumerating all stacking/twist registries derived from C2DB monolayers, with stacking-dependent electronic, (anti)ferroelectric, and magnetic properties (GPAW/DFT). Part of the DTU/CAMD 2DHub ecosystem. *(Community contribution.)* 🔗 Verify: https://bidb.fysik.dtu.dk/ · https://2dhub.org/bidb/bidb.html.
- **HetDB (van der Waals 2D Heterostructure Database)**: 336 van der Waals heterobilayers constructed by combining 44 different monolayers and relaxing with the PBE-D3 functional (GPAW), with interlayer and electronic properties. DTU/CAMD. *(Community contribution.)* 🔗 Verify: https://hetdb.fysik.dtu.dk/ · https://2dhub.org/hetdb/hetdb.html.
- **QPOD (Quantum Point Defects Database)**: 24,399 entries cataloguing intrinsic point defects (vacancies, antisites) and their charge states in 2D semiconductors/insulators, with defect formation energies, charge-transition levels, transition dipole moments, hyperfine coupling, and zero-field splitting — aimed at screening single-photon emitters and spin qubits. DTU/CAMD. *(Community contribution.)* 🔗 Verify: https://qpod.fysik.dtu.dk/ · paper arXiv:2110.01961.
- **2D Alloy Database**: 400 two-dimensional transition-metal-dichalcogenide (TMDC) alloy monolayers with DFT-computed properties, for tuning 2D-material properties by alloying. DTU/CAMD. *(Community contribution.)* 🔗 Verify: https://cmrdb.fysik.dtu.dk/2dalloys/ · https://2dhub.org/2dalloys/2dalloys.html.

#### 🧪 Experimental Datasets (4 datasets)
- **NMRexp**: Open, curated collection of 3.37 million experimental NMR records for six nuclei (1H, 13C, 19F, 31P, 29Si, 11B) extracted from ~200,000 Supporting-Information documents (2010–2024), with >99% metadata-extraction accuracy and source-DOI traceability — over an order of magnitude larger than prior public NMR databases. 🔗 Verify: https://zenodo.org/records/17296666 · Sci. Data DOI:10.1038/s41597-025-06245-5.
- **OpenBind (first release)**: First dataset from the OpenBind open-science consortium — 925 crystallographic binding events for 699 compounds (601 with measured K_D affinities) against Enterovirus A71 (EV-A71) 2A protease, accompanied by reference benchmarks for docking, ML-docking, cofolding, and affinity prediction. CC0 1.0. 🔗 Verify: https://openbind.uk · data on Zenodo/Fragalysis · released May 2026.
- **SAFE Database (LANL)**: AI-ready separation-chemistry database from Los Alamos — 18,367 experimental + computational records covering 41 metals including actinides (Am, Pu, U, Cf, Cm) and lanthanides (Eu, Ce, Nd, Pr) and 323 extractant compounds, for liquid–liquid extraction and chromatography. 🔗 Verify: https://safe.lanl.gov. (Community-proposed.)
- **X2DB (Experimental 2D Materials Database)**: 603 experimentally realized two-dimensional materials, complementing the computational C2DB with a record of lab-synthesized monolayers (DTU/CAMD 2DHub). *(Community contribution.)* 🔗 Verify: https://x2db.fysik.dtu.dk/ · https://2dhub.org/x2db/x2db.html.

#### 📖 Literature-mined & Text Datasets (1 dataset)
- **RetroRules 2026**: Expanded reaction-template database combining biochemical (MetaNetX, Rhea) and — newly — organic (USPTO) chemistry: 1,174,216 templates derived from 92,698 reactions covering 5,796 fourth-level EC numbers, with a redesigned website, template generator, and OpenAPI. 🔗 Verify: https://retrorules.org · Nucleic Acids Research DOI:10.1093/nar/gkaf1261.

#### 📚 LLM Training & Benchmark Datasets (4 datasets)
- **SciCUEval**: Benchmark for scientific context understanding in LLMs — 10 domain-specific sub-datasets spanning biology, chemistry, physics, biomedicine, and materials science, integrating structured tables, knowledge graphs, and unstructured text to test relevant-information identification, information-absence detection, multi-source integration, and context-aware inference. (Resolves a prior TODO.) 🔗 Verify: paper arXiv:2505.15094 · Sci. Data DOI:10.1038/s41597-026-06594-9.
- **MatSciBench**: College-level materials-science reasoning benchmark — 1,340 problems across 6 primary fields and 31 subfields; 946 with detailed reference solutions and 315 with images for multimodal evaluation, organized by a three-tier difficulty system and supporting process-level error analysis. 🔗 Verify: paper arXiv:2510.12171.
- **MolecularIQ**: Chemical-reasoning benchmark for LLMs built entirely on symbolically verifiable tasks over molecular graphs (avoiding literature/label leakage and multiple-choice shortcuts), enabling fine-grained localization of model failures to specific tasks and structures. 🔗 Verify: https://github.com/ml-jku/moleculariq · leaderboard https://huggingface.co/spaces/ml-jku/molecularIQ_leaderboard · paper arXiv:2601.15279. (Community-proposed.)
- **MatSyn25 (Material Synthesis 2025)**: Literature-mined 2D-materials synthesis dataset — 163,240 synthesis processes and 193,633 physicochemical-property records extracted from 85,160 articles (182,299 2D materials), used to build a synthesis-process instruction set and the MatSyn AI assistant. 🔗 Verify: https://huggingface.co/datasets/MatSynAI/MatSyn25 · paper arXiv:2510.00776.

#### 🧫 Materials Synthesis Recipes & Precursor Data (5 datasets)
- **Text-Mined Solid-State Synthesis (CederGroup / Kononova)**: 30,031 codified inorganic solid-state synthesis recipes extracted by NLP from 95,283 paragraphs — the foundational corpus underpinning most inorganic-synthesis ML. Captures target formula, precursors, operation sequence, and conditions (temperature, dwell time, atmosphere). 🔗 Verify: https://github.com/CederGroupHub/text-mined-synthesis_public · data https://doi.org/10.6084/m9.figshare.9722159 · Sci. Data 6,203 (2019).
- **Text-Mined Solution-Based Synthesis (CederGroup / Wang)**: 35,675 solution-route procedures (20,037 hydrothermal + 15,638 precipitation) with quantitative precursor amounts (molarity/concentration/volume), solvent, mixing, temperature/time, and balanced reaction equations. CC-BY 4.0. 🔗 Verify: https://github.com/CederGroupHub/text-mined-solution-synthesis_public · Sci. Data 9,231 (2022).
- **Solid-State Synthesis with Impurity Phases (CederGroup, 2025)**: 80,806 LLM-extracted reactions (61,937 phase-pure, 18,869 with documented impurity/secondary phases) from 8.4M publications — the only large corpus linking precursor selection + heating temperature directly to synthesis purity/failure. CC-BY 4.0. 🔗 Verify: https://doi.org/10.6084/m9.figshare.30423274 · Sci. Data Dec 2025.
- **ZeoSyn**: 23,961 zeolite hydrothermal synthesis routes spanning 233 frameworks and 921 OSDAs from 3,096 articles, with 51-component gel composition, crystallization temperature/time, and OSDA descriptors → resulting framework type (~25% failed/amorphous syntheses included). CC-BY 4.0. 🔗 Verify: https://github.com/eltonpan/zeosyn_dataset · ACS Cent. Sci. 2024.
- **ARROWS³**: Experimental solid-state synthesis dataset with systematic precursor × temperature sweeps (~241 experiments across YBCO/NTMO/t-LTOPO), recording XRD-determined phases and weight fractions including target yield% — rare in capturing failed/partial syntheses. CC-BY 4.0. 🔗 Verify: https://doi.org/10.5281/zenodo.8331001 · code https://github.com/njszym/ARROWS · Nat. Commun. Oct 2023.

#### 🏭 Processing → Structure → Property (Causality) (4 datasets)
- **NIST AM-Bench**: Flagship additive-manufacturing benchmark (LPBF & DED of IN625/IN718/15-5 SS/Ti-6Al-4V/polymers) spanning laser power/scan speed/layer thickness → melt-pool geometry, in-situ thermography, phase transformations, 3D microstructure, residual strain, and tensile/fatigue properties — the full feedstock→microstructure→property chain, built for model validation. NIST public domain. 🔗 Verify: https://www.nist.gov/ambench/am-bench-2025-measurements-and-challenge-problems · data https://data.nist.gov.
- **Ti-6Al-4V LPBF Process–Structure–Property**: 42 LPBF parameter sets, 168 tensile specimens, XCT + optical characterization (3.5 TB), mapping laser power/scan speed/hatch/layer → porosity, β-grain morphology, roughness, and YS/UTS/elongation/modulus/hardness across keyhole, lack-of-fusion, and nominal regimes. CC-BY 4.0. 🔗 Verify: https://zenodo.org/records/6587905.
- **AlSi10Mg LPBF Process–Structure–Property**: 60 processing-parameter combinations (power 60–460 W, speed 250–3000 mm/s, hatch 100–150 µm) with Archimedes + XCT porosity + SEM/EBSD + tensile testing → 9 microstructure features and 5 mechanical properties. CC-BY 4.0. 🔗 Verify: https://zenodo.org/records/10008435.
- **UHCSDB (Ultra-High Carbon Steel Micrograph DB)**: 961 SEM micrographs of ultra-high-carbon steel (598 with quantitative heat-treatment metadata: annealing temperature/time + cooling method → microstructure) — the landmark benchmark for process–structure linkage and generative microstructure models. NIST MDR. 🔗 Verify: http://uhcsdb.materials.cmu.edu · https://materialsdata.nist.gov/handle/11256/940.

#### 🤖 Self-Driving Lab / Autonomous Experimentation & HTE (7 datasets)
- **Aurora Autonomous Robotic Battery Platform (Empa)**: 199 coin cells robotically assembled and cycled 1,000× with full BattINFO-compliant assembly metadata and cycling time series (704.5 GB) — the largest open robotic battery dataset; logged assembly + protocol → capacity-fade trajectory. CC-BY 4.0. 🔗 Verify: https://zenodo.org/records/15481956.
- **A-Lab (Autonomous Inorganic Synthesis, LBNL)**: Closed-loop solid-state synthesis campaign targeting 57 novel oxides/phosphates (36 realized in 17 days) — ML proposes a precursor recipe → robot synthesizes → automated XRD → active learner updates; CIF + XRD data open in supplementary. 🔗 Verify: https://www.nature.com/articles/s41586-023-06734-w · code https://github.com/CederGroupHub/s4.
- **AlphaFlow (NC State)**: Reinforcement-learning fluidic platform for multi-step CdSe quantum-dot shell growth — ~9,000+ in-situ spectral condition→outcome measurements where injection sequence/volumes drive absorption/PL outcomes and policy updates. CC-BY 4.0. 🔗 Verify: https://github.com/AbolhasaniLab/AlphaFlow · Nat. Commun. Mar 2023.
- **Swiss Cat+ CO₂ Hydrogenation HTE**: Automated fixed-bed campaign synthesizing/testing 144 heterogeneous catalysts (Cu/Zn/In/Ce on ZrO₂) across 6 Bayesian-optimization generations (boundaries preserved) — catalyst composition + conditions → CO₂ conversion + methanol selectivity. CC-BY 4.0. 🔗 Verify: https://zenodo.org/doi/10.5281/zenodo.8314734.
- **CAMEO (NIST)**: Closed-loop autonomous materials exploration on a Fe-Ga-Pd composition spread — the full trajectory of composition → synchrotron XRD → active-learning query → next composition for simultaneous phase mapping and property optimization. NIST license. 🔗 Verify: https://data.nist.gov/od/ds/mds2-2480/CAMEO_NComm-master.zip.
- **Olympus**: 33 experimentally-derived self-driving-lab benchmark datasets (Suzuki, SnAr, N-benzylation, HPLC, color mixing, photobleaching, …), each a real optimization campaign mapping conditions → yield/purity/stability — the standard benchmark suite for Bayesian-optimization / active-learning development. MIT. 🔗 Verify: https://github.com/aspuru-guzik-group/olympus.
- **Perovskite Database Project (NOMAD)**: 43,398 experimental perovskite-solar-cell records with 410 attributes each from 16,000+ papers, linking fabrication process (deposition method, solvent, dopant, annealing) → PCE and stability — the richest open process→property resource for perovskite PV. FAIR/CC. 🔗 Verify: https://nomad-lab.eu/prod/v1/gui/search/perovskite-solar-cells-database.

#### ⚗️ Reaction & Synthesis Planning (12 datasets)
- **Dreher–Doyle Buchwald–Hartwig HTE**: The canonical reaction-yield benchmark — 3,955 Pd-catalyzed C–N couplings in a full combinatorial matrix of aryl halides, Buchwald ligands, bases, and isoxazole additives. XLSX. 🔗 Verify: https://github.com/rxn4chemistry/rxn_yields · Science 10.1126/science.aat8763.
- **Pfizer Suzuki–Miyaura HTE (Perera et al.)**: 5,760 Pd-catalyzed Suzuki couplings from a nanomole-scale automated platform (electrophile × nucleophile × ligand × base × solvent → yield) — the standard companion to the Dreher–Doyle benchmark. XLSX/CSV. 🔗 Verify: https://github.com/rxn4chemistry/rxn_yields · Science 10.1126/science.aaa9820.
- **Pfizer HiTEA**: The largest open HTE release — 39,000+ reactions across Buchwald–Hartwig, Ullmann, and heterogeneous/homogeneous hydrogenation plus chiral resolutions (>350 products), mapping ligand/catalyst/solvent/base/temperature → yield, dr, and ee. CC-BY 4.0. 🔗 Verify: https://github.com/emmaking-smith/HiTEA · Nature Chemistry 2024.
- **AstraZeneca ELN Buchwald–Hartwig**: The first open electronic-lab-notebook reaction dataset from a major pharma — 781 real-world BH reactions spanning a far broader substrate space (340 aryl halides, 260 amines) than HTE matrices, with temperature and time. CC BY-NC 3.0. 🔗 Verify: https://github.com/nsf-c-cas · Chem. Sci. 10.1039/D2SC06041H.
- **Minerva HTE**: 1,632 HTE reactions from an automated parallel platform optimizing yield and selectivity simultaneously via Bayesian active learning; introduces the SURF reaction format. MIT. 🔗 Verify: https://github.com/schwallergroup/minerva · Nat. Commun. 10.1038/s41467-025-61803-0.
- **PaRoutes**: The field-standard multi-step retrosynthesis route benchmark — two independent 10,000-route test sets (n1/n5) from patents plus ~150k training routes, stock lists, and route-quality/diversity evaluation scripts. CC-BY 4.0. 🔗 Verify: https://zenodo.org/records/6275421 · https://github.com/MolecularAI/PaRoutes.
- **USPTO-50k (Schneider)**: The universal single-step retrosynthesis benchmark — 50,016 atom-mapped patent reactions across 10 reaction classes with standard 40k/5k/5k splits (distinct from the broader USPTO-Lowe set). Reaction SMILES. 🔗 Verify: https://figshare.com/articles/dataset/USPTO-50K_raw_/25459573 · http://tdcommons.ai/generation_tasks/retrosyn/.
- **Syntheseus (Microsoft)**: Unified retrosynthesis benchmarking framework standardizing 10+ single-step models and multi-step search algorithms behind one API, with bundled hard-target test sets — eliminates inconsistent cross-method comparisons. MIT. 🔗 Verify: https://github.com/microsoft/syntheseus · Faraday Discuss. 2024.
- **PMechDB (Polar Mechanism Database)**: ~103,000 elementary polar reaction steps (≈90k combinatorially generated + ≈13k manually curated) with explicit arrow-pushing, atom mapping, and reaction-class labels — the primary curated dataset for polar mechanism prediction. 🔗 Verify: https://deeprxn.ics.uci.edu/pmechdb/download · JCIM 10.1021/acs.jcim.3c01810.
- **RMechDB (Radical Mechanism Database)**: ~5,500 curated elementary radical reaction steps with fish-hook (half-arrow) notation, atom mapping, and mechanistic class labels — the radical companion to PMechDB. 🔗 Verify: https://deeprxn.ics.uci.edu/rmechdb · JCIM 10.1021/acs.jcim.2c01359.
- **mech-USPTO-31k**: 31,364 polar organic reactions paired with chemically validated arrow-pushing mechanisms (generated by MechFinder applied to the USPTO patent corpus) — the largest open patent-scale set of reactions with elementary-step mechanisms. CC BY-NC-ND 4.0. 🔗 Verify: https://doi.org/10.6084/m9.figshare.24797220 · code https://github.com/snu-micc/MechFinder.
- **Transition1x**: 9.6M DFT (ωB97x/6-31G(d)) energies and forces sampled along ~10,000 NEB reaction paths for organic reactions (≤7 heavy atoms; C/N/O) — uniquely covers transition-state regions for training reactive ML potentials and predicting TS geometries. HDF5, CC-BY 4.0. 🔗 Verify: https://doi.org/10.6084/m9.figshare.19614657 · Sci. Data 10.1038/s41597-022-01870-w.

### October 2025

Added 18 new datasets focusing on catalysis, reaction kinetics, cluster chemistry, experimental solubility, literature mining, and foundation models to enhance resources for computational chemistry and machine learning applications.

#### 🧮 Computational Datasets (7 datasets)
- **AQCat25**: The AQCat25 dataset provides a large and diverse collection of 13.5 million DFT calculation trajectories, encompassing approximately 5K materials and 47K intermediate-catalyst systems. It is designed to complement existing large-scale datasets by providing calculations at higher fidelity and including critical spin-polarized systems, which are essential for accurately modeling many industrially relevant catalysts.
- **OMol25 Electronic Structures Dataset**: The OMol25 Electronic Structures dataset includes the raw DFT outputs, electronic densities, wavefunctions, and molecular orbital information for over 4M million high-accuracy quantum chemical calculations. We see this as a transformative opportunity to develop higher quality partial charges, partial spins, and advanced electronic features to unlock the next generation of physics-informed ML models.
- **Unrestricted CCSD(T) Dataset For Organic Molecule Reactions**: Dataset of 3119 organic molecule configurations at gold-standard quantum accuracy with automated workflows for unrestricted CCSD(T) calculations. Includes a transferable MLIP trained on UCCSD(T) data, showing significant improvements in force and activation energy accuracy.
- **MC-PDFT-OPESf**: This work combines multi-configuration pair-density functional theory (MC-PDFT) as an accurate and eﬃcient multireference electronic structure method with on-the-fly probability enhanced sampling flooding (OPESf) as an enhanced sampling method capable of accelerating reactive transitions. MC-PDFT–OPESf provides reaction rates in agreement with experiments at a fraction of the computational cost required by conventional unbiased ab-initio calculations.
- **Quantum Cluster Database**: A database of 63015 low-energy atomically precise nanoclusters for 55 elements across the periodic table, including main group and transition metal elements.
- **Cambridge Cluster Database**: A collection of results from global optimizations for a variety of cluster systems, including Lennard-Jones, metal, molecular, and ionic clusters. The database is continuously updated with new results from published papers.
- **Battery Electrolyte Solvation/Ionization**: This dataset presents molecular properties critical for battery electrolyte design, specifically solvation energies, ionization potentials, and electron affinities for thousands of organic molecules from QM9, EGP, GDB17, and ZINC.

#### 🧪 Experimental Datasets (5 datasets)
- **Catechol Benchmark**: Time-series Solvent Selection Data for Few-shot Machine Learning, providing the first-ever transient flow dataset for machine learning benchmarking, covering over 1200 process conditions. This dataset focuses on solvent selection, a task that is particularly difficult to model theoretically.
- **BNNLab/Solubility_data: Leeds Solubility Data**: Curated solubility data in organic solvents and water and descriptors for solubility prediction.
- **BigSolDB 2.0**: A comprehensive dataset of 103,944 experimentally measured solubility values of 1,448 organic compounds in 213 solvents reported in 1,595 literature peer-reviewed articles.
- **OpenExp**: Features 274,439 pairs of chemical reactions and their corresponding step-by-step instructions of experimental procedures. This dataset, compiled from the USPTO-Applications and ORD databases.
- **Battery Imaging Library (BIL)**: An open, curated collection of multi-modal and multi-length scale battery imaging datasets, featuring over 80 scans and 500 billion voxels of data from single particles to full cells.

#### 📚 LLM Training Datasets (5 datasets)
- **Mat-Instructions**: A large-scale inorganic material instruction dataset with ~30k instruction-response pairs, designed to unlock the potential of LLMs in materials science.
- **Open Materials Guide (OMG)**: A dataset of 17K high-quality, expert-verified synthesis recipes from open-access literature, which forms the basis for the AlchemyBench benchmark for LLM-guided synthesis prediction.
- **ChemDFM**: A pioneering LLM for chemistry trained on 34B tokens from chemical literature and textbooks, and fine-tuned using 2.7M instructions. As a result, it can understand and reason with chemical knowledge in free-form dialogue.
- **ChemTable**: A large-scale benchmark of real-world chemical tables curated from the experimental sections of literature. ChemTable supports table recognition and table understanding tasks to advance scientific reasoning in chemistry.
- **ChemCoTBench**: A reasoning framework that bridges molecular structure understanding with arithmetic-inspired operations to formalize chemical problem-solving into transparent, step-by-step workflows for tasks like molecular optimization and reaction prediction.

#### 📖 Literature-mined & Text Datasets (1 dataset)
- **L2M3 (Large Language Model MOF Miner)**: A database of MOF synthesis conditions and properties extracted from over 40,000 research articles using LLMs, enabling analysis of synthesis-structure-property relationships.

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

