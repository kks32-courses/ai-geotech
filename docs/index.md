# Scientific Machine Learning (SciML)

Welcome to the Scientific Machine Learning course materials.

## Course Overview

This course covers the fundamentals of Scientific Machine Learning, combining traditional scientific computing with modern machine learning techniques.

## Topics Covered

### **Day 1: Foundations & Physics-Informed Methods (3 Hours)**

This day focuses on establishing the core concepts of SciML and introducing the first major technique, PINNs.

*   **Module 1: Foundations of SciML & Differentiable Programming (1.5 hours)**
    *   **Objective**: Establish the SciML landscape and understand Automatic Differentiation (AD) as the core engine for most SciML methods.
    *   **Topics**:
        *   What is Scientific Machine Learning (SciML)? Bridging ML and Scientific Computation.
        *   **Core Concept**: A deep dive into Automatic Differentiation (AD), comparing forward and reverse modes.
        *   **Differentiable Programming**: How to think about and build end-to-end differentiable pipelines.
        *   Introduction to the context of Ordinary and Partial Differential Equations (ODEs/PDEs).
    *   **Tools/Demo**: Introduction to `JAX` or `PyTorch Autograd` as the primary tools for AD.

*   **Module 2: Physics-Informed Neural Networks (PINNs) (1.5 hours)**
    *   **Objective**: Dive deep into using PINNs for solving forward and inverse problems involving differential equations.
    *   **Topics**:
        *   PINN Architecture: Combining data loss and physics loss.
        *   Solving Forward Problems: Using PINNs to find solutions to known PDEs (e.g., Burger's equation).
        *   Solving Inverse Problems: Using PINNs to discover unknown PDE parameters from data.
        *   The role and importance of colocation points.
    *   **Tools/Demo**: Live demo in Colab solving a forward PDE and a simple inverse problem with a PINN.

### **Day 2: Advanced Surrogate Modeling (3 Hours)**

This day builds on the foundations to cover more advanced and scalable surrogate modeling techniques like Operator Learning and GNNs.

*   **Module 3: Operator Learning (1.5 hours)**
    *   **Objective**: Understand methods for learning mappings between function spaces to accelerate solutions for entire families of PDEs.
    *   **Topics**:
        *   Motivation: The limitations of PINNs when PDE parameters or boundary conditions change frequently.
        *   The Operator Learning Paradigm: Learning function-to-function mappings.
        *   **DeepONet**: A deep dive into the architecture (Branch Net, Trunk Net) and its theoretical underpinnings.
        *   Data generation strategies for training operator networks.
    *   **Tools/Demo**: Live demo training a DeepONet and applying it to a parameterized PDE problem.

*   **Module 4: GNN Surrogates for Simulations (1.5 hours)**
    *   **Objective**: Learn to apply GNNs as powerful surrogates for physical systems represented by graphs or meshes.
    *   **Topics**:
        *   Introduction to Graph Neural Networks (GNNs).
        *   Representing physical systems as graphs (e.g., meshes, particle systems, multi-body physics).
        *   **GNNs as Surrogates**: Using GNNs to learn the dynamics of a system and accelerate simulations.
        *   Core Concepts: Message passing and graph convolution in the context of physics.
    *   **Tools/Demo**: Showcase a GNN surrogate applied to a simple physics simulation (e.g., fluid or particle dynamics).


## Instructor

**Krishna Kumar**  
Dr. Krishna Kumar is an Assistant Professor at the University of Texas at Austin. His research is
at the intersection of AI/ML, geotechnical engineering, and robotics. He directs a $7M
NSF-funded national ecosystem for AI integration in civil engineering and received an NSF
CAREER Award in 2024. His research involves developing differentiable simulations, graph
neural networks and numerical methods for understanding natural hazards. As an educator, he
received the Dean's Award for Outstanding Teaching at UT Austin and runs coding clubs at
Austin Public Libraries teaching AI/ML robotics to children ages 7-12.

## License

This work is licensed under the MIT License.