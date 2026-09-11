# 6. Clustering

Syllabus: Module 7, Day 3.

This module groups cone penetration test profiles into soil layers without labels. It
covers k-means, DBSCAN, and agglomerative clustering with a tri-diagonal connectivity
matrix, which is the one method of the three that keeps a layer vertically contiguous.
The feature space is two-dimensional, qc1Ncs and Ic, so nothing is reduced before
clustering.

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [Fetch CPT data from the DesignSafe API](06a-fetch-cpt-data-dapi.ipynb)  
  Reference only. This notebook needs a DesignSafe account and a live MySQL connection
  to the NGL host, neither of which exists in Colab, so it ships without outputs. Its
  results are the two data files below. Run it from a DesignSafe Jupyter server if you
  want to fetch the data yourself.
- [Clustering analysis](06b-clustering-analysis.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/06-clustering/06b-clustering-analysis-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/06-clustering/06b-clustering-analysis.ipynb)

## Data

- [cpt_summary.csv](cpt_summary.csv): one row per CPT sounding with site and test
  name, number of measurements, maximum depth, and the minimum, maximum, and mean of
  qc, Ic, and qc1Ncs.
- [all_cpt_profiles.pkl](all_cpt_profiles.pkl): the full measured profiles, pickled.
  64 soundings from Wildlife Array, Moss Landing Marine Lab, and Jefferson Ranch,
  11,191 measurement points in total. Points where Qtn or Fr fell outside the range of
  Robertson's chart carry NaN in Ic, and notebook 06b drops them before clustering.
