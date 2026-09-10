# Modules 4 and 5: Multi-Layer Perceptron

These modules build a multi-layer perceptron from its parts and apply it to
classification, regression, and function approximation. The theory pages cover the
approximation result, the activation function, the loss, and how the network is
trained.

## Slides

- [Multi-layer perceptron](03-mlp-slides.pdf)

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [MLP classification](03a-mlp-classification.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/03-mlp/03a-mlp-classification-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/03-mlp/03a-mlp-classification.ipynb)
- [MLP pile capacity](03b-mlp-pile-capacity.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/03-mlp/03b-mlp-pile-capacity-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/03-mlp/03b-mlp-pile-capacity.ipynb)
- [MLP function approximation](03c-mlp-function-approximation.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/03-mlp/03c-mlp-function-approximation-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/03-mlp/03c-mlp-function-approximation.ipynb)
- [MLP extrapolation](03d-mlp-extrapolation.ipynb)  
  Notebook: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/03-mlp/03d-mlp-extrapolation.ipynb)

## Theory

- [Universal approximation theorem](uat.md)
- [Activation function ReLU](relu.md)
- [Binary cross entropy](bce.md)
- [Automatic differentiation](ad.md)
- [Gradient descent](sgd.md)

## Exercises

- [MLP classification](03a-mlp-classification-exercise.ipynb)
- [MLP function approximation](03c-mlp-function-approximation-exercise.ipynb)
- [MLP pile capacity](03b-mlp-pile-capacity-exercise.ipynb)

## Data

- [pile_bearing_capacity.csv](pile_bearing_capacity.csv): 100 pile load tests in
  Vietnam. Columns X1 to X10 are pile geometry, elevations, and SPT N-values, and
  Pu_Experiment is the measured axial capacity in MN.
- Tunnel boring machine datasets in `tbm/`:
  [shield_tunneling_risk_dataset.csv](tbm/shield_tunneling_risk_dataset.csv),
  [tunnel_risk_dataset.csv](tbm/tunnel_risk_dataset.csv), and
  [TBM-Supplementary material.xlsx](tbm/TBM-Supplementary%20material.xlsx).
