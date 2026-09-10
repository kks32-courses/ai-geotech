# Module 7: Clustering

This module groups cone penetration test profiles into soil layers without labels. It
covers k-means, DBSCAN, agglomerative clustering, and principal component analysis for
dimensionality reduction and plotting.

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [Fetch CPT data from the DesignSafe API](06a-fetch-cpt-data-dapi.ipynb)  
  Notebook: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/06-clustering/06a-fetch-cpt-data-dapi.ipynb)
- [Clustering analysis](06b-clustering-analysis.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/06-clustering/06b-clustering-analysis-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/06-clustering/06b-clustering-analysis.ipynb)

## Data

- [cpt_summary.csv](cpt_summary.csv): one row per CPT sounding with site and test
  name, number of measurements, maximum depth, and the minimum, maximum, and mean of
  qc, Ic, and qc1Ncs.
- [all_cpt_profiles.pkl](all_cpt_profiles.pkl): the full measured profiles, pickled.
