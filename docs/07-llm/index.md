# Module 8: Large Language Models

This module calls a large language model from Python for geotechnical tasks: computing
bearing capacity, splitting that computation across cooperating agents, and answering
questions from a set of site investigation reports with retrieval-augmented
generation. The notebooks read OPENAI_API_KEY from a `.env` file in this folder, and
prompt for the key if the file is missing.

## Slides

- [Large language models](07-llm-slides.pdf)

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [Direct API calls](07a-llm-bearing-capacity-direct.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07a-llm-bearing-capacity-direct-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07a-llm-bearing-capacity-direct.ipynb)
- [Multi-agent calculator, four cooperating agents in plain Python](07b-llm-bearing-capacity-agents.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07b-llm-bearing-capacity-agents-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07b-llm-bearing-capacity-agents.ipynb)
- [RAG over geotechnical reports](07c-llm-rag-geotechnical.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07c-llm-rag-geotechnical-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07c-llm-rag-geotechnical.ipynb)

## Data

The retrieval corpus is four PDFs in `docs/`, also packaged as [docs.zip](docs.zip):

- [Geotech Report.pdf](docs/Geotech%20Report.pdf)
- [GeotechnicalInvestigationReport.pdf](docs/GeotechnicalInvestigationReport.pdf)
- [gpt-bearing-capacity.pdf](docs/gpt-bearing-capacity.pdf)
- [TERRACON_FINALV5.pdf](docs/TERRACON_FINALV5.pdf)
