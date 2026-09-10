# Module 9: Physics-Informed Neural Networks

This module trains neural networks whose loss includes the residual of a governing
equation. The examples are a damped harmonic oscillator, a one-dimensional wave
equation compared against a finite difference solution, and one-dimensional
consolidation.

## Slides

- [Physics-informed neural networks](08-pinn-slides.pdf)

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [PINN oscillator](08a-pinn.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/08-pinn/08a-pinn-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/08-pinn/08a-pinn.ipynb)
- [1D wave equation: PINN vs finite difference](08b-pinn-forward.ipynb)  
  Notebook: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/08-pinn/08b-pinn-forward.ipynb)
- [1D consolidation](08c-1d-consolidation-pinns.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/08-pinn/08c-1d-consolidation-pinns-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/08-pinn/08c-1d-consolidation-pinns.ipynb)
- [1D consolidation with L-BFGS](08d-1d-consolidation-pinns-lbfgs.ipynb)  
  Notebook: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/08-pinn/08d-1d-consolidation-pinns-lbfgs.ipynb)

## Data

- [pinn_consolidation_model.pth](pinn_consolidation_model.pth): trained weights for the
  consolidation network.
