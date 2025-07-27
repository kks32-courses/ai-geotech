# AI in Geotechnical Engineering

> Krishna Kumar

A comprehensive course designed to introduce geotechnical engineers and scientists to the revolutionary field of Scientific Machine Learning (SciML). This course bridges traditional geotechnical engineering with cutting-edge AI techniques, focusing on solving real-world problems in soil mechanics, foundation engineering, and geotechnical modeling through Physics-Informed Neural Networks (PINNs) and advanced machine learning approaches.

The course emphasizes practical applications in geotechnical engineering, from soil classification and liquefaction prediction to solving complex consolidation problems and parameter identification. Participants will gain hands-on experience with industry-standard tools including Python, PyTorch, and modern scientific computing libraries.


**Slides:** [![View PDF](https://img.shields.io/badge/View-PDF-red?style=flat-square&logo=googledocs&logoColor=white)](https://github.com/kks32-courses/ai-geotech/raw/main/docs/2025-AI-Geotech.pdf)

## Course Structure

### Module 1: Foundations of Machine Learning in Geotechnical Engineering

**[00a-classification](docs/00a-classification/)** - Introduction to Classification Problems
- Traditional geotechnical classification using Decision Trees, Random Forest, and XGBoost
- Earthquake-induced liquefaction prediction with SHAP explainability
- Real-world geotechnical dataset analysis and feature importance

**[00b-mlp-classification](docs/00b-mlp-classification/)** 

- Multi-Layer Perceptrons for Geotechnical Applications
- From perceptrons to deep neural networks: theoretical foundations
- Universal Approximation Theorem and Sobolev spaces
- Activation functions, gradient descent, and automatic differentiation
- Advanced MLP implementation for liquefaction classification
- Comparison with traditional methods and feature importance analysis

### Module 2: Physics-Informed Neural Networks for Geotechnical Problems

**[01-pinn](docs/01-pinn/)** - Physics-Informed Neural Networks Introduction
- **1D Consolidation Problems**: Complete introduction using Terzaghi's consolidation equation
- Why standard neural networks fail for physics problems
- Universal Approximation Theorem extension to PDEs and Sobolev spaces
- Automatic differentiation for exact derivative computation
- Multi-component loss functions: data, physics, boundary conditions, and initial conditions
- Advanced training strategies (Adam + LBFGS optimization)
- Engineering validation against analytical solutions

### Course Objectives
Upon completion of this course, participants will be able to:

1. **Apply Machine Learning to Geotechnical Classification**: Implement and compare traditional ML methods (Decision Trees, Random Forest) with modern neural networks for geotechnical problems like liquefaction prediction.

2. **Master Neural Network Fundamentals**: Understand MLPs from theoretical foundations (Universal Approximation Theorem) to practical implementation, with focus on geotechnical applications.

3. **Solve PDEs with Physics-Informed Neural Networks**: Implement PINNs for fundamental geotechnical problems, starting with 1D consolidation and extending to complex boundary value problems.

4. **Understand Theoretical Foundations**: Grasp the mathematical principles behind SciML, including Sobolev spaces, automatic differentiation, and physics-informed training strategies.

5. **Compare Traditional vs AI Methods**: Critically evaluate when to use AI approaches versus traditional geotechnical methods, understanding advantages and limitations of each.

6. **Handle Real Geotechnical Data**: Work with sparse, noisy field measurements typical in geotechnical engineering and learn to extract meaningful insights.

### Target Audience
This course is specifically designed for:

- **Geotechnical Engineers**: Practicing professionals seeking to integrate AI/ML into foundation design, soil analysis, and geotechnical modeling workflows.

- **Geotechnical Researchers**: Academics and graduate students working on computational geomechanics, soil behavior modeling, and geotechnical data analysis.

- **Civil Engineering Professionals**: Engineers working in areas intersecting with geotechnical engineering (structural, environmental, earthquake engineering).

- **Engineering Consultants**: Technical professionals in geotechnical consulting firms looking to modernize analysis capabilities and improve prediction accuracy.

- **Data Scientists in Engineering**: ML practitioners interested in applying physics-informed approaches to engineering problems with solid theoretical foundations.

## Key Features

### **Geotechnical Engineering Focus**

- Real-world problems: liquefaction prediction, consolidation analysis, soil classification
- Industry-relevant datasets and case studies
- Connection to practical engineering applications and design decisions

### **Progressive Learning Approach**

- **Start Simple**: Traditional ML methods (Decision Trees, Random Forest)
- **Build Foundation**: Neural networks with theoretical rigor (Universal Approximation Theorem)
- **Advanced Applications**: Physics-Informed Neural Networks for PDEs

### **Strong Theoretical Foundation**

- Mathematical rigor with Sobolev spaces and functional analysis
- Clear derivations from first principles
- Understanding of when and why methods work

### **Hands-On Implementation**

- Complete Jupyter notebooks with detailed explanations
- PyTorch implementations optimized for geotechnical problems
- Automatic differentiation and modern optimization techniques

###  **Comprehensive Comparisons**

- Traditional methods vs neural networks
- Data-driven vs physics-informed approaches
- Performance analysis and engineering validation

## Prerequisites

### **Essential Background**

- **Geotechnical Engineering**: Soil mechanics, consolidation theory, foundation engineering basics
- **Mathematics**: Calculus (derivatives, integrals), linear algebra basics, differential equations
- **Programming**: Basic Python programming experience

### **Helpful but Not Required**
- Machine learning fundamentals
- PyTorch or TensorFlow experience
- Numerical methods background

## Learning Outcomes

After completing this course, participants will have:

### **Practical Skills**

- ✅ Implemented complete ML pipelines for geotechnical classification problems
- ✅ Built neural networks from scratch with theoretical understanding
- ✅ Solved PDEs using Physics-Informed Neural Networks
- ✅ Applied automatic differentiation to geotechnical problems

### **Theoretical Understanding**

- ✅ Universal Approximation Theorem and its extensions to PDEs
- ✅ Sobolev spaces and their role in scientific machine learning
- ✅ Physics-informed training strategies and loss function design
- ✅ When to use AI vs traditional methods in geotechnical engineering

### **Professional Capabilities**

- ✅ Evaluate and implement AI solutions for geotechnical problems
- ✅ Integrate sparse field measurements with physics-based models
- ✅ Communicate AI approach benefits and limitations to engineering teams
- ✅ Design custom neural network architectures for specific geotechnical applications

## Technical Requirements

- **Google Colab** (recommended) or local Python environment
- **Python 3.8+** with standard scientific computing libraries
- **PyTorch** for neural network implementation
- **Basic libraries**: NumPy, Matplotlib, Pandas, Scikit-learn

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kks32-courses/ai-geotech.git
   cd ai-geotech
   ```

2. **Start with Module 1**

   - Begin with `docs/00a-classification/` for traditional ML approaches
   - Progress to `docs/00b-mlp-classification/` for neural network foundations

3. **Advance to PINNs**

   - Work through `docs/01-pinn/1d-consolidation-pinns.ipynb` for physics-informed approaches

4. **Use Google Colab Links**

   - Each notebook includes direct Colab links for immediate execution
   - No local setup required - run everything in the cloud

---

> **Note**: This course focuses specifically on geotechnical applications of Scientific Machine Learning. For broader SciML topics, see the main [SciML course](https://chishiki-ai.org/sciml).