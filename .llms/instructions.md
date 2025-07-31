# Instructions for Adding Datasets to Awesome Materials & Chemistry Datasets

This guide provides clear instructions for LLMs to add new datasets to the repository following the established format and conventions.

## Dataset Categories

### 🧮 Computational Datasets
**Purpose**: DFT calculations, molecular dynamics simulations, quantum chemistry datasets, and computational benchmarks.
**Examples**: Materials Project, Open Catalyst, QM9, NOMAD, MS25

### 🧪 Experimental Datasets  
**Purpose**: Real experimental measurements, crystal structures, bioactivity data, and laboratory results.
**Examples**: Crystallography Open Database (COD), ChEMBL, PDBbind, HTEM-DB

### 📚 LLM Training Datasets
**Purpose**: Text-based datasets for training language models on scientific content, Q&A pairs, instructions.
**Examples**: ChemPile, SmolInstruct, MegaScience, ChemQA

### 📖 Literature-mined & Text Datasets
**Purpose**: Data extracted from scientific literature, patents, and text corpora.
**Examples**: PubChem, Open Reaction Database, MatScholar, PatCID

### 🌊 Physics & Engineering (PDE, CFD) Datasets
**Purpose**: Computational fluid dynamics, partial differential equations, engineering simulations.
**Examples**: PDEBench, BLASTNet, JHTDB, WeatherBench

### 🔒 Proprietary Datasets
**Purpose**: Reference-only listing of important commercial/restricted datasets.
**Examples**: CAS Registry, Reaxys, CSD (Cambridge)

## Table Format

All dataset tables follow this exact format:

```markdown
| [Dataset Name](link) | Domain | Size | Type | Format | License | Access |
```

### Field Guidelines

**Dataset Name**: Use the official name as it appears in publications/websites
**Link**: Direct link to dataset homepage, download page, or primary reference
**Domain**: Brief description of scientific area (e.g., "Small molecules", "Inorganic crystals")
**Size**: Specific numbers when available (e.g., "134k molecules", "1.2M relaxations")  
**Type**: Choose from: Computational, Experimental, LLM Training, Literature, Simulation, Benchmark, Mixed
**Format**: File formats (e.g., JSON, HDF5, CSV, CIF, SMILES)
**License**: Specific license (CC BY 4.0, MIT, Open) or "Proprietary"
**Access**: "Open" or "Restricted"

## Adding New Datasets

### Step 1: Determine Category
Read the dataset description and classify based on:
- **Computational**: Contains DFT/MD/quantum calculations
- **Experimental**: Real laboratory measurements
- **LLM Training**: Text data for language model training
- **Literature-mined**: Extracted from papers/patents
- **Physics/Engineering**: CFD/PDE simulations
- **Proprietary**: Commercial/restricted access

### Step 2: Add to Table
Insert alphabetically or at the end of the appropriate category table.

### Step 3: Update Changelog
Add entry to the current month's changelog section following this format:

```markdown
### [Month] 2025

[Brief summary of additions]

#### 🧮 Computational Datasets (X datasets)
- **Dataset Name**: Detailed description highlighting key features, size, methodology, and significance. Include specific metrics and capabilities where relevant.
```

## Changelog Guidelines

### Format
- Use emoji headers matching the dataset categories
- Count datasets accurately in parentheses  
- Write detailed descriptions (2-4 sentences) highlighting:
  - Dataset size and scope
  - Key methodologies or features
  - Scientific significance
  - Performance metrics if available

### Monthly Organization
- Create new month sections as needed
- Place newest months at the top
- Update summary line to reflect total additions

## Quality Standards

### Required Information
- ✅ Working link to dataset
- ✅ Clear domain description
- ✅ Specific size metrics when available
- ✅ Appropriate category placement

### Avoid
- ❌ Broken or unclear links
- ❌ Vague size descriptions ("large", "many")
- ❌ Wrong category placement
- ❌ Missing license information

## Examples

### Good Entry
```markdown
| [QM9](http://quantum-machine.org/datasets/) | Small organic molecules | 134k molecules with quantum properties | Computational | SDF/CSV | CC BY 4.0 | Open |
```

### Good Changelog Entry
```markdown
- **MS25**: Comprehensive benchmark dataset for evaluating machine learning interatomic potentials (MLIPs) across 6 diverse materials systems including MgO surfaces, liquid water, zeolites, catalytic Pt surface reactions, high-entropy alloys, and disordered Zr-oxides. Evaluates 5 MLIP architectures with focus on derived physical observables beyond traditional energy/force metrics.
```

## Special Cases

### Benchmark Datasets
Use "Benchmark" or "Benchmark/Comp" for Type field

### Multi-format Datasets  
List primary formats separated by "/" (e.g., "JSON/HDF5")

### Size Uncertainty
Use "~" for approximations (e.g., "~500k entries")

### License Unknown
Use "Open" if clearly open-access, "Proprietary" if restricted, blank if truly unknown

## Final Checklist

Before submitting:
- [ ] Dataset added to correct category table
- [ ] Table formatting preserved (pipe alignment)
- [ ] Changelog updated with detailed description
- [ ] All links functional
- [ ] No linting errors introduced
- [ ] Consistent formatting with existing entries