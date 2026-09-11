# 7. Large Language Models

Syllabus: Module 8, Day 4.

This chapter goes from one API call, to retrieval over four site investigation reports,
to a small agent that reads a report, finds the soil parameters, and checks a bearing
capacity with a calculation tool.

The notebooks run on Google Colab. Store the key as a Colab secret named `OPENAI_API_KEY`
(the key icon in the left toolbar), or locally in a `.env` file in this folder. Each notebook
opens with the steps.

## Slides

- [Large language models](07-llm-slides.pdf)

## Notebooks

Each notebook opens in Google Colab. The exercise has blanks to fill in; the solution is the
completed notebook.

- [One API call](07a-llm-api-call.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07a-llm-api-call-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07a-llm-api-call.ipynb)
- [RAG over geotechnical reports](07b-llm-rag-geotechnical.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07b-llm-rag-geotechnical-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07b-llm-rag-geotechnical.ipynb)
- [Report-reading agent with tools](07c-llm-report-agent.ipynb)  
  Exercise: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07c-llm-report-agent-exercise.ipynb) Solution: [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=flat-square&logo=googlecolab)](https://colab.research.google.com/github/kks32-courses/ai-geotech/blob/main/docs/07-llm/07c-llm-report-agent.ipynb)

## Data

The retrieval corpus is four PDFs in `docs/`, also packaged as [docs.zip](docs.zip):

- [Geotech Report.pdf](docs/Geotech%20Report.pdf)
- [GeotechnicalInvestigationReport.pdf](docs/GeotechnicalInvestigationReport.pdf)
- [gpt-bearing-capacity.pdf](docs/gpt-bearing-capacity.pdf)
- [TERRACON_FINALV5.pdf](docs/TERRACON_FINALV5.pdf)

The agent example uses the Terracon report, which states a friction angle of 29 to 30
degrees, cohesion of 432 to 539 psf, groundwater at 24 ft, and an allowable bearing
pressure of 2,000 psf for footings under 9 ft wide.
