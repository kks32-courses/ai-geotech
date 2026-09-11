# AI in Geotechnical Engineering

**Dr. Krishna Kumar and Dr. Ellen Rathje, University of Texas at Austin**

## Course overview

The [lecture slides](2025-AI-Geotech.pdf) introduce machine learning in geotechnical
engineering in 49 pages. The [course agenda](TexasEEE-AI-Geotech.pdf) lists the modules
and the daily schedule.

This 20-hour online course enables geotechnical professionals with practical AI skills. Participants master data processing, feature engineering, and core machine learning models for classification, regression, and clustering. The curriculum explores deep learning, including various neural networks (DNN, RNN, CNN), vital explainable AI (XAI) techniques and Large Language Models for geotechnical applications. Through hands-on exercises with industry tools, attendees tackle real-world geotechnical challenges, from site characterization to knowledge management. Participants will be equipped to apply AI to enhance analysis, improve decision-making, and drive innovation in geotechnics.

### Course Introduction Video

[![Course Introduction](https://img.youtube.com/vi/vOO85acoXmQ/0.jpg)](https://youtu.be/vOO85acoXmQ?si=P6IXBZlIdp1TBgeh)

*Click the image above to watch the course introduction video*

## Learning Outcomes

Apply a range of machine learning and deep learning algorithms (including regression, classification, clustering, and various neural networks) to analyze and solve practical geotechnical engineering problems.

- Process, prepare, and engineer features from diverse geotechnical datasets (such as borehole logs, CPT/SPT data, lab tests, and time-series measurements) for effective AI model development.

- Develop, train, and evaluate predictive models for tasks such as soil classification, landslide susceptibility, site characterization, TBM performance optimization, and time-dependent behavior analysis.

- Interpret complex AI model outputs using Explainable AI (XAI) techniques like SHAP and leverage "glass-box" models to enhance decision-making and build trust in AI-driven geotechnical solutions.

- Implement advanced AI techniques, including Recurrent Neural Networks for time-series data, Large Language Models (LLMs) for knowledge management, and Convolutional/Graph Neural Networks for specialized geotechnical data analysis, while considering ethical implications and emerging trends.

## Day 1:

### Module 1: Introduction, Data Processing, and Feature Engineering (10am-noon)

**Theme:** Laying the groundwork for AI in geotechnics, from understanding data to preparing it for modeling.

**Presentations**
- Introduction to AI/ML/DL in Geotechnical Engineering (30min)
- Data Processing and Exploration (EDA, missing data, normalization)
- Feature Engineering for Geotechnical Data

**Demo examples:** Perform exploratory data analysis on the Christchurch lateral spreading dataset: 7,291 sites described by groundwater depth, distance to the free face, ground slope, and peak ground acceleration.

**Materials**
- Slides: [Introduction and exploratory analysis](01-dtree/01-intro-eda-slides.pdf), [Exploratory data analysis](01-dtree/01-eda-slides.pdf)
- Notebook: [Exploratory data analysis](01-dtree/01a-eda-liquefaction.ipynb)

### Module 2: Tree-based Supervised Classification Methods

**Theme:** Applying fundamental supervised learning algorithms for prediction tasks.

**Presentations**
- Decision Trees (DT)
- Random Forests (RF)
- XGBoost
- Evaluation metrics

**Hands-On:** Build decision tree, random forest, and XGBoost classifiers for earthquake-induced lateral spreading.

**Materials**
- Slides: [Handout: limitations of ML in geotechnics](01-dtree/01-ml-limitations-handout.pdf)
- Notebook: [Decision tree, random forest, XGBoost](01-dtree/01b-classification.ipynb)

### Module 3: Explainable AI (XAI) and Glass-Box Models

**Theme:** Understanding and interpreting complex AI models.

**Presentations**
- The Importance of Explainability in Geotechnical AI
- SHAP (SHapley Additive exPlanations)
- Explainable Boosting Machines (EBM)

**Hands-On:** Interpret the lateral spreading random forest with SHAP values and feature importance, then train an Explainable Boosting Machine on the same data.

**Materials**
- Notebook: [SHAP section of the classification notebook](01-dtree/01b-classification.ipynb)
- Notebook: [Explainable Boosting Machine](02-xai/02a-ebm.ipynb)

## Day 2:

### Module 4: Neural Networks - Multi-Layer Perceptron (Theory)

**Theme:** Understanding the fundamental building blocks of deep learning models.

**Presentations**
- The Neuron and Network Architecture (Layers, Weights, Biases)
- Common Activation Functions (Sigmoid, ReLU, Tanh etc.)
- Loss Functions and Introduction to Training (Gradient Descent, Backpropagation overview)

**Hands-On:** Build the architecture of a PyTorch Deep Neural Network (DNN).

**Materials**
- Slides: [Multi-layer perceptron](03-mlp/03-mlp-slides.pdf)
- Notebook: [MLP classification](03-mlp/03a-mlp-classification.ipynb)
- Theory: [Universal approximation theorem](03-mlp/uat.md), [Activation function ReLU](03-mlp/relu.md), [Binary cross entropy](03-mlp/bce.md), [Automatic differentiation](03-mlp/ad.md), [Gradient descent](03-mlp/sgd.md)

## Day 3:

### Module 5: Neural Networks - Multi-Layer Perceptron (Applications)

**Theme:** Applying Deep Neural Networks (DNNs) to solve specific geotechnical engineering problems.

**Presentations**
- Optimizers (SGD, Adam) and Training Dynamics
- Case Study: DNNs for TBM (Tunnel Boring Machine) Performance
- Hyperparameter Tuning, Regularization, and Other Geotechnical Applications.
- Train a DNN to predict TBM data using synthetic geology data, focusing on the training process and hyperparameter tuning.

**Materials**
- Notebook: [MLP pile capacity](03-mlp/03b-mlp-pile-capacity.ipynb)
- Notebook: [MLP function approximation](03-mlp/03c-mlp-function-approximation.ipynb)
- Notebook: [MLP extrapolation](03-mlp/03d-mlp-extrapolation.ipynb)
- Data: [shield_tunneling_risk_dataset.csv](03-mlp/tbm/shield_tunneling_risk_dataset.csv), [tunnel_risk_dataset.csv](03-mlp/tbm/tunnel_risk_dataset.csv), [TBM-Supplementary material.xlsx](03-mlp/tbm/TBM-Supplementary%20material.xlsx)

### Module 6: Convolutional Neural Networks and Recurrent Neural Networks

**Theme:** Understanding and applying CNNs for image and spatial data in geotechnics.

**Presentations**
- CNN Architecture: Convolutional Layers, Pooling Layers
- Applications: Image-based soil/rock classification, analysis of geophysical data.
- Transfer Learning with CNNs.

**Hands-On:** Train a PyTorch CNN to invert seismic waveforms (simplified example) or for rock fracture detection from provided images

**Materials**
- Slides: [Convolutional neural networks](04-cnn/04-cnn-slides.pdf)
- Notebook: [Soil image classification](04-cnn/04a-cnn-soil-classification.ipynb)
- Notebook: [FWI velocity inversion](04-cnn/04b-cnn-fwi-velocity.ipynb)
- Slides: [Recurrent networks and LSTM](05-lstm/05-rnn-lstm-slides.pdf), [LSTM for liquefaction](05-lstm/05-lstm-liquefaction-slides.pdf)
- Notebook: [LSTM liquefaction](05-lstm/05a-lstm-liquefaction.ipynb)

### Module 7: Clustering
**Theme:** Using unsupervised learning for site profiling and layering.

**Presentations**
- Introduction to Unsupervised Learning and Clustering
- K-Means, DBSCAN
- PCA for Dimensionality Reduction and Visualization
- Spectral Clustering

**Hands-On:** Cluster soil layers from CPT/SPT data using SciKit-Learn and visualize the resulting 3D stratigraphy.

**Materials**
- Notebook: [Fetch CPT data from the DesignSafe API](06-clustering/06a-fetch-cpt-data-dapi.ipynb)
- Notebook: [Clustering analysis](06-clustering/06b-clustering-analysis.ipynb)

## Day 4:

### Module 8: Large Language Models (LLMs) in Geotechnics

**Theme:** Leveraging LLMs for knowledge management and text-based tasks.

**Presentations**
- Introduction to LLMs and Transformers
- Retrieval-Augmented Generation (RAG)
- Geotechnical Applications (report analysis, Q&A on codes).

**Hands-On:** Call a model from Python, build a retrieval-augmented generation pipeline over site investigation reports, and run a tool-using agent that reads a report and checks a bearing capacity.

**Materials**
- Slides: [Large language models](07-llm/07-llm-slides.pdf)
- Notebook: [One API call](07-llm/07a-llm-api-call.ipynb)
- Notebook: [RAG over geotechnical reports](07-llm/07b-llm-rag-geotechnical.ipynb)
- Notebook: [Report-reading agent](07-llm/07c-llm-report-agent.ipynb)

### Module 9: Physics Informed Neural Networks and Operator Learning

**Theme:** Exploring Graph Neural Networks, other advanced concepts, and the future of AI in Geotechnics.

**Presentations**
- Introduction to Graph Neural Networks (GNNs) - Concepts & Potential Applications.
- Other Emerging AI Methods (e.g., Physics-Informed Neural Networks - PINNs).
- Future Trends, Ethics, and Challenges in AI for Geotechnics.

**Materials**
- Slides: [Physics-informed neural networks](08-pinn/08-pinn-slides.pdf)
- Notebook: [PINN oscillator](08-pinn/08a-pinn.ipynb)
- Notebook: [1D wave equation: PINN vs finite difference](08-pinn/08b-pinn-forward.ipynb)
- Notebook: [1D consolidation](08-pinn/08c-1d-consolidation-pinns.ipynb)
- Notebook: [1D consolidation with L-BFGS](08-pinn/08d-1d-consolidation-pinns-lbfgs.ipynb)