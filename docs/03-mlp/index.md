# 3. Multi-Layer Perceptron

Syllabus: Modules 4 and 5, Days 2 and 3.

These modules build a multi-layer perceptron from its parts and apply it to
classification, regression, and function approximation. Each theory page states the
result in a few paragraphs and then gives an interactive demo. The pages cover the
approximation result, the activation function, the loss, and how the network is trained.

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
- [MLP pile capacity](03b-mlp-pile-capacity-exercise.ipynb)
- [MLP function approximation](03c-mlp-function-approximation-exercise.ipynb)

## Data

[pile_bearing_capacity.csv](pile_bearing_capacity.csv) holds 100 rows from PHC nodular
pile load tests in Vietnam, covering 88 distinct pile configurations. Eleven rows repeat
another row's inputs with a different measured capacity. The file has 65 columns.

- `X1` to `X10` are pile geometry, elevations, pile length, and SPT N-values.
  `X9` is the total pile length in metres and equals `X2 + X3 + X4`, the sum of the tip,
  middle and top segment lengths. `X8` equals `X5 + X2 + X3 + X4`, the ground elevation
  plus the same three segment lengths. Both identities hold in 99 of the 100 rows. Row 24
  is the exception and is left as it stands in the source.
- `Pu_Experiment` is the measured axial capacity in MN. It is the target.
- `Est 1` to `Est 52` are the source paper's load-displacement estimates.
- `Pu_Prediction` is the source paper's own neural-network prediction of the capacity.
- `R_square` is that paper's fit statistic. It holds one value, 0.972895, in a single row
  and is empty in the other 99.

!!! warning "Do not train on `Pu_Prediction`"

    `Pu_Prediction` correlates 0.986 with `Pu_Experiment` because it is another model's
    estimate of the same quantity. Selecting "all numeric columns" as features leaks the
    target. Use only `X1` to `X10`. The same applies to `Est 1` to `Est 52` and to
    `R_square`.

Source: Nguyen, T., Ly, K.-D., Nguyen-Thoi, T., Nguyen, B.-P., and Doan, N.-P. (2022).
"Prediction of axial load bearing capacity of PHC nodular pile using Bayesian
regularization artificial neural network." *Soils and Foundations*, 62(5), 101203.
[doi:10.1016/j.sandf.2022.101203](https://doi.org/10.1016/j.sandf.2022.101203)

The tunnel boring machine files in `tbm/` are supplementary. No chapter 3 notebook, slide
or theory page reads them:
[shield_tunneling_risk_dataset.csv](tbm/shield_tunneling_risk_dataset.csv),
[tunnel_risk_dataset.csv](tbm/tunnel_risk_dataset.csv), and
[TBM-Supplementary material.xlsx](tbm/TBM-Supplementary%20material.xlsx).
