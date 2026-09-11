# 2. Explainable AI

Syllabus: Module 3, Day 1.

This module explains what the tree models of Chapter 1 have learned. SHAP attributes each
prediction to its input features. The Explainable Boosting Machine is a glass-box model
whose shape functions can be read, checked against soil mechanics, and edited. Both use
the Christchurch lateral spreading dataset.

## Slides

- [Introduction and exploratory analysis lecture deck](../01-dtree/01-intro-eda-slides.pdf):
  the SHAP and EBM material starts at slide 22.

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [SHAP section of the classification notebook](../01-dtree/01b-classification.ipynb)  
  Notebook: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/01-dtree/01b-classification.ipynb)
- [Explainable Boosting Machine](02a-ebm.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/02-xai/02a-ebm-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/02-xai/02a-ebm.ipynb)

## Data

- [RF_YN_Model3.csv](../01-dtree/RF_YN_Model3.csv): the lateral spreading dataset
  described in [Chapter 1](../01-dtree/index.md).
