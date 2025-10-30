# AI in Geotechnical Engineering

**Dr. Krishna Kumar and Dr. Ellen Rathje, University of Texas at Austin**

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

## Day 1: October 30

### Module 1: Introduction, Data Processing, and Feature Engineering (10am-noon)

**Theme:** Laying the groundwork for AI in geotechnics, from understanding data to preparing it for modeling.

**Presentations**
- Introduction to AI/ML/DL in Geotechnical Engineering (30min)
- Data Processing and Exploration (EDA, missing data, normalization)
- Feature Engineering for Geotechnical Data

**Demo examples:** Perform Exploratory Data Analysis (EDA) on borehole data and preprocess (clean) landslide data for modeling.

### Module 2: Tree-based Supervised Classification Methods - Day 1 (1-3:30 pm)

**Theme:** Applying fundamental supervised learning algorithms for prediction tasks.

**Presentations**
- Decision Trees (DT)
- Random Forests (RF)
- XGBoost
- Evaluation metrics

**Hands-On:** Build a decision tree classifier for landslide susceptibility mapping and train a logistic regression model for soil type prediction.

### Module 3: Explainable AI (XAI) and Glass-Box Models - Day 1 (4-5 pm)

**Theme:** Understanding and interpreting complex AI models.

**Presentations**
- The Importance of Explainability in Geotechnical AI
- SHAP (SHapley Additive exPlanations)
- Explainable Boosting Machines (EBM)

**Hands-On:** Train a Random Forest model to predict landslides and interpret the results using SHAP values and feature importance.

## Day 2: October 31

### Module 4: Neural Networks - Introduction - Day 2 (8-9:30 am, 10-noon)

**Theme:** Understanding the fundamental building blocks of deep learning models.

**Presentations**
- The Neuron and Network Architecture (Layers, Weights, Biases)
- Common Activation Functions (Sigmoid, ReLU, Tanh etc.)
- Loss Functions and Introduction to Training (Gradient Descent, Backpropagation overview)

**Hands-On:** Build the architecture of a PyTorch Deep Neural Network (DNN).

## Day 3: November 7

### Module 5: Neural Networks - Applications - Day 3 (10-noon)

**Theme:** Applying Deep Neural Networks (DNNs) to solve specific geotechnical engineering problems.

**Presentations**
- Optimizers (SGD, Adam) and Training Dynamics
- Case Study: DNNs for TBM (Tunnel Boring Machine) Performance
- Hyperparameter Tuning, Regularization, and Other Geotechnical Applications.
- Train a DNN to predict TBM data using synthetic geology data, focusing on the training process and hyperparameter tuning.

### Module 6: Convolutional Neural Networks - Day 3 (1-3 pm)

**Theme:** Understanding and applying CNNs for image and spatial data in geotechnics.

**Presentations**
- CNN Architecture: Convolutional Layers, Pooling Layers
- Applications: Image-based soil/rock classification, analysis of geophysical data.
- Transfer Learning with CNNs.

**Hands-On:** Train a PyTorch CNN to invert seismic waveforms (simplified example) or for rock fracture detection from provided images

### Module 7: Clustering - Day 3 (3:30-5 pm)

**Theme:** Using unsupervised learning for site profiling and layering.

**Presentations**
- Introduction to Unsupervised Learning and Clustering
- K-Means, DBSCAN
- PCA for Dimensionality Reduction and Visualization
- Spectral Clustering

**Hands-On:** Cluster soil layers from CPT/SPT data using SciKit-Learn and visualize the resulting 3D stratigraphy.

## Day 4: November 8

### Module 8: Large Language Models (LLMs) in Geotechnics - Day 4 (8-10 am)

**Theme:** Leveraging LLMs for knowledge management and text-based tasks.

**Presentations**
- Introduction to LLMs and Transformers
- Retrieval-Augmented Generation (RAG)
- Geotechnical Applications (report analysis, Q&A on codes).

**Hands-On:** Create a Q&A chatbot for geotechnical codes using HuggingFace Transformers and RAG principles.

### Module 9: Advanced Topics & Future Outlook - Day 4 (10:30-noon)

**Theme:** Exploring Graph Neural Networks, other advanced concepts, and the future of AI in Geotechnics.

**Presentations**
- Introduction to Graph Neural Networks (GNNs) - Concepts & Potential Applications.
- Other Emerging AI Methods (e.g., Physics-Informed Neural Networks - PINNs).
- Future Trends, Ethics, and Challenges in AI for Geotechnics.