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
  - [Physics & Engineering (PDE, CFD)](#-computational-fluid-dynamics-pde--engineering-datasets)
  - [Microstructure, Phase-Field & Continuum Mechanics](#microstructure-phase-field--continuum-mechanics-datasets)
  - [Proprietary](#proprietary-datasets-for-reference)
  - [APIs, Platforms & Leaderboards](#apis-platforms--leaderboards)
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
| [Materials Project (LBL)](https://materialsproject.org) | Inorganic crystals | 500k+ compounds | Computational | JSON / REST API (mp-api, MCP server) |
| [Open Catalyst 2020 (OC20)](https://opencatalystproject.org) | Catalysis (surfaces) | 1.2M relaxations | Computational | JSON/HDF5 |
| [AFLOW](https://aflow.org) | Inorganic materials | 3.5M materials | Computational | REST API |
| [OQMD](https://oqmd.org) | Inorganic solids | 1M+ compounds | Computational | SQL/CSV |
| [JARVIS-DFT (NIST)](https://jarvis.nist.gov) | 3D/2D materials | 40k+ entries | Computational | JSON/API |
| [Carolina Materials DB](http://www.carolinamatdb.org) | Hypothetical crystals | 214k structures | Computational | JSON |
| [NOMAD](https://nomad-lab.eu/prod/v1/gui/search/entries/search/entries) | Various DFT/MD | >19M calculations | Computational | JSON / REST API (v1) |
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
| [Quantum‑Chemical Bonding DB (LOBSTER)](https://doi.org/10.17172/nomad.mc38-9gm1) | Solid‑state bonding analysis | 13,800 compounds | Computational | JSON/Raw LOBSTER & DFT outputs |
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
| [WBM-MatPES](https://alexandria.icams.rub.de/data/matpes/wbm/) | uMLIP stability/discovery benchmark at MatPES PBE settings (0 to 150 GPa) | 182,427 test structures + 47,792 high-pressure (to 150 GPa) | Benchmark/Comp | JSON (bz2)/CSV |
| [uMOF](https://doi.org/10.6084/m9.figshare.33311829) | Metal-organic frameworks (MLIP training + experimental property benchmark) | 85,524 r2SCAN-D4 configs / 19,950 MOFs | Computational | ZIP |
| [MAD-1.6 (r2SCAN)](https://archive.materialscloud.org/records/ffd5a-1hc37) | Universal (molecules, clusters, bulk, surfaces, adsorbates; 102 elements) | 362,646 r2SCAN configs (102 elements) | Computational | EXTXYZ |
| [ELEMENTA (Kairos Materials)](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) | Inorganic crystals (unary/binary/ternary; universal MLIP training) | ~39M public frames + 4.7M spin frames (public subset of ~210M; CC BY-NC) | Computational | EXTXYZ (tar.zst) |
| [AM26 (Amorphous Materials)](https://github.com/vldgroup/AM26) | Amorphous solids (uMLIP transferability benchmark) | 934 structures / 5 amorphous systems | Benchmark/Comp | EXTXYZ |
| [AdsZeo](https://zenodo.org/records/21445386) | Methane adsorption in Al/Na zeolites (coordinate-resolved GCMC) | 4,775 frameworks × 13 pressures (12.4M frames) | Simulation | DuckDB |
| [OrgReact](https://doi.org/10.6084/m9.figshare.31668682) | Organic reactions / transition states | 9,649 reactions with reactant, product and TS geometries | Computational | XYZ/CSV |
| [LeMat-Rho](https://huggingface.co/datasets/LeMaterial/LeMat-Rho) | Inorganic crystals (r2SCAN charge densities) | 69,117 r2SCAN charge densities | Computational | Parquet |
| [QuantumPioneer](https://zenodo.org/records/20060606) | Solution-phase hydrogen-atom-transfer reactions, radicals, solvation | 348k species / 167k HAT TSs / >100M solvation values | Computational | CSV/Parquet |
| [Reaction-QM](https://zenodo.org/records/18551029) | Organic reaction pathways / transition states (H, C, N, O, F, Si, P, S, Cl) | 2.3M xTB + 200k B3LYP reactions / 23M IRC frames | Computational | HDF5/CSV |
| [QCDGE-CI](https://langroup.site/QCDGE_CI) | Photochemistry / S0-S1 conical intersections of small organic molecules | 259,184 molecules (up to 10 heavy atoms: C, N, O, F) | Computational | HDF5/CSV |
| [AQVolt26](https://huggingface.co/collections/SandboxAQ/aqvolt26) | Lithium halide solid-state electrolytes (high-temperature r2SCAN) | 322,656 r2SCAN single points (public subset gated) | Computational | Parquet |
| [SQuIRL](https://doi.org/10.6084/m9.figshare.30734843) | Computed IR spectra / vibrational properties (QM9 chemical space) | 133,883 molecules | Computational | HDF5 |
| [HE26 (Heavy Elements)](https://doi.org/10.6084/m9.figshare.31429325) | Heavy elements and minor actinides (nuclear materials) | 8 heavy/actinide elements (solids, oxides) | Computational | tar.gz |
| [MofasaDB (Orbital Materials)](https://huggingface.co/datasets/Orbital-Materials/MofasaDB) | Generated metal-organic frameworks (generative-model output, ORB MLIP-relaxed, not DFT) | 200k+ generated MOFs | Computational | ASE DB |
| [tmQMg*](https://zenodo.org/records/17209767) | Excited states of transition metal complexes | 74,281 TMCs × 30 excited states | Computational | CSV |
| [ODAC25 (Open DAC 2025)](https://huggingface.co/facebook/ODAC25) | MOFs + CO2/H2O/N2/O2 adsorption (direct air capture) | ~70M DFT single points / ~15k MOFs | Computational | ASE LMDB (aselmdb) |
| [Halo8](https://zenodo.org/records/16737590) | Reaction pathways incorporating halogen chemistry (F, Cl, Br) | ~20.1M structures / ~19k pathways | Computational | DB (.db) |
| [OC20-mAds / OC20-Slabs](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20_mads.md) | Catalyst surfaces with co-adsorbates; clean slabs | 21.8M + 18.3M frames | Computational |  |
| [HORM (Hessians)](https://zenodo.org/records/17217897) | Molecular Hessians along reaction paths | 1.84M Hessians | Computational | LMDB |
| [QDπ Dataset](https://zenodo.org/records/14970869) | Drug-like molecules, biopolymer fragments and their interactions | 1.6M structures; 13 elements | Computational |  |
| [Alex-MP-20 (MatterGen)](https://github.com/microsoft/mattergen/tree/main/data-release) | Inorganic crystals (generative model training / novelty reference) | ~600k train + 846k reference structures | Benchmark/Comp | CSV |
| [tmQM](https://github.com/uiocompcat/tmQM) | Transition metal complexes (all 30 d-block metals) | ~108k transition-metal complexes | Computational | XYZ/CSV |
| [MDR Phonon PBE (Alexandria)](https://alexandria.icams.rub.de/data/phonon_benchmark/) | Harmonic phonons of inorganic crystals | ~10k PBE phonon calculations | Benchmark/Comp | EXTXYZ / per-material files |
| [sAlex (train + val)](https://huggingface.co/datasets/facebook/OMAT24#salex-dataset) | Inorganic crystals (MLIP fine-tuning; Matbench Discovery compliant) | 10.4M train + 553k val structures | Computational | ASE LMDB (aselmdb) |
| [nablaDFT / ∇²DFT](https://github.com/AIRI-Institute/nablaDFT) | Drug-like molecules (C, N, S, O, F, Cl, Br, H) | 1.94M molecules / 12.7M conformations | Benchmark/Comp |  |
| [OC20NEB](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20neb.md) | Surface reaction barriers (transition states) | 932 NEB trajectories | Benchmark/Comp | ASE .traj (tar.gz) |
| [MISATO](https://zenodo.org/records/7711953) | Protein-ligand complexes with MD and semiempirical QM | 19,443 complexes with MD + QM | Mixed | HDF5 |
| [SPICE 2](https://zenodo.org/records/10975225) | Drug-like molecules, peptides, ligand-amino acid dimers, solvated systems | 2.0M conformations / 114k molecules | Computational | HDF5 |
| [GNoME (DeepMind)](https://github.com/google-deepmind/materials_discovery) | Inorganic crystals (predicted stable materials) | ~381k new stable crystals (520k+ near hull) | Computational | CSV/CIF |
| [ANI-2x](https://zenodo.org/records/10108942) | Small organic molecules (H, C, N, O, S, F, Cl) | ~4.6M conformers | Computational | HDF5 |
| [MPtrj](https://figshare.com/articles/dataset/23713842) | Inorganic crystals (universal MLIP training) | 1.58M frames / 145,923 materials | Computational | JSON / EXTXYZ |
| [Materials Cloud MC2D](https://mc2d.materialscloud.org/) | 2D materials from computational exfoliation | 2,683 2D materials | Computational | OPTIMADE JSON; AiiDA provenance |
| [PubChemQC B3LYP/6-31G*//PM6](https://nakatamaho.riken.jp/pubchemqc.riken.jp/b3lyp_pm6_datasets.html) | PubChem small molecules (electronic structure) | 86M molecules | Computational |  |
| [RGD1](https://doi.org/10.6084/m9.figshare.21066901) | Organic reactions / transition states (C, H, N, O) | 176,992 reactions with TSs | Computational | HDF5/CSV |
| [MD22](http://www.sgdml.org/) | MD trajectories of biomolecules and supramolecules (42 to 370 atoms) | 7 systems (42 to 370 atoms) | Benchmark/Comp | NPZ/XYZ |
| [OC22 (Open Catalyst 2022)](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc22.md) | Oxide electrocatalyst surfaces + adsorbates (total energies) | ~62k oxide systems / 9.85M frames | Computational | LMDB |
| [MPTS-52](https://figshare.com/articles/dataset/Materials_Project_Time_Split_Data/19991516) | Crystal generative model benchmark (chronological splits) | MP compounds ≤52 sites, time-split | Benchmark/Comp | JSON |
| [GEOM](https://doi.org/10.7910/DVN/JNGTDF) | Molecular conformer ensembles (drug-like and QM9 molecules) | ~37M conformers / 450k+ molecules | Computational | MessagePack/RDKit |
| [MP-20 / Perov-5 / Carbon-24 (CDVAE)](https://github.com/txie-93/cdvae/tree/main/data) | Crystal generation / structure prediction benchmarks | ~45k / ~19k / ~10k structures | Benchmark/Comp | CSV |
| [OrbNet Denali](https://doi.org/10.6084/m9.figshare.14883867) | Bio-organic molecules incl. protonation/tautomer states, salts, non-covalent complexes | 2.3M conformers / 212,905 molecules | Computational | XYZ |
| [QM7-X](https://zenodo.org/records/4288677) | Small organic molecules (up to 7 heavy atoms; C, N, O, S, Cl) | ~4.2M structures, 42 properties | Computational | XZ-compressed files |
| [DES370K / DES5M](https://zenodo.org/records/5676266) | Non-covalent dimer interaction energies (neutral and ionic, protein-like fragments) | 370k CCSD(T) + ~5M SNS-MP2 dimer geometries | Computational | CSV |
| [WBM Test Set](https://github.com/janosh/matbench-discovery/blob/main/data/wbm/readme.md) | Hypothetical inorganic crystals (stability prediction / discovery benchmark) | 256,963 structures | Benchmark/Comp | JSON / EXTXYZ / CSV |
| [MD17 / revised MD17 (rMD17)](https://doi.org/10.6084/m9.figshare.12672038) | Molecular dynamics trajectories of small organic molecules | 10 molecules (100k frames each in rMD17) | Benchmark/Comp | NPZ/XYZ |
| [OE62](https://doi.org/10.14459/2019mp1507656) | Organic molecules from crystals / organic electronics (orbital energies) | 61,489 molecules | Computational | XYZ |
| [Materials Cloud MC3D](https://mc3d.materialscloud.org/) | Inorganic crystals (experimental structures relaxed with DFT) | ~33k relaxed structures | Computational | OPTIMADE JSON; AiiDA provenance graphs |


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
| [4D-STEM Diffraction Benchmark](https://doi.org/10.57760/sciencedb.nbsdc.00281) | 4D-STEM convergent-beam diffraction patterns (Ag, Au, Au-Ag, CoO, Pd, ZnO nanoparticles + simulations) | 145k experimental + 29k simulated patterns | Benchmark | PKL/JSON |
| [PolyBench26](https://github.com/rlearsch/PolymerBenchmark2026) | Polymer properties (homopolymers and alternating, random, block copolymers) | ~250k datapoints / 8 properties | Benchmark | CSV (PSMILES) |
| [OpenADMET blind-challenge datasets](https://huggingface.co/openadmet) | ADMET: CYP inhibition/TDI (4 isoforms), PXR induction (+184 co-crystal structures), ExpansionRx (9 endpoints) | ~10k + 11,362 + >7,000 compounds | Benchmark | CSV/Parquet |
| [Precursor Genome (A-Lab)](https://doi.org/10.5281/zenodo.21285546) | Solid-state synthesis (pairwise precursor reactions, XRD) | 1,035 reactions / 1,351 XRD scans | Experimental | JSON/XRDML/PKL |
| [RamanBench](https://github.com/ml-lab-htw/RamanBench) | Raman spectroscopy (materials, chemical/industrial, biological, clinical) | 74 datasets / 325,668 spectra | Benchmark | Parquet/Python |
| [EM3M](https://huggingface.co/datasets/UniParser/EM3M) | Electron microscopy of materials (powders, nanoparticles, ceramics, minerals) | 5,091 micrographs / ~3M masks | Experimental | Parquet |
| [Runs N' Poses](https://zenodo.org/records/14794785) | Protein-ligand co-folding benchmark | 2,600 PLI systems | Benchmark | CSV/Parquet + structure archives |
| [BatteryLife](https://github.com/Ruifeng-Tan/BatteryLife) | Li-ion, Na-ion and Zn-ion battery cycle life | 16 datasets / 990+ cells | Benchmark | PKL/raw |
| [OBELiX](https://github.com/NRC-Mila/OBELiX) | Lithium solid-state electrolytes: ionic conductivity | 599 measured conductivities | Experimental | CSV + CIF |
| [Papyrus](https://zenodo.org/records/13787633) | Bioactivity (compound-protein activity) | ~60M activities / 1.27M compounds | Experimental | TSV/SDF |
| [Leash BELKA](https://polarishub.io/datasets/leash-bio/belka-v1) | DNA-encoded library small-molecule binding (BRD4, sEH, HSA) | ~133M molecules × 3 targets | Experimental | Parquet |
| [MassSpecGym](https://huggingface.co/datasets/roman-bushuiev/MassSpecGym) | Tandem mass spectrometry (MS/MS) of small molecules | 231k MS/MS spectra / 29k molecules | Benchmark | TSV/Parquet |
| [PLINDER](https://www.plinder.sh/) | Protein-ligand interaction systems (docking / co-folding training and evaluation) | 1.34M PLI systems | Benchmark |  |
| [CALiSol-23](https://doi.org/10.11583/DTU.c.6929599.v1) | Li-ion electrolyte ionic conductivity (salt, solvent blend, concentration, temperature) | 13,825 measurements | Experimental | CSV |
| [RhNet Gas Sorption in Polymers](https://github.com/Shorku/rhnet/tree/main/data) | Polymers (gas and vapor solubility / sorption) | ~16k measurements / 107 polymers / 81 gases | Experimental | CSV + XYZ geometries |
| [ProteinGym](https://proteingym.org) | Protein fitness / mutation effects (DMS and clinical variants) | ~2.7M variants / 217 DMS assays | Benchmark | CSV |
| [3DSC](https://github.com/aimat-lab/3DSC) | Superconductors: measured Tc matched to crystal structures | 5,759 superconductors with structures | Mixed | CSV + CIF |
| [PoseBusters Benchmark](https://zenodo.org/records/8278563) | Protein-ligand docking pose validity | 428 + 85 complexes | Benchmark | ZIP/CSV |
| [MPEA Mechanical Properties](https://doi.org/10.6084/m9.figshare.12642953) | High-entropy / multi-principal element alloys: mechanical properties and phases | 1,545 records / 630 alloys | Experimental | CSV |
| [AqSolDB](https://doi.org/10.7910/DVN/OVHAW8) | Aqueous solubility of organic compounds | 9,982 compounds | Experimental | CSV |
| [Toyota-Stanford-MIT Battery Cycle Life](https://data.matr.io/1/) | LFP/graphite fast-charge cycling to end of life | 124+ LFP cells cycled to failure | Experimental | MAT/CSV |
| [NIST Chemistry WebBook](https://webbook.nist.gov/chemistry/) | Thermochemistry, IR / mass / UV-Vis spectra, thermophysical properties | 40,000+ compounds | Experimental | Web/JCAMP-DX |
| [RRUFF](https://rruff.info) | Minerals: Raman, IR, powder XRD, microprobe chemistry | ~22k Raman + IR + XRD of minerals | Experimental | TXT/DIF |
| [Battery Archive](https://www.batteryarchive.org) | Li-ion cell cycling and abuse/thermal-runaway tests from multiple institutions | 12 studies from 8 institutions | Experimental | CSV (standardized cycle and time-series) |
| [SciGlass](https://github.com/epam/SciGlass) | Glasses and glass-forming melts: composition-property data | ~422k glass compositions | Experimental | MDB |
| [NIST ThermoML Archive](https://trc.nist.gov/ThermoML/) | Thermophysical and thermochemical properties of pure compounds and mixtures | Data from 5 partner journals | Experimental | ThermoML (IUPAC XML) |
| [NIST/ARPA-E ISODB](https://adsorption.nist.gov/isodb/) | Gas adsorption isotherms on MOFs, zeolites, carbons and other porous materials | ~40k isotherms | Experimental | JSON API/CSV |
| [nmrshiftdb2](https://nmrshiftdb.nmr.uni-koeln.de/) | NMR spectra of organic molecules (13C, 1H and other nuclei) | 70k measured spectra / 272k structures | Experimental | SDF/CML |
| [MassBank](https://massbank.eu/MassBank/) | Mass spectra (EI, ESI-MS/MS) of small molecules | ~139k spectra | Experimental | Text/MSP/API |
| [NIST XPS Database (SRD 20)](https://srdata.nist.gov/xps/) | XPS and Auger line energies, chemical shifts, doublet splittings | 22,000+ line positions | Experimental | Web |

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
| [ChemRxivQuest](https://huggingface.co/datasets/Bocklitz-Lab/ChemQuests) | Chem literature QA | 952 QA pairs (151 preprints) | LLM Training | JSONL/CSV |
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
| [MatSciFig](https://huggingface.co/datasets/CMEG-IITR/MatSciFig) | Materials science figures (multimodal image-text) | 391,606 panel image-text pairs / 14,810 papers | LLM Training | Parquet (gated) |
| [MolDesignBench](https://huggingface.co/datasets/LG-AI-Research/MolDesignBench) | Tool-augmented molecular design agents | 2,000 tasks / 17 tools | Benchmark | JSONL |
| [SciAgentGym](https://github.com/CMarsRover/SciAgentGYM) | Multi-step scientific tool use (physics, chemistry, materials, life science, astronomy) | 259 tasks / 1,780 tools | Benchmark | JSON |
| [LABBench2](https://huggingface.co/datasets/EdisonScientific/labbench2) | Biology research agents (literature, figures, tables, protocols, sequences, cloning) | ~1,900 tasks | LLM Eval | Parquet (gated) |
| [FrontierScience](https://huggingface.co/datasets/openai/frontierscience) | Expert-level physics, chemistry and biology reasoning | 160 gold questions | LLM Eval | JSON/Parquet |
| [MatCha](https://huggingface.co/datasets/FreedomIntelligence/MatCha) | Materials characterization image understanding | 1,500 questions / 21 tasks | LLM Eval | JSON + images |
| [MatQnA](https://huggingface.co/datasets/richardhzgg/matQnA) | Materials characterization multimodal QA (XPS, XRD, SEM, TEM and others) | 4,968 QA pairs | LLM Eval | Parquet (images + text) |
| [HLE Gold Bio/Chem](https://huggingface.co/datasets/futurehouse/hle-gold-bio-chem) | Validated chemistry and biology subset of Humanity's Last Exam | Validated HLE subset | LLM Eval | Parquet (gated) |
| [ether0 Benchmark](https://huggingface.co/datasets/futurehouse/ether0-benchmark) | Chemistry reasoning with molecule-valued answers (verifiable rewards) | 325 questions | LLM Eval | Parquet |
| [ChemToolBench](https://huggingface.co/datasets/RadiCat/ChemToolBench) | Chemistry and materials tool calling (tool selection and parameter filling) | 137 tools | LLM Training | JSON |
| [MolLangBench](https://huggingface.co/datasets/ChemFM/MolLangBench) | Language-prompted molecular structure recognition, editing and generation | ~34.6k examples | LLM Eval | Parquet (SMILES + molecule images) |
| [ChemIQ](https://github.com/oxpig/ChemIQ) | Molecular comprehension and chemical reasoning from SMILES | 816 questions | LLM Eval | JSONL |
| [MatTools](https://huggingface.co/datasets/SiyuLiu/MatTools) | Materials science tool use and code generation (pymatgen) | ~69k QA pairs + 138 tasks | Benchmark | JSON |
| [MolPuzzle](https://huggingface.co/datasets/kguo2/MolPuzzle_data) | Multimodal structure elucidation from IR, MS, 1H and 13C NMR | 217 puzzles / 23,678 QA pairs | LLM Eval | CSV |
| [TOMG-Bench](https://huggingface.co/datasets/phenixace/S2-TOMG-Bench) | Open-domain text-driven molecule generation | 45k test samples | Benchmark | CSV |
| [LabSafety Bench](https://huggingface.co/datasets/yujunzhou/LabSafety_Bench) | Laboratory safety (chemical, biological, radiation, physical hazards) | 765 MCQs + 3,128 open tasks | LLM Eval | Parquet (text + images) |
| [ChemEval](https://huggingface.co/datasets/Ooo1/ChemEval) | Multi-level chemistry benchmark (text + multimodal) | 62 tasks / 5,120 examples | LLM Eval | Parquet |
| [CrystaLLM CIF Corpus](https://zenodo.org/records/10642388) | Crystal structure generation with language models | 2.28M CIFs | LLM Training | CIF |
| [ChEBI-20](https://github.com/cnedwards/text2mol) | Molecule-text pairs (captioning and text-to-molecule) | 33,010 molecule-text pairs | LLM Training | TXT/SDF |


---

### Literature-mined & Text Datasets

| Dataset | Domain | Size | Type | Format |
| -------------------------------- | ------------------------- | -------------------------- | -------------- | ------------- |
| [PubChem](https://pubchem.ncbi.nlm.nih.gov) | Molecules & data | 119M compounds | Literature | SMILES/SDF |
| [Open Reaction Database (ORD)](https://open-reaction-database.org) | Synthetic reactions | ~1M reactions | Experimental/Lit | JSON |
| [PatCID (IBM)](https://github.com/DS4SD/PatCID) | Chemical image data | 81M images / 13M mols | Literature | PNG/SMILES |
| [MatScholar](https://matscholar.com) | NLP corpus (materials) | 5M+ abstracts | Literature | JSON/Graph |
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
| [SureChEMBL Bulk Data](https://ftp.ebi.ac.uk/pub/databases/chembl/SureChEMBL/bulk_data/) | Patent chemistry (compounds, patents, biomedical annotations) | Weekly snapshots (~17 GB Parquet + HDF5) | Literature-mined | Parquet/HDF5 |
| [ORD USPTO Grants (uspto-grants)](https://huggingface.co/datasets/open-reaction-database/ord-data/viewer/uspto-grants) | Organic reactions from US patent grants | 1.77M reactions | Literature-mined | Parquet (ORD) |
| [LeMat-Synth](https://huggingface.co/datasets/LeMaterial/LeMat-Synth) | Inorganic materials synthesis procedures | 58k procedures / 81k papers | Literature-mined | Parquet |
| [NEMAD](https://www.nemad.org) | Magnetic materials (Curie/Neel temperatures); thermoelectric and superconductor sections | 67,573 magnetic entries | Literature-mined | Web/CSV |
| [LLM-Agent Thermoelectric Dataset](https://cmeg-iitr.github.io/thermoelectric_dataset) | Thermoelectric materials (ZT, Seebeck, conductivities + structure) | 27,822 records | Literature-mined | Web/CSV |
| [MatSKRAFT Knowledge Base](https://doi.org/10.5281/zenodo.17064278) | Materials compositions and properties from tables (glasses and beyond) | 509,281 entries | Literature-mined | CSV |
| [MatSciKB](https://github.com/BangLab-UdeM-Mila/NLP4MatSci-HoneyComb/blob/main/honeycomb_framework/recall_layer/databases/knowledge_base.json) | Materials science knowledge base (papers, Wikipedia, textbooks, formulas) | ~28k entries | Literature-mined | JSON |
| [PolyIE](https://github.com/jerry3027/PolyIE) | Polymer information extraction (solar cells, Li batteries) | 146 annotated papers | Benchmark | JSONL |
| [ORDerly](https://figshare.com/articles/dataset/ORDerly_chemical_reactions_condition_benchmarks/23298467) | Reaction condition, forward and retrosynthesis benchmarks | 3 benchmark tasks (cleaned USPTO-in-ORD) | Benchmark | Parquet |
| [CO2 Reduction Electrocatalyst Corpus](https://doi.org/10.57760/sciencedb.13290) | Electrocatalytic CO2 reduction catalysts and synthesis | 6,985 expert records + LLM corpus | Literature-mined | CSV/JSON |
| [MatKG](https://zenodo.org/records/10144972) | Materials science knowledge graph | ~3.5M triples / 150k+ entities | Literature-mined | CSV/N-Triples |
| [ChemDataExtractor auto-generated databases (Cole group)](https://doi.org/10.6084/m9.figshare.11888115) | Literature-mined properties: battery materials, thermoelectrics, band gaps, refractive index/dielectric, solar cells (DSC/PSC), Curie/Néel temperatures | 6 databases / ~1.2M records | Literature-mined | JSON/CSV/SQL/MongoDB |

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
| [AgentFEM Material Loading Memory](https://huggingface.co/datasets/HaomingLuo/AgentFEM-Material-Loading-Memory) | Path-dependent elastoplasticity / Neural constitutive modeling | 3,788 loading histories across six staged releases | Simulation / Benchmark | HDF5/NPZ/JSON |
| [AgentFEM Controlled Transient Heat](https://huggingface.co/datasets/HaomingLuo/AgentFEM-Controlled-Transient-Heat) | Controlled solid heat conduction / Field forecasting | 64 scenarios, 192 branched trajectories | Simulation / Benchmark | HDF5/CSV/JSON |
| [TIDE](https://huggingface.co/datasets/ydai17/TIDE) | 3D incompressible turbulence DNS (256^3) | 134 trajectories / ~2.6 TB | Benchmark | Zarr |
| [HiLiftAeroML](https://huggingface.co/datasets/nvidia/HiLiftAeroML) | High-lift aircraft aerodynamics (NASA CRM-HL, wall-modeled LES) | 1,800 LES runs / ~67 TB | Simulation | VTU/STL/CSV/NPY |
| [PDEInvBench](https://huggingface.co/datasets/DabbyOWL/PDE_Inverse_Problem_Benchmarking) | PDE inverse problems (parameter recovery): KdV, reaction-diffusion, Navier-Stokes, Kolmogorov turbulence, Darcy | >1.2M simulations / ~2.3 TB | Benchmark | HDF5 |
| [Luminary SHIFT-Crash](https://huggingface.co/datasets/luminary-shift/SHIFT-Crash) | Vehicle frontal crash (time-resolved stress, strain, energy); gated, CC BY-NC | ~5,200 crash cases | Simulation | VTP/VTU/STL |
| [Luminary SHIFT-Battery](https://huggingface.co/datasets/luminary-shift/Battery) | Battery pack thermal management (conjugate heat transfer CFD); gated, CC BY-NC | 1,300+ battery cases | Simulation | VTP/VTU/STL |
| [WAKESET](https://huggingface.co/datasets/ZacharyCB99/WAKESET) | High-Reynolds turbulent wake hydrodynamics (AUV recovery, RANS) | 1,091 RANS simulations / ~481 GB | Simulation |  |
| [SuperWing](https://huggingface.co/datasets/yunplus/SuperWing) | Transonic swept-wing aerodynamics (RANS, ADflow; Mach 0.75 to 0.90) | 4,239 wings / 28,856 flow fields | Simulation | NPY/Parquet |
| [DrivAerStar](https://drivaerstar.github.io/) | Automotive aerodynamics (industrial STAR-CCM+ CFD) | 12,000 simulations / ~20 TB | Simulation | VTK/EnSight |
| [BubbleML 2.0](https://huggingface.co/datasets/hpcforge/BubbleML_2) | Multiphase boiling and phase change (pool and flow boiling; FC-72, R-515B, LN2) | 160+ simulations / ~2.55 TB | Simulation | HDF5 + JSON metadata |
| [The Well (Polymathic AI)](https://github.com/PolymathicAI/the_well) | Multi-physics PDE simulations (fluids, MHD, acoustics, active matter, reaction-diffusion, astrophysics) | 16 datasets / 15 TB | Simulation | HDF5 |
| [FlowBench](https://huggingface.co/datasets/BGLab/FlowBench) | Flow over complex geometries (2D flow past objects, 2D/3D lid-driven cavity; DNS) | 10k+ samples / ~1.72 TB | Benchmark | NPZ |
| [DrivAerML / AhmedML / WindsorML](https://huggingface.co/datasets/neashton/drivaerml) | Automotive external aerodynamics (hybrid RANS-LES, OpenFOAM) | 484 + 500 + 355 runs (~42 TB) | Simulation | VTU/VTP/STL/CSV |
| [DrivAerNet++](https://dataverse.harvard.edu/dataverse/DrivAerNet) | Car aerodynamics, multimodal (CFD fields, meshes, point clouds, drag coefficients) | 8,000+ designs / ~39 TB | Simulation |  |
| [LagrangeBench](https://github.com/tumaer/lagrangebench) | Lagrangian particle (SPH) fluid mechanics | 7 datasets / 8.4 GB | Benchmark | ZIP archives |
| [AirfRANS](https://github.com/Extrality/AirfRANS) | 2D subsonic airfoil RANS flows | 1,000 simulations | Benchmark |  |

---

### Microstructure, Phase-Field & Continuum Mechanics Datasets

Mesoscale and continuum materials data: phase-field microstructure evolution, homogenization, crystal plasticity and fracture.

| Dataset | Domain | Size | Type | Format |
| --------------------------------- | ------------------------- | -------------------------- | -------------- | ------------- |
| [CrackMNIST](https://doi.org/10.5281/zenodo.18454958) | Fatigue crack growth in aluminium alloys (DIC displacement fields) | 8,794 DIC fields / 70,352 samples | Experimental | HDF5 |
| [Material Fracturing & Failure (LANL)](https://huggingface.co/datasets/smartFRACs/material_fracturing) | Fracture propagation in PBX, shale, tungsten, aluminum and steel (phase-field and FDEM) | 400k phase-field cases × 5 materials + 90k FDEM (~5.3 TB) | Simulation | HDF5 |
| [Strained Alloy Microstructure (Materials Cloud)](https://archive.materialscloud.org/record/2025.117) | Phase-field spinodal decomposition with elastic lattice misfit | ~34 GiB | Simulation | ZIP archives |
| [PFM-Fracture](https://dataverse.harvard.edu/dataverse/PFM-Fracture) | Phase-field brittle fracture (three energy decompositions, tension and shear) | 6,000 simulations / ~198 GB | Benchmark |  |
| [SIFBench](https://huggingface.co/datasets/tgautam03/SIFBench) | Stress intensity factors for cracked components (finite-element derived) | 5M+ geometries / 37 scenarios | Benchmark | CSV/Parquet |
| [OPMD (Open Phase-field Microstructure Dataset)](https://zenodo.org/records/16756795) | Phase-field microstructure evolution (PFHub-style benchmark) | 1,000 simulations × 200 frames | Benchmark | TAR (arrays) |
| [LiFePO4 Phase-Field Benchmark (DTU)](https://doi.org/10.11583/DTU.25562364) | Cahn-Hilliard phase separation in LiFePO4 battery particles | 1,100 trajectories / ~96 GB | Benchmark | HDF5 |
| [MICRO2D](https://arobertson38.github.io/MICRO2D) | Two-phase microstructures with homogenized elastic and thermal properties | 87,379 microstructures | Simulation | HDF5 |
| [Microstructure Evolution Phase-Field (Sandia/MDF)](https://acdc.alcf.anl.gov/mdf/detail/microstructure_evolution_phase_field_v1.1/) | Phase-field trajectories: spinodal decomposition, physical vapor deposition, dendritic growth, grain growth | 4 phenomena (spinodal, PVD, dendrites, grain growth) | Simulation |  |
| [Inconel 718 3D Microstructure + Deformation](https://doi.org/10.5061/dryad.83bk3j9sj) | 3D EBSD grain structure plus in-situ DIC strain/slip fields for a Ni superalloy | ~55 GB (3D EBSD + DIC) | Experimental |  |
| [Mechanical MNIST (collection)](https://open.bu.edu/collections/61b965cd-064d-4e51-b31d-f7d784ee970b) | Finite-element mechanics of heterogeneous materials (hyperelasticity, Cahn-Hilliard patterns, phase-field fracture) | 10 datasets (~70k samples each) | Benchmark |  |
| [Synthetic 3D Polycrystals + EVPFFT (Mangal & Holm)](https://data.mendeley.com/datasets/kt8hfg4t2p/1) | Crystal plasticity of DREAM.3D polycrystals (HCP; companion FCC set) | 54 microstructures (128³ voxels) | Simulation |  |

---

### Proprietary Datasets (for reference)

| Dataset | Domain | Size | Use Case Notes |
| -------------------------------- | ------------------------- | -------------------------- | ---------------- |
| CAS Registry | Chemical substances | 250M+ substances | Industry standard for molecule indexing |
| Reaxys (Elsevier) | Reactions & properties | Millions of reactions | Rich curated literature reaction data |
| Citrine Informatics DB | Experimental materials | Private | Materials ML platform w/ industry data |
| CSD (Cambridge) | Organic crystals | 1.3M+ | Gold-standard X-ray structures |
| [PoLyInfo](https://polymer.nims.go.jp/en/) | Polymers & properties | 500k+ data points / Experimental | Polymer properties from literature sources |
| [Pistachio (NextMove)](https://www.nextmovesoftware.com/pistachio.html) | Patent reactions (US and EPO) | 21M+ reactions | Commercial patent reaction set (US + EPO); common Reaxys alternative |
| [MPDS / PAULING FILE](https://mpds.io) | Inorganic materials: crystal structures, physical properties, phase diagrams | 425k structures / 1.1M properties / 140k phase diagrams | Curated literature data (PAULING FILE); free open subset via API; requested in issue #3 |
| [ICDD PDF-5+](https://www.icdd.com/pdf-5/) | Powder diffraction reference patterns (inorganic and organic) | ~1.15M entries | Reference patterns for XRD phase ID; annual subscription |
| [SpringerMaterials](https://materials.springer.com) | Curated properties, crystal structures and phase diagrams across material classes | Not stated | Curated properties, structures and phase diagrams; subscription |
| [MatNavi (NIMS)](https://mits.nims.go.jp/en/) | Structures, CALPHAD, diffusion, creep/fatigue/tensile sheets, CCT diagrams | 12 databases | Free with registration; bulk download prohibited |
| [SDBS (AIST)](https://sdbs.db.aist.go.jp) | Organic compound spectra: EI-MS, 1H/13C NMR, FT-IR, Raman, ESR | ~34,600 compounds | Free to browse (MS, NMR, IR, Raman, ESR); bulk download prohibited |
| [Polymer Scholar](https://polymerscholar.org) | Polymer properties (LLM/MaterialsBERT-extracted) | ~1.06M property records | Browsable with login; bulk-download terms not stated |

### Dataset Resources
* [The Materials Data Facility](https://www.materialsdatafacility.org) - Over 100 TB of open materials data. #TODO list some of these in the tables above
* [Foundry-ML](https://materialsdatafacility.org/portal) *search Foundry* - 61 structured datasets ready for download through a Python client #TODO list some of these in the tables above

### APIs, Platforms & Leaderboards

Programmatic access points, data hubs and community leaderboards (not single datasets).

| Resource | Domain | Scale | Type | Access |
| --------------------------------- | ------------------------- | -------------------------- | -------------- | ------------- |
| [LeMat-GenBench](https://huggingface.co/spaces/LeMaterial/LeMat-GenBench) | Generative models for inorganic crystals | 12+ generative models | Benchmark | Open-source evaluation suite + Hugging Face leaderboard |
| [OPTIMADE](https://www.optimade.org/) | Federated materials structure databases | 30 registered providers | API | JSON:API REST |
| [Garden (Globus Labs)](https://thegardens.ai/) | Published scientific AI models (MLIPs and others) | 100+ models | Platform | garden-ai Python SDK; remote execution on Modal and Globus Compute |
| [MLIP Arena](https://huggingface.co/spaces/atomind/mlip-arena) | Universal machine-learning interatomic potentials | 4 benchmark categories | Benchmark | Python package + Hugging Face leaderboard |
| [LAMBench](https://www.aissquare.com/openlam?tab=Benchmark) | Universal MLIPs across materials, molecules and catalysis | 17 OOD test sets (12 force-field + 5 property) | Benchmark | Python benchmark suite + web leaderboard |
| [Polaris Hub](https://polarishub.io/) | Drug-discovery datasets, benchmarks and competitions | Not stated | Platform | Python API (polaris-lib) |
| [JARVIS-Leaderboard](https://pages.nist.gov/jarvis_leaderboard/) | Materials design methods (AI, DFT, force fields, QC, experiment) | 322 benchmarks | Benchmark | CSV/JSON via GitHub submissions |
| [ColabFit Exchange](https://materials.colabfit.org/) | MLIP training data (molecules and materials) | 500+ MLIP datasets | Platform | Parquet, extended XYZ |
| [CAS Common Chemistry](https://commonchemistry.cas.org/) | Chemical substances (names, CAS RNs, structures, basic properties) | ~500k substances | API | REST (search, detail, molfile export) with free API key |
| [Therapeutics Data Commons (TDC)](https://tdcommons.ai/) | Therapeutics ML datasets (ADMET, DTI, generation, retrosynthesis) | 66 datasets / 22 ADMET benchmarks | Benchmark | Python API |
| [Chemotion Repository](https://www.chemotion-repository.net/) | Reactions, molecules and analytical data (NMR, MS, IR) | ~24k datasets | Experimental | Web + DOIs per reaction/molecule/dataset |
| [MolSSI QCArchive](https://qcarchive.molssi.org/) | Quantum chemistry calculations and ML datasets | Not stated | Platform | QCPortal Python client; public ML server (ml.qcarchive.molssi.org) |
| [MPContribs](https://contribs.materialsproject.org/) | Community experimental and computational datasets linked to MP | Not stated | Platform | REST API (contribs-api.materialsproject.org); mpcontribs-client |
| [Materials Commons](https://materialscommons.org/) | Experimental and simulation materials data (structural materials) | 179 published datasets | Platform | Web, Python API, CLI |
| [ioChem-BD](https://www.iochem-bd.org/) | Computational chemistry results (homogeneous/heterogeneous catalysis, molecular QC) | ~313k items / 501 collections | Platform | CML; REST, RDF and OAI-PMH endpoints |
| [OpenKIM](https://openkim.org/) | Interatomic potentials and property tests | 1,532 models | Platform | KIM API (LAMMPS, ASE, GULP, DL_POLY); query.openkim.org |
| [NIST Interatomic Potentials Repository](https://www.ctcms.nist.gov/potentials/) | Classical interatomic potentials (EAM, MEAM, ADP, ReaxFF, etc.) | Not stated | Platform | Potential files; REST via potentials.nist.gov (CDCS) |
| [NFDI4Chem Search Service](https://search.nfdi4chem.de/) | Federated search over German chemistry data repositories | ~152k datasets | Platform | Web search (SPARQL link offered) |

## TODO
* Add all OpenQDC datasets https://www.openqdc.io/datasets
* Classify [Atomly](https://atomly.net/#/). A bit challenging with non-English
* Look into adding NOMAD for experimental data as well
* Add A Quantum-Chemical Bonding Database for Solid-State Materials Part 1: https://zenodo.org/records/8091844 Part 2: https://zenodo.org/records/8092187


---

### Other Links
* [Awesome Materials Informatics](https://github.com/tilde-lab/awesome-materials-informatics)
* [Awesome Chemistry Datasets](https://github.com/kjappelbaum/awesome-chemistry-datasets)
* [Best of Atomistic Machine Learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning)
* [Data Resources for Materials Science](https://github.com/sedaoturak/data-resources-for-materials-science)

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

### October 2026

Added 159 entries in one sweep covering July to October 2026, which no earlier update reached, plus earlier releases that were never listed, along with the two AgentFEM continuum-mechanics datasets (#46). 35 of the 159 were released or substantially updated in 2026. Highlights from July to October 2026: ELEMENTA, WBM-MatPES (resolves the WBM request in issue #2), MAD-1.6 and uMOF for universal potentials; the A-Lab Precursor Genome and the 4D-STEM Diffraction Benchmark for experimental data; OpenADMET PXR and CYP challenge data; MolDesignBench and MatSciFig for LLM agents; and the TIDE turbulence corpus.

This update also closes long-standing gaps: the standard MLIP training and generative benchmarks (MPtrj, sAlex, WBM, GNoME, OC22, ODAC25, Alex-MP-20, MP-20/Perov-5/Carbon-24), canonical molecular sets from the OpenQDC and quantum-machine.org TODOs (GEOM, SPICE 2, ANI-2x, QM7-X, MD17/rMD17, MD22, tmQM, nablaDFT), battery and spectroscopy references, MPDS in the proprietary table (issue #3), and three related awesome lists, including the one named in issue #8. It adds two new sections: Microstructure, Phase-Field & Continuum Mechanics, and APIs, Platforms & Leaderboards (OPTIMADE, ColabFit, OpenKIM, Garden and others). It resolves the ChemRxivQuest, USPTO-Reactions, MatSciKB, Materials Cloud, quantum-machine.org and gas-in-polymer TODOs; the ChemRxivQuest row now points to the released data (952 QA pairs, not 970). Release months are shown in parentheses. Each entry has a 🔗 Verify line with the data link and the paper or announcement.

#### 🧮 Computational Datasets (47 entries)
- **WBM-MatPES** (2026-09): Recomputes the WBM discovery test set with uniform MatPES PBE settings (no Hubbard U, no empirical corrections) so MatPES-trained potentials can be scored against a consistent reference; ships two hulls to expose false 'discoveries' and six pressure test sets. Covers the WBM request in issue #2; no paper or explicit data license yet. 🔗 Verify: https://alexandria.icams.rub.de/data/matpes/wbm/ · https://alexandria.icams.rub.de/data/matpes/wbm/README.md
- **uMOF** (2026-09): Largest r2SCAN-D4 MOF DFT set to date (empty and gas-loaded frameworks, EOS, finite-temperature MD) from the Persson group, paired with an LLM-mined experimental benchmark and fine-tuned MACE models. Fills the gap beyond CoRE MOF/QMOF/ODAC23 at a higher level of theory. 🔗 Verify: https://doi.org/10.6084/m9.figshare.33311829 · https://arxiv.org/abs/2608.28100
- **MAD-1.6 (r2SCAN)** (2026-08): Successor to the already-listed MAD (PBEsol, ~96k structures): recomputed with all-electron FHI-aims r2SCAN, extended to 102 elements, molecular clusters and adsorbed molecules, with uncertainty-based outlier removal (MAD-1.5 appeared Mar 2026). Best treated as an update/replacement of the existing MAD row. 🔗 Verify: https://archive.materialscloud.org/records/ffd5a-1hc37 · https://arxiv.org/abs/2603.02089
- **ELEMENTA (Kairos Materials)** (2026-07): Composition-complete DFT corpus built by random structure search over enumerated unary, binary and ternary formulas, so it is not tied to known prototypes; the public release covers all unary/binary chemistries plus small ternaries and the full magnetic-moment-scan Spin set. Already used to train Matbench Discovery entries; the full 210M-frame corpus stays private. 🔗 Verify: https://huggingface.co/datasets/kairosmaterial/ELEMENTA · https://doi.org/10.5281/zenodo.22638068
- **AM26 (Amorphous Materials)** (2026-07): Deringer group benchmark showing that current foundation MLIPs transfer poorly to disordered phases; provides melt-quench reference structures, DFT labels and leaderboard scripts. Fills a gap since most uMLIP benchmarks are crystalline. 🔗 Verify: https://github.com/vldgroup/AM26 · https://arxiv.org/abs/2607.11384
- **AdsZeo** (2026-07): Unlike isotherm-only screening sets, it stores the equilibrium molecule and cation coordinates behind each loading, enabling generative and density-estimation models of adsorbates in charged pores. 🔗 Verify: https://zenodo.org/records/21445386 · https://arxiv.org/abs/2608.08848
- **OrgReact** (2026-07): New low-barrier organic reactions enumerated from Transition1x reactants (about 90% not in Transition1x), with IRC-verified TSs at ωB97X-D/def2-TZVP plus DeePHF-extrapolated CCSD(T)-level energies (Scientific Data, Jul 2026). Useful as an out-of-distribution test set for TS generators and reactive potentials. 🔗 Verify: https://doi.org/10.6084/m9.figshare.31668682 · https://www.nature.com/articles/s41597-026-07771-6
- **LeMat-Rho** (2026-06): LeMaterial r2SCAN recalculations of AFLOW/OQMD/MP structures with compressed CHGCAR/AECCAR densities, Bader charges, forces and stresses; one of very few open charge-density sets for electron-density and charge-aware ML (first posted Jun 2025, updated Jun 2026). 🔗 Verify: https://huggingface.co/datasets/LeMaterial/LeMat-Rho · https://huggingface.co/datasets/LeMaterial/LeMat-Rho/blob/main/README.md
- **QuantumPioneer** (2026-05): Reaction-centered open-shell database with ωB97X-D/def2-SVP geometries, DLPNO-CCSD(T)-F12d single points, COSMO-RS solvation and TST kinetics for H-transfer chemistry (MIT Green group; JACS, Aug 2026). Fills the gap in radical thermochemistry, barrier heights and solvent effects at near-coupled-cluster accuracy. 🔗 Verify: https://zenodo.org/records/20060606 · https://dspace.mit.edu/handle/1721.1/173097
- **Reaction-QM** (2026-05): Million-scale reaction dataset that extends TS-level data beyond CHNO to second- and third-row elements, with full IRC trajectories for reactive MLIP training and barrier prediction (Scientific Data, Apr 2026). Complements Transition1x and RGD1 in chemical coverage. 🔗 Verify: https://zenodo.org/records/18551029 · https://www.nature.com/articles/s41597-026-07325-w
- **QCDGE-CI** (2026-05): First large-scale dataset of ground-state minima paired with S0/S1 minimum-energy conical-intersection geometries (OM2/MRCI, benchmarked against CASSCF), a key missing ingredient for ML models of nonadiabatic photochemistry. Extends the QCDGE excited-state database; arXiv v2 posted Sep 2026. 🔗 Verify: https://langroup.site/QCDGE_CI · https://arxiv.org/abs/2605.14287
- **AQVolt26** (2026-04): SandboxAQ dataset of high-temperature, strongly distorted halide configurations that exposes energy errors of foundation MLIPs in soft ionic conductors; co-training fixes them. The public HF repo is gated and appears to expose only a subset split. 🔗 Verify: https://huggingface.co/collections/SandboxAQ/aqvolt26 · https://arxiv.org/abs/2604.02524
- **SQuIRL** (2026-04): Harmonic IR frequencies, intensities and force constants for all QM9 molecules at ωB97X-D/aug-cc-pVTZ, a much higher level than earlier QM9 spectral sets (Scientific Data, Apr 2026). Training data for spectrum prediction and spectrum-to-structure models. 🔗 Verify: https://doi.org/10.6084/m9.figshare.30734843 · https://www.nature.com/articles/s41597-026-07240-0
- **HE26 (Heavy Elements)** (2026-03): First-principles data for elements absent from MPtrj/OMat24, used to extend MACE-Osaka26 to 97 elements; a small but unique coverage extension for universal potentials in nuclear applications. 🔗 Verify: https://doi.org/10.6084/m9.figshare.31429325 · https://arxiv.org/abs/2603.03223
- **MofasaDB (Orbital Materials)** (2025-11): Orbital Materials' public release of structures from its Mofasa generative model with Zeo++, MOFid and MOFChecker descriptors; a large resource for MOF generative modeling and screening. Geometries are relaxed with the ORB MLIP rather than DFT. 🔗 Verify: https://huggingface.co/datasets/Orbital-Materials/MofasaDB · https://mofux.ai/MOFASA.pdf
- **tmQMg*** (2025-10): TD-DFT (ωB97xd/def2SVP) excitation energies, oscillator strengths, NTO charge-transfer character and solvatochromic shifts for TMCs from the CSD, the largest open excited-state set for inorganic complexes (JCIM, Oct 2025). Supports ML for photocatalysts and dyes. 🔗 Verify: https://zenodo.org/records/17209767 · https://pubs.acs.org/doi/10.1021/acs.jcim.5c01958
- **ODAC25 (Open DAC 2025)** (2025-08): Successor to the listed ODAC23 with functionalized and synthetic frameworks, GCMC-derived high-energy placements and two extra adsorbates, labeled with PBE+D3; roughly doubles ODAC23 in size. HF download is gated (access request); ColabFit hosts mirrors. 🔗 Verify: https://huggingface.co/facebook/ODAC25 · https://arxiv.org/abs/2508.03162
- **Halo8** (2025-08): Largest open reaction-pathway dataset with halogens, computed at ωB97X-3c, filling the halogen gap left by Transition1x-style CHNO sets (Scientific Data, Oct 2025; correction Jan 2026). Directly relevant to pharmaceutical and materials reactivity, where halogens are ubiquitous. 🔗 Verify: https://zenodo.org/records/16737590 · https://pmc.ncbi.nlm.nih.gov/articles/PMC12537968/
- **OC20-mAds / OC20-Slabs** (2025-06): New OC20 extensions released with Meta's UMA model to capture coverage and co-adsorption effects and clean-surface energetics; part of the UMA training mixture. 🔗 Verify: https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20_mads.md · https://arxiv.org/abs/2506.23971
- **HORM (Hessians)** (2025-05): Largest open molecular Hessian dataset (ωB97x/6-31G(d)) sampled from Transition1x and RGD1 geometries, enabling Hessian-informed training of reactive MLIPs for TS search and vibrational analysis (Scientific Data, Dec 2025). 🔗 Verify: https://zenodo.org/records/17217897 · https://www.nature.com/articles/s41597-025-06350-5
- **QDπ Dataset** (2025-04): Actively-learned, de-duplicated union of several sources relabeled consistently at ωB97M-D3(BJ)/def2-TZVPPD (SPICE level), designed as compact MLIP training data for drug-like and biomolecular simulation (Scientific Data, Apr 2025). 🔗 Verify: https://zenodo.org/records/14970869 · https://www.nature.com/articles/s41597-025-04972-3
- **Alex-MP-20 (MatterGen)** (2025-01): Union of MP-20 and Alexandria re-relaxed with consistent PBE settings, released with MatterGen and now the de facto large training set for crystal generative models (DiffCSP, OMatG, etc.); the reference set enables stability/novelty (SUN) scoring. 🔗 Verify: https://github.com/microsoft/mattergen/tree/main/data-release · https://www.nature.com/articles/s41586-025-08628-5
- **tmQM** (2024): Canonical CSD-derived TMC dataset with GFN2-xTB geometries and TPSSh-D3BJ/def2-SVP energies, HOMO-LUMO gaps, dipoles and NBO charges; basis of tmQMg graphs and most inorganic-complex ML work. Listed on both OpenQDC and quantum-machine.org. 🔗 Verify: https://github.com/uiocompcat/tmQM · https://pubs.acs.org/doi/10.1021/acs.jcim.0c01041
- **MDR Phonon PBE (Alexandria)** (2024-12): PBE recalculation of the NIMS MDR phonon database used to show uMLIPs are 'ready for phonons'; a preprocessed 8,510-material Hessian subset for phonon fine-tuning (PFT, figshare 31049869) followed in Jan 2026. 🔗 Verify: https://alexandria.icams.rub.de/data/phonon_benchmark/ · https://arxiv.org/abs/2412.16551
- **sAlex (train + val)** (2024-10): Meta FAIR's de-duplicated Alexandria trajectory subset with all WBM-matching prototypes removed and frames kept only when energies differ by >10 meV/atom; the standard companion to OMat24 and MPtrj for leaderboard-compliant uMLIP training. Requested in issue #2. 🔗 Verify: https://huggingface.co/datasets/facebook/OMAT24#salex-dataset · https://arxiv.org/abs/2410.12771
- **nablaDFT / ∇²DFT** (2024-06): ωB97X-D/def2-SVP energies, forces, Hamiltonian and overlap matrices plus relaxation trajectories for MOSES-derived drug-like molecules; one of the few large sets supporting Hamiltonian/wavefunction learning alongside conformational optimization benchmarks. 🔗 Verify: https://github.com/AIRI-Institute/nablaDFT · https://arxiv.org/abs/2406.14347
- **OC20NEB** (2024-05): Converged nudged-elastic-band trajectories on OC20 surfaces from the CatTSunami work; the main open benchmark for MLIP-accelerated transition-state searches in heterogeneous catalysis. 🔗 Verify: https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20neb.md · https://arxiv.org/abs/2405.02078
- **MISATO** (2024-05): Couples curated experimental protein-ligand structures with explicit-water MD traces and semiempirical electronic properties, enabling dynamics-aware affinity and binding-site models (Nature Computational Science, May 2024). 🔗 Verify: https://zenodo.org/records/7711953 · https://www.nature.com/articles/s43588-024-00627-2
- **SPICE 2** (2024-04): Version 2 roughly doubles SPICE 1 (adds PubChem molecules, ~194k amino acid-ligand dimers, water clusters, solvated molecules, B and Si) at ωB97M-D3(BJ)/def2-TZVPPD; it is the training set behind the Nutmeg potentials. Supersedes SPICE 1 (listed via OpenQDC). 🔗 Verify: https://zenodo.org/records/10975225 · https://arxiv.org/abs/2406.13112
- **GNoME (DeepMind)** (2023-11): Google DeepMind's DFT-verified expansion of the convex hull, with summary energies, r2SCAN checks for binaries/ternaries and structures by composition; widely used as a reference hull and generative-model novelty set. Only the near-stable subset is public, not the ~89M-frame training corpus. 🔗 Verify: https://github.com/google-deepmind/materials_discovery · https://doi.org/10.1038/s41586-023-06735-9
- **ANI-2x** (2023-11): Active-learned off-equilibrium conformers extending ANI-1x to S, F and Cl; the 2023 Zenodo release adds relabelings at ωB97X/def2-TZVPP, ωB97M-D3BJ, ωB97M-V and B97-3c, making it a multi-fidelity benchmark. Repo lists ANI-1x/1ccx but not ANI-2x. 🔗 Verify: https://zenodo.org/records/10108942 · https://pubs.acs.org/doi/10.1021/acs.jctc.0c00121
- **MPtrj** (2023-07): The GGA/GGA+U relaxation-trajectory set from Materials Project used to train CHGNet and the default 'compliant' training set of Matbench Discovery; nearly every universal MLIP (MACE-MP, SevenNet, Orb, etc.) reports an MPtrj-only variant. 🔗 Verify: https://figshare.com/articles/dataset/23713842 · https://doi.org/10.1038/s42256-023-00716-3
- **Materials Cloud MC2D** (2023-06): 2D candidates obtained by screening layered 3D compounds for exfoliability, with relaxed monolayers and electronic properties; the 2023 ACS Nano expansion is the current release. Second part of the Materials Cloud TODO. 🔗 Verify: https://mc2d.materialscloud.org/ · https://doi.org/10.1021/acsnano.2c11510
- **PubChemQC B3LYP/6-31G*//PM6** (2023-05): Largest open DFT electronic-structure dataset of real molecules (orbital energies, dipoles, Mulliken charges); it is the parent of the OGB-LSC PCQM4Mv2 HOMO-LUMO benchmark (3.7M molecules) and many molecular pretraining corpora. Only the derived PubChemQCR is currently listed. 🔗 Verify: https://nakatamaho.riken.jp/pubchemqc.riken.jp/b3lyp_pm6_datasets.html · https://arxiv.org/abs/2305.18454
- **RGD1** (2023-03): Largest open CHNO TS dataset from graph-enumerated reactions at B3LYP-D3/TZVP with a CCSD(T)-F12 subset; standard training/OOD set for barrier prediction and TS generation, and source of HORM's OOD split. 🔗 Verify: https://doi.org/10.6084/m9.figshare.21066901 · https://www.nature.com/articles/s41597-023-02043-z
- **MD22** (2022-09): Large-system successor to MD17 (peptide, DHA, stachyose, DNA base pairs, buckyball catcher, double-walled nanotube) at PBE+MBD; standard test of MLIP accuracy and long-range interactions. Named in the quantum-machine.org TODO. 🔗 Verify: http://www.sgdml.org/ · https://arxiv.org/abs/2209.14865
- **OC22 (Open Catalyst 2022)** (2022-06): Oxide-surface sequel to OC20 trained on DFT total energies rather than adsorption energies (S2EF-Total, IS2RE-Total, IS2RS tasks); a standard component of UMA, SevenNet-Omni and other multi-domain potentials. OC20 and OC25 are listed but OC22 is missing. 🔗 Verify: https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc22.md · https://doi.org/10.1021/acscatal.2c05426
- **MPTS-52** (2022-06): Harder companion to MP-20 that splits by first-report date, so models must generate materials discovered after their training data; reported by DiffCSP, FlowMM and later CSP papers (now maintained in matbench-genmetrics). 🔗 Verify: https://figshare.com/articles/dataset/Materials_Project_Time_Split_Data/19991516 · https://github.com/sparks-baird/mp-time-split
- **GEOM** (2022-04): Energy-annotated CREST/GFN2-xTB conformer ensembles with Boltzmann weights (DFT for a BACE subset); the default training and evaluation set for 3D conformer generation and molecular generative models. Also served through OpenQDC. 🔗 Verify: https://doi.org/10.7910/DVN/JNGTDF · https://www.nature.com/articles/s41597-022-01288-4
- **MP-20 / Perov-5 / Carbon-24 (CDVAE)** (2021-10): The three standard splits introduced with CDVAE that virtually every crystal generative or CSP model (DiffCSP, FlowMM, MatterGen, CrystaLLM) still reports on: varied chemistry (MP-20), fixed prototype with varied composition (Perov-5) and fixed composition with varied structure (Carbon-24). 🔗 Verify: https://github.com/txie-93/cdvae/tree/main/data · https://arxiv.org/abs/2110.06197
- **OrbNet Denali** (2021-07): Paired ωB97X-D3/def2-TZVP and GFN1-xTB energies on near- and off-equilibrium geometries, enabling Δ-learning and semiempirical-to-DFT transfer for charged and drug-like species. Part of the OpenQDC collection. 🔗 Verify: https://doi.org/10.6084/m9.figshare.14883867 · https://arxiv.org/abs/2107.00299
- **QM7-X** (2021-02): Exhaustive sampling of GDB-13 isomers and their distorted geometries with 42 global and atomic properties at PBE0+MBD, a standard benchmark for multi-property and force learning. Named in the quantum-machine.org TODO. 🔗 Verify: https://zenodo.org/records/4288677 · https://www.nature.com/articles/s41597-021-00812-2
- **DES370K / DES5M** (2021-02): D. E. Shaw Research gold-standard interaction energies, the reference for training and benchmarking intermolecular terms of MLIPs and force fields. In the OpenQDC interaction collection; DES5M is at zenodo.org/records/5706002. 🔗 Verify: https://zenodo.org/records/5676266 · https://www.nature.com/articles/s41597-021-00833-x
- **WBM Test Set** (2021-01): Five rounds of chemically guided element substitution on MP structures followed by MP-compatible DFT relaxation; it is the prospective test set behind Matbench Discovery and the reference against which training sets are de-duplicated. Requested in issue #2; also reachable from the Matbench Discovery data page. 🔗 Verify: https://github.com/janosh/matbench-discovery/blob/main/data/wbm/readme.md · https://doi.org/10.1038/s41524-020-00481-6
- **MD17 / revised MD17 (rMD17)** (2020-07): The most widely reported MLIP energy/force benchmark; rMD17 recomputes MD17 structures at tight-convergence PBE/def2-SVP to remove numerical noise. Original MD17 is hosted at sgdml.org; named in the quantum-machine.org TODO. 🔗 Verify: https://doi.org/10.6084/m9.figshare.12672038 · https://arxiv.org/abs/2007.09593
- **OE62** (2020-02): Benchmark for orbital-energy and ionization-level prediction of realistic, larger organic molecules, including GW quasiparticle energies; widely used for organic semiconductor screening. 🔗 Verify: https://doi.org/10.14459/2019mp1507656 · https://www.nature.com/articles/s41597-020-0385-y
- **Materials Cloud MC3D**: Curated database of DFT-relaxed versions of experimentally known crystals from MPDS, COD and ICSD, computed with SSSP pseudopotentials and full AiiDA provenance. Resolves the Materials Cloud TODO together with MC2D. 🔗 Verify: https://mc3d.materialscloud.org/ · https://doi.org/10.1038/s41597-020-00637-5

#### 🧪 Experimental Datasets (30 entries)
- **4D-STEM Diffraction Benchmark** (2026-09): First large labelled benchmark of experimental 4D-STEM diffraction patterns with Bragg-disk annotations and acquisition metadata, plus baselines for disk detection and pattern analysis; code at github.com/Gaiya69-rgb/4D-ImageNet. Hosted on Science Data Bank; dataset license not stated in the paper. 🔗 Verify: https://doi.org/10.57760/sciencedb.nbsdc.00281 · https://arxiv.org/abs/2609.21593
- **PolyBench26** (2026-09): Unified open benchmark mixing experimental glass transition temperatures (PolyMetriX) with DFT and MD properties, with tasks for data scaling, repeat-unit complexity and transfer to unseen copolymer architectures. 🔗 Verify: https://github.com/rlearsch/PolymerBenchmark2026 · https://arxiv.org/abs/2609.27036
- **OpenADMET blind-challenge datasets** (2026): Three industry-grade ADMET sets released through OpenADMET blind challenges.
  - **CYP Inhibition / TDI** (2026-08): Octant-generated pIC50 and time-dependent-inhibition data for CYP1A2, CYP2C9, CYP2D6 and CYP3A4 from one consistent assay platform, released for the OpenADMET CYP blind challenge (launched 17 Aug 2026; test labels unblinded after 3 Nov 2026). Companion Octant CYP3A4/CYP2J2 inhibition and reactivity release (Mar 2026) is in the same HF org. 🔗 Verify: https://huggingface.co/datasets/openadmet/cyp-challenge-train-test · https://openadmet.ghost.io/announcing-openadmets-cyp-inhibition-blind-challenge/
  - **PXR** (2026-03): Largest open, single-assay PXR induction dataset (pEC50, Emax, counter-screen) plus 184 new PXR X-ray structures, released in full after the OpenADMET blind challenge closed on 1 Jul 2026; training split went public in Apr 2026. A rare prospective, industry-grade ADMET benchmark for drug-drug-interaction liability. 🔗 Verify: https://huggingface.co/datasets/openadmet/pxr-challenge-train-test · https://openadmet.ghost.io/its-the-end-of-the-pxr-challenge-as-we-know-it-and-i-feel-fine/
  - **ExpansionRx** (2026-01): Real drug-discovery ADMET data from Expansion Therapeutics' RNA-targeting programs (LogD, KSOL, HLM/MLM CLint, Caco-2 Papp and efflux, plasma/brain/muscle protein binding), fully released on 27 Jan 2026 after a 370+ participant blind challenge. Time-split, project-realistic test set rather than random public-data splits. 🔗 Verify: https://huggingface.co/datasets/openadmet/openadmet-expansionrx-challenge-data · https://openadmet.ghost.io/the-openadmet-expansionrx-blind-challenge-has-come-to-an-end/
- **Precursor Genome (A-Lab)** (2026-07): Pairwise solid-state reactions run autonomously by the Berkeley A-Lab, each with raw XRD, thermal profiles, recovered masses and expert-graded automated Rietveld phase fractions; a rare open record of failed and partial outcomes for learning reaction pathways and precursor selection (loader code at github.com/lauren-walters/precursor-genome). 🔗 Verify: https://doi.org/10.5281/zenodo.21285546 · https://arxiv.org/abs/2607.09903
- **RamanBench** (2026-05): Aggregates 74 public experimentally measured Raman datasets (16 released for the first time) behind one loader with standardized splits and a Hugging Face leaderboard; the companion raman-data package had grown to 93 datasets by its Sep 2026 release. 🔗 Verify: https://github.com/ml-lab-htw/RamanBench · https://arxiv.org/abs/2605.02003
- **EM3M** (2025-08): Raw SEM micrographs contributed by 60+ institutions with about 3 million expert instance-segmentation masks and structured text descriptions, supporting microstructure segmentation, captioning and text-to-image generation; paper revised July 2026. 🔗 Verify: https://huggingface.co/datasets/UniParser/EM3M · https://arxiv.org/abs/2508.16239
- **Runs N' Poses** (2025-02): Time-split, similarity-stratified benchmark showing that AF3-class co-folding models degrade on ligands and pockets unlike their training data; includes predictions and PoseBusters checks for major co-folding methods (Zenodo v6, Jan 2026). Standard reference for evaluating Boltz/AF3-style models. 🔗 Verify: https://zenodo.org/records/14794785 · https://www.biorxiv.org/content/10.1101/2025.02.03.636309v1
- **BatteryLife** (2025-02): Harmonized battery-degradation benchmark (KDD 2025) that merges 16 lab and industrial cycling datasets, including MATR/Severson, CALCE, HUST and RWTH, into one schema with life labels (990 cells: 837 Li-ion, 95 Zn-ion, 31 Na-ion, 27 industrial CALB); v12 (2026-07) added the 123-cell Farasis industrial pouch-cell set from the Nature 2026 Discovery Learning paper and the full XJTU data. 🔗 Verify: https://github.com/Ruifeng-Tan/BatteryLife · https://arxiv.org/abs/2502.18807
- **OBELiX** (2025-02): Curated benchmark pairing experimentally measured Li-ion conductivities with crystal structures and fixed splits (NRC Canada and Mila); fills the gap of experimental transport labels for structure-based battery-materials ML. 🔗 Verify: https://github.com/NRC-Mila/OBELiX · https://arxiv.org/abs/2502.14234
- **Papyrus** (2024-10): Standardized, deduplicated aggregation of ChEMBL, ExCAPE-DB and other sources with quality tiers (Papyrus++ for reproducible assays), ready for proteochemometric and QSAR modeling at scale. 🔗 Verify: https://zenodo.org/records/13787633 · https://link.springer.com/article/10.1186/s13321-022-00672-x
- **Leash BELKA** (2024-10): Largest public protein-small-molecule binding dataset (Big Encoded Library for Chemical Assessment), released in full with read counts and controls after the NeurIPS 2024 Kaggle competition; key for large-scale binding and DEL-denoising models. 🔗 Verify: https://polarishub.io/datasets/leash-bio/belka-v1 · https://leashbio.substack.com/p/belka-unleashed
- **MassSpecGym** (2024-10): NeurIPS 2024 benchmark built from curated experimental MS/MS libraries with scaffold-disjoint splits for de novo generation, retrieval and spectrum simulation; the reference benchmark for spectrum-to-structure models. 🔗 Verify: https://huggingface.co/datasets/roman-bushuiev/MassSpecGym · https://arxiv.org/abs/2410.23326
- **PLINDER** (2024-07): Largest annotated protein-ligand dataset with leakage-controlled splits (PL50, TIME, ECOD) and linked apo/predicted structures; now the standard training and evaluation resource for ML docking and co-folding models. 🔗 Verify: https://www.plinder.sh/ · https://www.biorxiv.org/content/10.1101/2024.07.17.603955v3
- **CALiSol-23** (2024-07): Largest open compilation of experimentally measured liquid-electrolyte conductivities, the standard training set for electrolyte formulation and conductivity models. 🔗 Verify: https://doi.org/10.11583/DTU.c.6929599.v1 · https://www.nature.com/articles/s41597-024-03575-8
- **RhNet Gas Sorption in Polymers** (2024-02): Literature-compiled experimental uptake of gases and vapors in polymers over wide pressure and temperature ranges, each row traceable to a source DOI and with predefined validation/test pairs; previously on the TODO list; fills the gap of experimental polymer sorption data. 🔗 Verify: https://github.com/Shorku/rhnet/tree/main/data · https://doi.org/10.1039/D3PY01028G
- **ProteinGym** (2023-12): Standard benchmark for protein language and fitness models with zero-shot and supervised leaderboards (v1.3 adds more baselines); complements the protein-design benchmarks already listed (PDBench, PDB-Struct). 🔗 Verify: https://proteingym.org · https://github.com/OATML-Markslab/ProteinGym
- **3DSC** (2023-11): Links experimental critical temperatures from SuperCon to 3D crystal structures, enabling structure-aware Tc prediction instead of composition-only models; complements the listed MDR SuperCon. 🔗 Verify: https://github.com/aimat-lab/3DSC · https://www.nature.com/articles/s41597-023-02721-y
- **PoseBusters Benchmark** (2023-08): De facto benchmark and validity test suite for ML docking and co-folding (AF3, Boltz, Chai all report PoseBusters success rates), checking physical plausibility in addition to RMSD. 🔗 Verify: https://zenodo.org/records/8278563 · https://github.com/maabuu/posebusters
- **MPEA Mechanical Properties** (2020-12): The standard curated table of experimentally measured HEA/MPEA hardness, yield and ultimate strength, elongation and observed phases, with test temperature and processing; the usual benchmark for alloy property ML (GitHub mirror CitrineInformatics/MPEA_dataset, archived 2024). 🔗 Verify: https://doi.org/10.6084/m9.figshare.12642953 · https://www.nature.com/articles/s41597-020-00768-9
- **AqSolDB** (2019-08): Curated, deduplicated aqueous solubility (logS) reference with reliability groups and RDKit descriptors; the standard solubility benchmark used in TDC and many property-prediction papers, larger and cleaner than ESOL. 🔗 Verify: https://doi.org/10.7910/DVN/OVHAW8 · https://www.nature.com/articles/s41597-019-0151-1
- **Toyota-Stanford-MIT Battery Cycle Life** (2019-03): The canonical early-prediction battery lifetime benchmark: full voltage, current and temperature traces for fast-charged LFP cells cycled to failure, the basis for most cycle-life ML papers and included as MATR in BatteryLife and BatteryML. 🔗 Verify: https://data.matr.io/1/ · https://www.nature.com/articles/s41560-019-0356-8
- **NIST Chemistry WebBook**: Long-standing evaluated reference for gas-phase thermochemistry, reaction energetics, ion energetics and reference IR/EI-MS/UV-Vis spectra; widely scraped as ground truth for spectrum-to-structure and thermochemistry ML. Data last updated 2025. 🔗 Verify: https://webbook.nist.gov/chemistry/ · https://data.nist.gov/pdr/lps/EBC9DB05EDEE5B0EE043065706812DF85
- **RRUFF**: Reference library of measured Raman, IR and XRD data on well-characterized mineral specimens (University of Arizona); the de facto training and test set for Raman and XRD phase identification models. 🔗 Verify: https://rruff.info · https://www.re3data.org/repository/r3d100010766
- **Battery Archive**: DOE-funded public repository that normalizes cycling and disruptive-test data from many labs into a common schema with browser visualization and the open Battery Lifecycle Framework; a primary source for cross-chemistry degradation ML. 🔗 Verify: https://www.batteryarchive.org · https://www.batteryarchive.org/study_summaries.html
- **SciGlass**: The largest compilation of measured glass properties (formerly a commercial product) now openly released; the standard training source for glass property models such as GlassNet and Tg/density/refractive index predictors. 🔗 Verify: https://github.com/epam/SciGlass
- **NIST ThermoML Archive**: NIST TRC archive of experimentally measured densities, vapor pressures, phase equilibria, heat capacities and related properties in a standard machine-readable XML schema; a primary source for force-field fitting (e.g. OpenFF) and thermophysical property ML. 🔗 Verify: https://trc.nist.gov/ThermoML/ · https://www.nist.gov/mml/acmd/trc/thermoml/thermoml-archive
- **NIST/ARPA-E ISODB**: Curated literature compilation of measured adsorption isotherms with standardized adsorbent and adsorbate identifiers and a JSON API; the main experimental counterpart to simulated MOF adsorption data such as MOFX-DB and ODAC. 🔗 Verify: https://adsorption.nist.gov/isodb/
- **nmrshiftdb2**: Long-running open, community-assigned NMR shift database; the classic training and test source for 13C/1H chemical-shift prediction and spectrum-to-structure models, complementary to the listed NMRexp. 🔗 Verify: https://nmrshiftdb.nmr.uni-koeln.de/
- **MassBank**: Open community mass-spectral library with versioned data releases on GitHub (v2026.03 in Apr 2026); a core public source behind MS/MS benchmarks and spectrum-to-structure models. 🔗 Verify: https://massbank.eu/MassBank/ · https://github.com/MassBank/MassBank-data
- **NIST XPS Database (SRD 20)**: Critically evaluated reference of photoelectron and Auger binding energies compiled from the literature (v5.0, data content last updated 2023); ground truth for automated XPS peak assignment and core-level shift prediction models. 🔗 Verify: https://srdata.nist.gov/xps/ · https://dx.doi.org/10.18434/T4T88K

#### 📚 LLM Training & Benchmark Datasets (19 entries)
- **MatSciFig** (2026-06): Large multimodal corpus of figure sub-panels with sub-captions, a 19-class visualization taxonomy and LLM-written scientific summaries, built for training and evaluating vision-language models on materials literature; a companion MaterialScope panel-detection set (2,811 annotated figures) is also on HF. 🔗 Verify: https://huggingface.co/datasets/CMEG-IITR/MatSciFig · https://arxiv.org/abs/2606.29667
- **MolDesignBench** (2026-05): Scenario-grounded design tasks that mix narrative requirements with explicit property and functional-group constraints, including deliberately infeasible specs the agent must flag; the best model succeeds on roughly 43% of cases. 🔗 Verify: https://huggingface.co/datasets/LG-AI-Research/MolDesignBench · https://arxiv.org/abs/2609.27349
- **SciAgentGym** (2026-02): Executable tool environment plus tiered SciAgentBench tasks for long-horizon scientific workflows, including chemistry and materials toolsets and multimodal cases; accepted at ICML 2026. 🔗 Verify: https://github.com/CMarsRover/SciAgentGYM · https://arxiv.org/abs/2602.12984
- **LABBench2** (2026-02): Successor to the already listed LAB-Bench from Edison Scientific (FutureHouse spin-out) with new LitQA3, ProtocolQA2, FigQA2/TableQA2 (image and PDF variants), PatentQA and cloning tasks; biology-centred; listed as the LAB-Bench update. 🔗 Verify: https://huggingface.co/datasets/EdisonScientific/labbench2 · https://advances.edisonscientific.com/benchmarks/labbench2/
- **FrontierScience** (2025-12): OpenAI's expert-level science benchmark with an olympiad track (IChO-level problems) and a rubric-graded research track; chemistry is a large share of the open gold set and it is now a standard frontier-model reporting benchmark. 🔗 Verify: https://huggingface.co/datasets/openai/frontierscience · https://arxiv.org/abs/2601.21165
- **MatCha** (2025-09): EMNLP 2025 multimodal benchmark spanning four stages of materials research (microscopy, diffraction, spectra and more); shows large gaps between MLLMs and human experts on characterization images. 🔗 Verify: https://huggingface.co/datasets/FreedomIntelligence/MatCha · https://arxiv.org/abs/2509.09307
- **MatQnA** (2025-09): Multiple-choice and open questions on interpreting real characterization data across ten techniques, complementing MaCBench for vision-language evaluation in materials. 🔗 Verify: https://huggingface.co/datasets/richardhzgg/matQnA · https://arxiv.org/abs/2509.11335
- **HLE Gold Bio/Chem** (2025-07): FutureHouse audit found about 29% of HLE text-only chemistry/biology answers conflict with the literature; this gold subset keeps only questions that passed expert and agent validation, making it the cleaner way to report HLE chemistry. 🔗 Verify: https://huggingface.co/datasets/futurehouse/hle-gold-bio-chem · https://www.futurehouse.org/research/hle-exam
- **ether0 Benchmark** (2025-06): FutureHouse test set for the ether0 RL-trained chemistry model where every answer is a molecule checked by programmatic verifiers (reaction prediction, constrained design, solubility edits, IUPAC to SMILES, safety/ADME MCQs); reward functions are open in github.com/Future-House/ether0. 🔗 Verify: https://huggingface.co/datasets/futurehouse/ether0-benchmark · https://arxiv.org/abs/2506.17238
- **ChemToolBench** (2025-06): Training and evaluation data for LLM tool learning over 137 chemistry/materials tools (CheMatAgent); used as the standard testbed by later tool-RL papers such as arXiv 2608.30952. 🔗 Verify: https://huggingface.co/datasets/RadiCat/ChemToolBench · https://arxiv.org/abs/2506.07551
- **MolLangBench** (2025-05): ICLR 2026 benchmark with deterministic, cheminformatics-checked labels that tests whether LLMs and VLMs can parse and manipulate molecular structure from text and images; frontier models still fail many simple editing and generation tasks. 🔗 Verify: https://huggingface.co/datasets/ChemFM/MolLangBench · https://arxiv.org/abs/2505.15054
- **ChemIQ** (2025-05): Short-answer (not multiple-choice) questions on graph interpretation, SMILES to IUPAC, NMR-based structure elucidation and SAR, each with an explicit verification method; a widely cited test of reasoning-model chemistry ability from Oxford OPIG. 🔗 Verify: https://github.com/oxpig/ChemIQ · https://arxiv.org/abs/2505.07735
- **MatTools** (2025-05): Evaluates whether LLMs can answer pymatgen questions and write executable materials-simulation code verified by automatic checkers, a direct test of materials-coding competence. 🔗 Verify: https://huggingface.co/datasets/SiyuLiu/MatTools · https://arxiv.org/abs/2505.10852
- **MolPuzzle** (2024): NeurIPS 2024 staged benchmark that walks LLMs through formula analysis, spectrum interpretation and full molecule assembly, a key reference point for spectra-to-structure reasoning. 🔗 Verify: https://huggingface.co/datasets/kguo2/MolPuzzle_data · https://github.com/KehanGuo2/MolPuzzle
- **TOMG-Bench** (2024-12): Covers molecule editing, optimization (LogP, MR, QED) and constraint-based custom generation scored with RDKit, plus an instruction-tuning set; widely used to compare chemistry LLMs on generation rather than retrieval. 🔗 Verify: https://huggingface.co/datasets/phenixace/S2-TOMG-Bench · https://arxiv.org/abs/2412.14642
- **LabSafety Bench** (2024-10): Safety-critical evaluation for lab-assistant and self-driving-lab agents, published in Nature Machine Intelligence (doi:10.1038/s42256-025-01152-1) and updated in Feb 2026. 🔗 Verify: https://huggingface.co/datasets/yujunzhou/LabSafety_Bench · https://arxiv.org/abs/2410.14182
- **ChemEval** (2024-09): Four-level, 13-dimension chemistry evaluation (25 tasks adapted from public data, 37 built with domain experts), expanded with a multimodal split for its ICLR 2026 version. 🔗 Verify: https://huggingface.co/datasets/Ooo1/ChemEval · https://github.com/USTC-StarTeam/ChemEval
- **CrystaLLM CIF Corpus** (2024-02): Ready-to-use text corpus and benchmark splits for training autoregressive LLMs on the CIF format (CrystaLLM, Nature Communications 2024); a common baseline for LLM crystal-generation benchmarks. 🔗 Verify: https://zenodo.org/records/10642388 · https://www.nature.com/articles/s41467-024-54639-7
- **ChEBI-20** (2021-11): The canonical molecule captioning and text-based molecule generation dataset used by MolT5, BioT5, Mol-Instructions and most chemistry LLM papers; a de facto standard. 🔗 Verify: https://github.com/cnedwards/text2mol · https://aclanthology.org/2021.emnlp-main.47/

#### 📖 Literature-mined & Text Datasets (12 entries)
- **SureChEMBL Bulk Data** (2026-10): EMBL-EBI's open patent chemistry resource: compounds text- and image-mined from WIPO, USPTO, EPO, JPO and CNIPA full texts, linked to patents, sections and LeadMine gene/disease annotations. It now ships only as bulk snapshots (weekly since Aug 2026, biweekly before; latest 2026-10-06), making it the main open counterpart to CAS/Reaxys patent data. 🔗 Verify: https://ftp.ebi.ac.uk/pub/databases/chembl/SureChEMBL/bulk_data/ · https://chembl.gitbook.io/surechembl/downloads/bulk-data
- **ORD USPTO Grants (uspto-grants)** (2026-06): Resolves the USPTO-Reactions TODO. The Open Reaction Database merged its 489 monthly USPTO grant shards into one dataset (ord_dataset-1158e351757f315b93cbcbe7bc55f38e) in June 2026 and serves it from a Hugging Face mirror with per-reaction patent provenance; the original Lowe figshare record (10.6084/m9.figshare.5104873, CC0, CML and SMILES 7z files) also still resolves. 🔗 Verify: https://huggingface.co/datasets/open-reaction-database/ord-data/viewer/uspto-grants · https://github.com/open-reaction-database/ord-data
- **LeMat-Synth** (2025-10): LLM/VLM-extracted synthesis protocols (text and figures) from arXiv, ChemRxiv and OMG papers, structured with an ontology covering 35 synthesis methods and 16 material classes; the authors call it the largest structured inorganic synthesis set. The HF data was refreshed in Aug 2026 alongside paper v2 (gated, license not stated on the card). 🔗 Verify: https://huggingface.co/datasets/LeMaterial/LeMat-Synth · https://arxiv.org/abs/2510.26824
- **NEMAD** (2025-10): LLM-extracted magnetic materials database (Nature Communications, Oct 2025) with ML-ready FM/AFM classification and Curie/Neel subsets at github.com/sumanitani/NEMAD-MagneticML; much larger and newer than the 2018 ChemDataExtractor Curie/Neel set. 🔗 Verify: https://www.nemad.org · https://www.nature.com/articles/s41467-025-64458-z
- **LLM-Agent Thermoelectric Dataset** (2025-09): Multi-agent GPT-4.1 extraction of thermoelectric properties together with crystal class, space group and doping, normalized to common units; published in Computational Materials Science vol. 265 (2026). Larger and richer in structure fields than the older ChemDataExtractor thermoelectric set. 🔗 Verify: https://cmeg-iitr.github.io/thermoelectric_dataset · https://doi.org/10.1016/j.commatsci.2026.114521
- **MatSKRAFT Knowledge Base** (2025-09): Table-mined database built with constraint-aware GNNs rather than LLMs, covering 18 properties and about 104K compositions missing from INTERGLAD/SciGlass; paper v2 appeared July 2026. Useful both as property training data and as a table-extraction benchmark (code at github.com/M3RG-IITD/MatSKRAFT). 🔗 Verify: https://doi.org/10.5281/zenodo.17064278 · https://arxiv.org/abs/2509.10448
- **MatSciKB** (2024-10): Resolves the MatSciKB TODO. The knowledge base behind the HoneyComb agent (EMNLP 2024 Findings) is shipped as a 50 MB JSON in the BangLab repo; the public file holds about 28,000 entries across 15 categories (arXiv abstracts, textbook passages, QA items, 57 formulas), fewer than the 38,469 in the paper, and no license is stated. 🔗 Verify: https://github.com/BangLab-UdeM-Mila/NLP4MatSci-HoneyComb/blob/main/honeycomb_framework/recall_layer/databases/knowledge_base.json · https://arxiv.org/abs/2409.00135
- **PolyIE** (2024-06): First expert-annotated SciIE benchmark for polymers (materials, properties, values, conditions plus relations), used to evaluate LLM extractors that build databases like Polymer Scholar. 🔗 Verify: https://github.com/jerry3027/PolyIE · https://aclanthology.org/2024.naacl-long.131
- **ORDerly** (2024-04): Reproducible cleaning of the ~1.7M USPTO reactions in ORD into forward, retro and the first open reaction-condition prediction benchmark, with non-USPTO test sets for generalization; the pip-installable pipeline (github.com/sustainable-processes/ORDerly) regenerates splits. Shows how uncleaned data inflates metrics. 🔗 Verify: https://figshare.com/articles/dataset/ORDerly_chemical_reactions_condition_benchmarks/23298467 · https://doi.org/10.1021/acs.jcim.4c00292
- **CO2 Reduction Electrocatalyst Corpus** (2024-04): One of the few open text-mined catalysis datasets, pairing a human benchmark corpus with an LLM-extended corpus (doi 10.57760/sciencedb.13292) and structured catalyst synthesis steps (10.57760/sciencedb.13293). 🔗 Verify: https://doi.org/10.57760/sciencedb.13290 · https://doi.org/10.1038/s41597-024-03180-9
- **MatKG** (2023-11): Largest open materials knowledge graph (Scientific Data 2024), linking materials to properties, applications, characterization and synthesis methods, with notebooks for Wikidata and Materials Project linking. A standard resource for KG-augmented LLMs and link prediction in materials. 🔗 Verify: https://zenodo.org/records/10144972 · https://github.com/olivettigroup/MatKG
- **ChemDataExtractor auto-generated databases (Cole group)** (2018–2022): Six rule-based literature-mined property databases built with ChemDataExtractor; links for each are below.
  - **Battery Materials DB** (2020-08): Flagship ChemDataExtractor auto-generated database and the most cited text-mined battery set; also the basis of BatteryBERT/BatteryDataExtractor work. Code at github.com/ShuHuang/batterydatabase. 🔗 Verify: https://doi.org/10.6084/m9.figshare.11888115 · https://doi.org/10.1038/s41597-020-00602-2
  - **Thermoelectric DB** (2022-10): Rule-based counterpart to the 2026 LLM thermoelectric set; each property is tied to its measurement temperature, useful for comparing extraction methods. 🔗 Verify: https://doi.org/10.6084/m9.figshare.19658787 · https://doi.org/10.1038/s41597-022-01752-1
  - **DSC & PSC Solar Cell DBs** (2022-06): Auto-generated device-level PV databases (PCE, Voc, Jsc, FF plus dyes, perovskites, electrodes); DSC part at doi 10.6084/m9.figshare.13516220. Complements the manually curated Perovskite Database Project already listed. 🔗 Verify: https://doi.org/10.6084/m9.figshare.13516238 · https://doi.org/10.1038/s41597-022-01355-w
  - **Band Gap DB** (2022-05): Largest literature-mined band gap set, a common experimental complement to DFT band gaps for ML; records keep the measurement temperature and source DOI. Code at github.com/QingyangDong-qd220/BandgapDatabase1. 🔗 Verify: https://doi.org/10.6084/m9.figshare.14079863 · https://doi.org/10.1038/s41597-022-01294-6
  - **Refractive Index & Dielectric DB** (2022-05): Text-mined optical property set that fills a gap left by DFT databases for dielectric and optical materials screening. 🔗 Verify: https://doi.org/10.6084/m9.figshare.12781142 · https://doi.org/10.1038/s41597-022-01295-5
  - **Curie/Néel Temperature DB** (2018-06): First large auto-generated magnetic transition database (semi-supervised Snowball extraction, ~73% precision), widely used for Curie temperature ML; code at github.com/cjcourt/magdb. 🔗 Verify: https://doi.org/10.6084/m9.figshare.c.3954418 · https://doi.org/10.1038/sdata.2018.111

#### 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets (16 entries)
- **TIDE** (2026-08): DNS corpus that varies one Navier-Stokes system along eight physics axes (15 configurations, 8 to 16 independent realizations each) with five benchmark tasks: forecasting, super-resolution, sparse reconstruction, pressure recovery and subgrid-stress closure. One of the few large 3D turbulence benchmarks released in the Jul to Oct 2026 window, with FNO, Transolver and DeepONet baselines. 🔗 Verify: https://huggingface.co/datasets/ydai17/TIDE · https://arxiv.org/abs/2608.04222
- **HiLiftAeroML** (2026-05): NVIDIA, Cadence and Boeing release of scale-resolving LES on 300M to 500M cell adapted grids for a high-lift transport configuration, positioned as the first open high-fidelity high-lift CFD dataset for surrogate training. Complements the already-listed NASA HLPW and CRM entries with ML-ready variant sweeps; card updated Sep 2026. 🔗 Verify: https://huggingface.co/datasets/nvidia/HiLiftAeroML · https://arxiv.org/abs/2605.19565
- **PDEInvBench** (2026-05): Benchmark for mapping observed solution fields back to physical parameters across five PDE systems, with in-distribution and two out-of-distribution evaluation tiers at multiple resolutions (TMLR 2026). Fills the inverse-problem gap that forward-only suites such as PDEBench do not cover. 🔗 Verify: https://huggingface.co/datasets/DabbyOWL/PDE_Inverse_Problem_Benchmarking · https://arxiv.org/abs/2605.25353
- **Luminary SHIFT-Crash / SHIFT-Battery** (2026-04): Luminary Cloud's growing family of parametric simulation datasets for 'physics AI'; the 2026 additions cover frontal crash of a morphed vehicle (time-resolved stress, strain and energy) and battery thermal management, both rare in open data. Access is gated and non-commercial. 🔗 Verify: https://huggingface.co/datasets/luminary-shift/SHIFT-Crash · https://huggingface.co/datasets/luminary-shift/Battery
- **WAKESET** (2026-02): Wake flow fields around an extra-large uncrewed underwater vehicle swept over speed (Re up to ~1.1e8) and turning angle, delivered as 128^3 volumetric grids plus planar slices with Python loaders. A 2026 open high-Re CFD set for surrogate modeling outside the usual automotive and airfoil domains. 🔗 Verify: https://huggingface.co/datasets/ZacharyCB99/WAKESET · https://arxiv.org/abs/2602.01379
- **SuperWing** (2025-12): Tsinghua and TUM dataset of parameterized 3D wings with surface and volumetric RANS solutions for data-driven aerodynamic design. Already adopted in the NVIDIA PhysicsNeMo 26.08 AeroJEPA example; card updated Sep 2026. 🔗 Verify: https://huggingface.co/datasets/yunplus/SuperWing · https://arxiv.org/abs/2512.14397
- **DrivAerStar** (2025-10): NeurIPS 2025 D&B dataset of industrial-grade car CFD (about 12M cells per case) hosted on Harvard Dataverse (doi:10.7910/DVN/UXVXQV). Used by the PhysicsNeMo-CFD surface uncertainty benchmark in release 26.08; dataset license not confirmed. 🔗 Verify: https://drivaerstar.github.io/ · https://arxiv.org/abs/2510.16857
- **BubbleML 2.0** (2025-07): Successor to BubbleML (NeurIPS 2023) released with the Bubbleformer forecasting model (NeurIPS 2025 spotlight), adding new fluids and flow-boiling configurations up to critical heat flux. The main open multiphase phase-change benchmark for neural operators. 🔗 Verify: https://huggingface.co/datasets/hpcforge/BubbleML_2 · https://arxiv.org/abs/2507.21244
- **The Well (Polymathic AI)** (2024-11): Curated collection of 16 large simulation datasets with a unified PyTorch loader, streaming from Hugging Face and benchmark baselines; it has become a default pretraining and evaluation corpus for PDE foundation models (Polymathic's Walrus checkpoints are trained on it). Latest package release v1.2.0 (Nov 2025). 🔗 Verify: https://github.com/PolymathicAI/the_well · https://arxiv.org/abs/2412.00568
- **FlowBench** (2024-09): Fully resolved simulations over procedurally generated shapes (harmonics, NURBS, skeleton) at up to 512x512 in 2D and 128^3 in 3D, aimed at geometry-aware neural operators. Complements car- and airfoil-specific sets with diverse generic geometries. 🔗 Verify: https://huggingface.co/datasets/BGLab/FlowBench · https://arxiv.org/abs/2409.18032
- **DrivAerML / AhmedML / WindsorML** (2024-08): Scale-resolving CFD on parametrically morphed DrivAer, Ahmed and Windsor bodies with surface/volume fields and force coefficients, now consolidated in the 'CAE ML Datasets' Hugging Face collection (cards updated Aug to Sep 2026). Widely used for training geometry-aware neural surrogates (e.g. in NVIDIA PhysicsNeMo). 🔗 Verify: https://huggingface.co/datasets/neashton/drivaerml · https://arxiv.org/abs/2408.11969
- **DrivAerNet++** (2024-06): NeurIPS 2024 D&B dataset covering fastback, notchback and estateback car designs with 26 shape parameters, surface and volume fields, part annotations and renders. The largest open multimodal car CFD set and a standard benchmark for 3D aerodynamic surrogates; note the non-commercial license. 🔗 Verify: https://dataverse.harvard.edu/dataverse/DrivAerNet · https://arxiv.org/abs/2406.09624
- **LagrangeBench** (2023-09): NeurIPS 2023 D&B suite of 2D and 3D SPH flows (Taylor-Green, Poiseuille, lid-driven cavity, dam break) with JAX GNN baselines. The standard particle-based counterpart to grid PDE benchmarks. 🔗 Verify: https://github.com/tumaer/lagrangebench · https://arxiv.org/abs/2309.16342
- **AirfRANS** (2022-12): NeurIPS 2022 D&B benchmark of steady incompressible RANS solutions over NACA-family airfoils with tasks on data scarcity, Reynolds generalization and angle-of-attack extrapolation; built into PyTorch Geometric. A canonical mesh-based CFD benchmark. 🔗 Verify: https://github.com/Extrality/AirfRANS · https://arxiv.org/abs/2212.07564
- **AgentFEM Material Loading Memory**: 3,788 synthetic elastoplastic loading histories across six separately documented releases, including multiaxial paths, material variation, long cycles, and 128 prospective sealed-test histories. Supports neural constitutive modeling and path-generalization studies; trajectories retain their published training, validation, development, and sealed-test roles. Open data under CC BY 4.0.
- **AgentFEM Controlled Transient Heat**: 64 finite-element thermal scenarios each branch from the same state into three control actions, yielding 192 complete trajectories with temperature fields, virtual sensors, controls, and numerical verification records. Scenario-grouped splits support action-conditioned forecasting and control-oriented surrogate research. Open data under CC BY 4.0.

#### 🔬 Microstructure, Phase-Field & Continuum Mechanics (new section) (12 entries)
- **CrackMNIST** (2026-02): DLR dataset from eight fatigue experiments on AA2024, AA7475 and AA7010 with crack-tip segmentation masks and stress-intensity-factor and T-stress labels, packaged at three resolutions with a pip-installable loader (Scientific Data 2026). Rare experimental benchmark for ML in fracture mechanics. 🔗 Verify: https://doi.org/10.5281/zenodo.18454958 · https://elib.dlr.de/225852/1/s41597-026-07722-1.pdf
- **Material Fracturing & Failure (LANL)** (2025-12): Scientific Data release of time-resolved crack evolution from randomized initial fracture patterns under uniaxial and biaxial tension, intended for foundation or surrogate models of material failure. By far the largest open fracture simulation corpus; HF repo updated Aug 2026. 🔗 Verify: https://huggingface.co/datasets/smartFRACs/material_fracturing · https://www.nature.com/articles/s41597-025-06412-8
- **Strained Alloy Microstructure (Materials Cloud)** (2025-07): Simulations of coherent alloy decomposition across misfit strains for both forward evolution prediction and inverse inference of the misfit parameter (Milano-Bicocca). Adds elasticity-coupled phase-field data, which existing benchmarks mostly omit. 🔗 Verify: https://archive.materialscloud.org/record/2025.117 · https://arxiv.org/abs/2507.21760
- **PFM-Fracture** (2025-07): Boston University benchmark built from 1,000 random initial crack configurations under two boundary conditions and three energy splits, offered at full resolution and 128x128, with PINN, FNO and UNet baselines. Targets robustness of fracture surrogates rather than raw volume. 🔗 Verify: https://dataverse.harvard.edu/dataverse/PFM-Fracture · https://arxiv.org/abs/2507.07237
- **SIFBench** (2025-06): Large tabular benchmark of FE-computed stress intensity factors for surface, corner and through cracks in plates and holes, with random forest, MLP and FNO baselines and a unified loader. Gives fracture-mechanics ML a standard regression benchmark at scale. 🔗 Verify: https://huggingface.co/datasets/tgautam03/SIFBench · https://arxiv.org/abs/2506.01173
- **OPMD (Open Phase-field Microstructure Dataset)** (2024): Latin-hypercube sweep of four phase-field model parameters with fixed train/test/validation splits, released with a community study benchmarking ML strategies for phase-field problems (Dingreville, Voorhees et al., MSMSE 2024). A standard test bed for microstructure-evolution surrogates, also hosted on Microstructures.net. 🔗 Verify: https://zenodo.org/records/16756795 · https://doi.org/10.1088/1361-651X/ad5f4a
- **LiFePO4 Phase-Field Benchmark (DTU)** (2024-11): Scientific Data benchmark of 2D spinodal decomposition trajectories over 10 domain sizes, 11 lithium concentrations and 10 random initializations, with baseline metrics and an out-of-distribution split. Links phase-field ML benchmarking to battery electrode materials. 🔗 Verify: https://doi.org/10.11583/DTU.25562364 · https://www.nature.com/articles/s41597-024-04128-9
- **MICRO2D** (2024-02): Large, statistically diverse microstructure library from the Kalidindi group with effective properties computed over a range of phase contrast ratios. A go-to dataset for structure-property homogenization surrogates and microstructure generative models (data on Google Drive). 🔗 Verify: https://arobertson38.github.io/MICRO2D · https://doi.org/10.1007/s40192-023-00340-4
- **Microstructure Evolution Phase-Field (Sandia/MDF)** (2023): Materials Data Facility collection of microstructure evolution trajectories grouped by four phenomena (Desai, Shrivastava, Dingreville). One of the few open sources covering grain growth and dendritic solidification together, directly relevant to latent-space and operator surrogates of mesoscale evolution. 🔗 Verify: https://acdc.alcf.anl.gov/mdf/detail/microstructure_evolution_phase_field_v1.1/ · https://doi.org/10.18126/ivdc-l57i
- **Inconel 718 3D Microstructure + Deformation** (2022-07): TriBeam serial-sectioned 3D orientation map co-registered with high-resolution DIC strain and slip fields under tension, plus voxel and FE meshes. A rare ground truth for validating crystal-plasticity and microstructure-to-response ML models. 🔗 Verify: https://doi.org/10.5061/dryad.83bk3j9sj · https://www.nature.com/articles/s41597-022-01525-w
- **Mechanical MNIST (collection)** (2019-12): Boston University (Lejeune lab) family of FEniCS benchmarks mapping MNIST-style stiffness patterns to displacement, force and damage fields, including uniaxial/equibiaxial/shear, Cahn-Hilliard, crack-path, multi-fidelity and distribution-shift variants. The canonical continuum-mechanics metamodel benchmark. 🔗 Verify: https://open.bu.edu/collections/61b965cd-064d-4e51-b31d-f7d784ee970b · https://open.bu.edu/items/c8346371-81b3-42f2-9741-22a6299a119c
- **Synthetic 3D Polycrystals + EVPFFT (Mangal & Holm)** (2018-06): Grain-wise microstructural descriptors paired with grain-averaged stress from elasto-viscoplastic FFT simulations of uniaxial tension (Data in Brief 2018; part two at 10.17632/nsfn6tw295.1). A small but frequently reused starting point for polycrystal stress hot-spot and GNN studies. 🔗 Verify: https://data.mendeley.com/datasets/kt8hfg4t2p/1 · https://doaj.org/article/b2976b541f9c441bb3468fae60739420

#### 🔒 Proprietary Datasets (for reference) (7 entries)
- **Pistachio (NextMove)** (2026-06): Reference only: the commercial successor to the open USPTO-Lowe extraction and the most common closed training set behind industrial retrosynthesis models; useful context next to Reaxys and CAS in the proprietary table. 🔗 Verify: https://www.nextmovesoftware.com/pistachio.html
- **MPDS / PAULING FILE**: Machine-readable access to the hand-curated PAULING FILE, the largest experimental inorganic database spanning structures, properties and phase diagrams; also sold by ASM International as the successor of its Alloy Phase Diagram Database and Pearson's Crystal Data. Requested in issue #3; its free subset is usable for ML benchmarking. 🔗 Verify: https://mpds.io · https://developer.mpds.io/
- **ICDD PDF-5+**: The industry-standard XRD phase-identification reference; the commercial baseline that open efforts such as opXRD, COD-derived simulated patterns and RRUFF are measured against. 🔗 Verify: https://www.icdd.com/pdf-5/
- **SpringerMaterials**: Expert-curated reference platform covering crystal structures, property values and binary/ternary phase diagrams, including the Landolt-Boernstein series and MSI Eureka collections; a common source of curated experimental values for alloy and inorganic ML when licensed. 🔗 Verify: https://materials.springer.com
- **MatNavi (NIMS)**: NIMS umbrella portal whose structural-materials data sheets (creep, fatigue, corrosion) and CCT diagrams are among the few long-term experimental mechanical datasets for steels and superalloys; PoLyInfo (already listed) is one of its databases. 🔗 Verify: https://mits.nims.go.jp/en/
- **SDBS (AIST)**: Japan AIST reference spectral collection measured in-house, widely used as ground truth for IR/NMR/MS interpretation; listed as a reference resource because its terms forbid bulk download for ML training (it is one source inside NMRGym-type aggregations). 🔗 Verify: https://sdbs.db.aist.go.jp · https://sdbs.db.aist.go.jp/Htmls/disclaimer_eng.html
- **Polymer Scholar** (2024-12): Largest LLM (GPT-3.5) plus MaterialsBERT extracted polymer property collection (Communications Materials 2024), browsable through Polymer Scholar 2.0; pipeline code at github.com/Ramprasad-Group/PromptDataExtraction. Bulk download terms are not stated (site has a login). 🔗 Verify: https://polymerscholar.org · https://doi.org/10.1038/s43246-024-00708-9

#### 🔌 APIs, Platforms & Leaderboards (new section) (18 entries)
- **LeMat-GenBench** (2026-02): Standardized metrics (stability, novelty, diversity and related measures) and a public leaderboard for inorganic crystal generators; public leaderboard launched Feb 2026 (paper Dec 2025, v2 Jan 2026). 🔗 Verify: https://huggingface.co/spaces/LeMaterial/LeMat-GenBench · https://arxiv.org/abs/2512.04562
- **OPTIMADE** (2025-12): Common REST API and filter grammar that lets one query run unchanged against Materials Project, AFLOW, OQMD, NOMAD, JARVIS, Alexandria, COD, Materials Cloud, MPDS and about 20 other providers. Spec v1.3.0 (Dec 2025) added a trajectories endpoint and Wyckoff/fractional-position fields; first published 2021. 🔗 Verify: https://www.optimade.org/ · https://doi.org/10.1038/s41597-021-00974-z
- **Garden (Globus Labs)** (2025-10): NSF-funded hub for citable, runnable models; the first release focused on MLIPs (MACE, MatterSim, SevenNet) served through TorchSim on HPC endpoints such as ALCF. Complements the dataset hubs by giving one-line access to models for evaluating them. 🔗 Verify: https://thegardens.ai/ · https://www.globus.org/blog/announcing-garden-hpc-ready-ai-powered-by-globus
- **MLIP Arena** (2025-09): Open benchmark that tests foundation MLIPs on physical behaviour (reactivity, stability under extreme conditions, thermodynamic properties) rather than DFT error alone; NeurIPS 2025 Datasets and Benchmarks spotlight, package v0.2.0 in Mar 2026. 🔗 Verify: https://huggingface.co/spaces/atomind/mlip-arena · https://arxiv.org/abs/2509.20630
- **LAMBench** (2025-04): Scores large atomistic models on force-field generalizability, domain property calculations, efficiency and MD stability. Complements the listed LAMBench-TrainingSet-v1. 🔗 Verify: https://www.aissquare.com/openlam?tab=Benchmark · https://arxiv.org/abs/2504.19578
- **Polaris Hub** (2024): Community hub that hosts curated, versioned drug-discovery benchmarks with standard splits and evaluation (e.g. BELKA-v1, Biogen ADME, RxRx3-core, Runs N' Poses, ASAP antiviral challenge), accessed through an open Python client. 🔗 Verify: https://polarishub.io/ · https://github.com/polaris-hub/polaris
- **JARVIS-Leaderboard** (2024-05): NIST community benchmark covering ML property prediction, electronic structure, force fields, quantum computing and experiments in one place. JARVIS-DFT and Matbench Discovery are listed, but this broader leaderboard is not. 🔗 Verify: https://pages.nist.gov/jarvis_leaderboard/ · https://doi.org/10.1038/s41524-024-01259-w
- **ColabFit Exchange** (2023-10): Largest open hub of DFT/CC datasets for fitting interatomic potentials (OpenKIM project), with a uniform schema and Hugging Face mirrors that include OC20/OC22, ODAC25 and MSR-ACC collections plus hundreds of smaller sets. An official colabfit-mcp server (PyPI, Oct 2025) adds agent search, download and MACE training. 🔗 Verify: https://materials.colabfit.org/ · https://doi.org/10.1063/5.0163882
- **CAS Common Chemistry** (2021): Open subset of the CAS Registry (listed only as proprietary) with a free API for resolving CAS numbers, SMILES and InChI; handy for identifier normalization when building chemistry datasets. 🔗 Verify: https://commonchemistry.cas.org/ · https://doi.org/10.1021/acs.jcim.2c00268
- **Therapeutics Data Commons (TDC)** (2021-02): Most widely used unified loader and leaderboard for molecular ADMET and drug-discovery tasks; its ADMET Benchmark Group is the standard comparison point for molecular property models. 🔗 Verify: https://tdcommons.ai/ · https://arxiv.org/abs/2102.09548
- **Chemotion Repository** (2020-09): KIT-hosted open repository of curated reactions with linked raw analytical spectra, each with a DOI; a growing source of experimental reaction and spectroscopy data for ML. 🔗 Verify: https://www.chemotion-repository.net/ · https://doi.org/10.1002/cmtd.202000034
- **MolSSI QCArchive** (2020-07): Server and client for storing and querying millions of QC results; its public ML server hosts ML training sets. QCPortal 0.71 released Oct 2026. 🔗 Verify: https://qcarchive.molssi.org/ · https://doi.org/10.1002/wcms.1491
- **MPContribs** (2019-05): Materials Project's platform where groups publish tabular, structure and attachment data keyed to MP materials, with DOIs and a Python client; a source of many smaller curated ML datasets not otherwise listed. 🔗 Verify: https://contribs.materialsproject.org/ · https://docs.materialsproject.org/services/mpcontribs
- **Materials Commons** (2016-07): University of Michigan (PRISMS Center, DOE BES) repository for storing, annotating and publishing materials research datasets with DOIs, plus a Python API and CLI; a common home for structural-materials experimental data. 🔗 Verify: https://materialscommons.org/ · https://doi.org/10.1007/s11837-016-1998-7
- **ioChem-BD** (2014-12): ICIQ/URV platform where groups publish full quantum chemistry outputs converted to CML alongside papers, exposed through REST and OAI-PMH; a large source of published reaction and catalysis calculations. 🔗 Verify: https://www.iochem-bd.org/ · https://doi.org/10.1021/ci500593j
- **OpenKIM** (2011-07): Curated, verified repository of classical and ML potentials with automated Crystal Genome property tests, useful as an evaluation reference for MLIPs. Active in 2026: MACE-MP-0a and PolyMLP portable models, new Gibbs free energy and thermal expansion test drivers, and Run Requests (Jul 2026). 🔗 Verify: https://openkim.org/ · https://doi.org/10.1007/s11837-011-0102-6
- **NIST Interatomic Potentials Repository** (2010-10): Long-running NIST collection of potential files with computed reference properties (iprPy/atomman), a standard baseline set for comparing ML potentials against classical ones. 🔗 Verify: https://www.ctcms.nist.gov/potentials/ · https://doi.org/10.1016/j.cossms.2013.10.001
- **NFDI4Chem Search Service**: Single entry point to MassBank spectra, Chemotion reactions, nmrXiv NMR and other NFDI chemistry repositories, useful for discovering experimental spectral data at scale. 🔗 Verify: https://search.nfdi4chem.de/ · https://www.nfdi4chem.de/


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
- **Quantum-Chemical Bonding DB (LOBSTER)**: Specialized dataset providing detailed bonding analysis for 13,800 solid-state compounds using LOBSTER methodology. Enables understanding of chemical bonding in crystalline materials through projected crystal orbital Hamilton populations and related descriptors.
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
