# LSTM for Predicting Pore Pressure in Liquefaction

This notebook demonstrates the use of Long Short-Term Memory (LSTM) neural networks to predict pore pressure response in liquefiable sands under cyclic loading.

## Overview

**Problem:** During earthquakes, saturated soils experience cyclic loading that can lead to liquefaction. The pore pressure response exhibits the "shielding effect" - where pore pressure does not increase when the current stress amplitude is lower than the peak prior amplitude.

**Challenge:** Traditional constitutive models (PM4Sand, PDMY02) fail to capture this stress history-dependent behavior.

**Solution:** LSTM networks can learn the shielding effect directly from experimental data.

## Notebooks

- `lstm-liquefaction.ipynb` - Main notebook with complete implementation and explanations
- `lstm-liquefaction-exercise.ipynb` - Exercise version for students (to be created)

## Data

### Experimental Data
The model is trained on cyclic simple shear tests from:
- **Source:** Kwan et al. (2017) - Experimental Database of Cyclic Simple Shear Tests
- **Location:** `Experiment-8/` and `Experiment-9/` directories
- **Soil:** Nevada sand
- **Conditions:**
  - Loose samples: Dr = 33-55%
  - Dense samples: Dr = 72-94%
  - Loading types: Harmonic, Modulated-up, Modulated-down

### Data Format
CSV files with the following columns:
- Time [sec]
- Shear Strain [%]
- Shear Stress [kPa]
- Effective Vertical Stress [kPa]
- Excess Pore Pressure [kPa]

Computed variables:
- Relative Density Dr [%]
- Pore pressure ratio: ru = Excess Pore Pressure / Confining Pressure

## Code Structure

### lstm-liquefaction Directory
Contains the original Python implementation:
- `model.py` - LSTM model architecture
- `train.py` - Training script
- `preparedata.py` - Data preprocessing functions
- `cssdata.py` - CSV data loading utilities
- `result_plot_tools.py` - Visualization functions
- `input.json` - Configuration file
- `requirements.txt` - Python dependencies

## Key Concepts

### LSTM Architecture
```
Input (batch, 800, 3)
    ↓
LSTM Layer 1 (128 units, return_sequences=True)
    ↓
LSTM Layer 2 (128 units)
    ↓
Dense Layer 1 (64 units, tanh)
    ↓
Dense Layer 2 (16 units, tanh)
    ↓
Output (1 unit, tanh) → ru prediction
```

### Features
- **Time history:** Normalized time steps
- **Stress history:** Normalized shear stress over 800 time steps (≈ 2 cycles)
- **Relative density:** Soil density (constant for each test)

### Target
- **Pore pressure ratio (ru):** Value at the next time step after the window

## Results

The LSTM model successfully:
- ✅ Captures the shielding effect in modulated-down loading
- ✅ Predicts accurate time to liquefaction
- ✅ Models density effects (loose vs dense sand)
- ✅ Reproduces pore pressure fluctuations

## References

1. Choi, Y., and Kumar, K. (2023). "A Machine Learning Approach to Predicting Pore Pressure Response in Liquefiable Sands under Cyclic Loading." Geo-Congress 2023.

2. Hochreiter, S., and Schmidhuber, J. (1997). "Long Short-Term Memory." Neural Computation, 9(8), 1735-1780.

3. Kwan, W. S., Sideras, S. S., Kramer, S. L., and El Mohtar, C. (2017). "Experimental Database of Cyclic Simple Shear Tests under Transient Loadings." Earthquake Spectra, 33(3), 1219-1239.

## Dependencies

```bash
pip install tensorflow numpy pandas matplotlib scikit-learn
```

See `lstm-liquefaction/requirements.txt` for specific versions used in the original implementation.

## Usage

1. Open the notebook: `lstm-liquefaction.ipynb`
2. Follow the step-by-step explanations
3. Run each cell to reproduce the results
4. Experiment with different hyperparameters

## Learning Objectives

After completing this notebook, you will understand:
- Why standard models fail for history-dependent behavior
- How LSTM networks capture sequential dependencies
- Time-window sampling for sequence prediction
- Training and evaluating LSTM models for geotechnical applications
- Limitations and future directions of data-driven approaches

## PDF Manuscript

See `lstm-liquefactinon.pdf` for the complete research paper describing this work.
