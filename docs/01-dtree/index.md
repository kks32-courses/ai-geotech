# Modules 1 and 2: Data and Tree-Based Classification

These modules cover exploratory data analysis of geotechnical datasets and tree-based
classifiers: decision trees, random forests, and XGBoost. The running example is lateral
spreading from the 2011 Christchurch earthquake. Explainability of these models continues
in [Module 3](../02-xai/index.md).

## Slides

- [Introduction and exploratory analysis lecture deck](01-intro-eda-slides.pdf)
- [Exploratory data analysis](01-eda-slides.pdf)
- [Tree-based classification](01-classification-slides.pdf)

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [Exploratory data analysis](01a-eda-liquefaction.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/01-dtree/01a-eda-liquefaction-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/01-dtree/01a-eda-liquefaction.ipynb)
- [Classification: decision tree, random forest, XGBoost](01b-classification.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/01-dtree/01b-classification-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/01-dtree/01b-classification.ipynb)

## Data

- [RF_YN_Model3.csv](RF_YN_Model3.csv): lateral spreading observations from Durante and
  Rathje (2021), Christchurch earthquake. Features are groundwater depth GWD (m),
  distance to the free face L (km), ground Slope (%), and peak ground acceleration
  PGA (g). The target is binary: 0 for no spreading, 1 for spreading.
