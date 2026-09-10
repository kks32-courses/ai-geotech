# Module 6: Recurrent Networks and LSTM

This module predicts the pore pressure response of liquefiable sand under cyclic
loading with a long short-term memory network. Saturated soil loaded cyclically during
an earthquake builds excess pore pressure, and the response shows a shielding effect:
pore pressure stops rising while the current stress amplitude stays below the largest
prior amplitude. Constitutive models such as PM4Sand and PDMY02 do not reproduce this
dependence on stress history. An LSTM learns it from the experimental records.

## Slides

- [Recurrent networks and LSTM](05-rnn-lstm-slides.pdf)
- [LSTM for liquefaction](05-lstm-liquefaction-slides.pdf)

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [LSTM liquefaction](05a-lstm-liquefaction.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/05-lstm/05a-lstm-liquefaction-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/05-lstm/05a-lstm-liquefaction.ipynb)

## Data

Cyclic simple shear tests on Nevada sand from Kwan et al. (2017), in the directories
`Experiment-8/` and `Experiment-9/`, also packaged as [data.zip](data.zip). Loose
samples have relative density 33 to 55 percent and dense samples 72 to 94 percent.
Loading is harmonic, modulated up, or modulated down.

Each CSV holds these columns:

- Time [sec]
- Shear Strain [%]
- Shear Stress [kPa]
- Effective Vertical Stress [kPa]
- Excess Pore Pressure [kPa]

The notebook computes relative density Dr [%] and the pore pressure ratio
ru = excess pore pressure / confining pressure.

## Network

The input is a window of 800 time steps with three channels: normalized time,
normalized shear stress, and relative density. The window spans about two loading
cycles. The stack is two LSTM layers of 128 units, then dense layers of 64 and 16
units with tanh activations, then a single tanh output. The target is ru at the time
step after the window.

## References

1. Choi, Y., and Kumar, K. (2023). "A Machine Learning Approach to Predicting Pore
   Pressure Response in Liquefiable Sands under Cyclic Loading." Geo-Congress 2023.
2. Hochreiter, S., and Schmidhuber, J. (1997). "Long Short-Term Memory." Neural
   Computation, 9(8), 1735-1780.
3. Kwan, W. S., Sideras, S. S., Kramer, S. L., and El Mohtar, C. (2017). "Experimental
   Database of Cyclic Simple Shear Tests under Transient Loadings." Earthquake
   Spectra, 33(3), 1219-1239.
