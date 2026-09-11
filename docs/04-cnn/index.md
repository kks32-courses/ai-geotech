# 4. Convolutional Neural Networks

Syllabus: Module 6, Day 3.

This module covers convolution and pooling layers and two applications: classifying
soil images, and inverting surface-wave dispersion images for a 2D shear wave velocity
section. Both networks are trained from scratch.

## Slides

- [Convolutional neural networks](04-cnn-slides.pdf)

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [Soil image classification](04a-cnn-soil-classification.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/04-cnn/04a-cnn-soil-classification-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/04-cnn/04a-cnn-soil-classification.ipynb)
- [Dispersion image to 2D Vs section](04b-cnn-fwi-velocity.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/04-cnn/04b-cnn-fwi-velocity-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/04-cnn/04b-cnn-fwi-velocity.ipynb)

## Data

- [Soil types.zip](Soil%20types.zip): labelled photographs of black, cinder, laterite,
  peat, and yellow soils. 156 images across the five classes.
- Hugging Face dataset [`kks32/cnn-dataset`](https://huggingface.co/datasets/kks32/cnn-dataset):
  12 HDF5 files of about 142 MB each, 500 samples per file. Each sample pairs a
  frequency-velocity dispersion image of shape (400, 76), holding 400 phase velocities
  from 100 to 1000 m/s by 76 frequencies from 5 to 80 Hz, with a 2D Vs section of shape
  (24, 48), 24 depth pixels by 48 lateral pixels. Notebook 04b uses 10 files for
  training and 2 for testing.
