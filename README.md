# Symbolic Regression with Genetic Programming

### Computational Intelligence Project 2024/2025  
### Lorenzo Formentin


## Overview

This repository is the project work for a symbolic regression system implemented using Genetic Programming (GP). The aim is to automatically evolve mathematical expressions that best model a given dataset. Candidate expressions are represented as trees, where each node corresponds to either an operator, constant, or variable. The project includes several techniques to ensure robustness and efficiency, such as protected operators to avoid numerical issues, a custom node-based tree representation, and evolutionary operators (crossover, mutation, and selection) with depth control.

---

## Project Structure

- **`gp_node.py`**  
  Contains the `Node` class that represents the building block for the expression trees. Key features include:
  - **Evaluation:** Each node can evaluate its corresponding mathematical expression on NumPy array inputs.
  - **String Representation:** The `concat_name` property provides a human-readable version of the evolved expression.
  - **Tree Depth:** A property that computes the depth of the tree for complexity control.

- **Jupyter Notebook / Main Script**  
  The notebook (or script) contains the complete implementation of the Genetic Programming algorithm:
  - **Protected Operators:** Functions such as `p_log`, `p_sqrt`, and `p_power` are defined to safely evaluate mathematical operations without altering input values.
  - **GP Class:** Implements the entire GP algorithm:
    - **Population Initialization:** Random expression trees are generated with a mechanism to ensure a mix of constants and variables.
    - **Fitness Evaluation:** The fitness of each tree is measured by the Mean Squared Error (MSE) between the predicted output and target values.
    - **Evolution Operators:** Methods for cloning, crossover (subtree swapping), and mutation (with constant fine-tuning) are provided.
    - **Evolution Loop:** Over multiple generations, the population is evolved using tournament selection, elitism, and recombination.

- **`data/`**  
  Contains dataset files (in `.npz` format) used to evaluate the evolved symbolic expressions.

---

## Technique and Methodology

### Symbolic Regression and Genetic Programming

In this project, Genetic Programming (GP) is employed to evolve these expressions over successive generations.

### Tree Representation

- **Node Structure:**  
  Each candidate expression is represented as a tree, where:
  - **Leaf Nodes** represent constants or variables (e.g., `3.14`, `x[0]`).
  - **Internal Nodes** represent functions or operators (e.g., `np.add`, `np.sin`).
- **Evaluation:**  
  The `Node` class allows the tree to be evaluated on a given NumPy array `X`, returning a computed output that is compared to the target values.
- **String Representation:**  
  The `concat_name` property recursively builds a human-readable string of the expression, which aids in understanding and debugging the evolved formulas.
- **Depth Control:**  
  The property `tree_depth` is used to compute the depth of the tree, ensuring that the expressions do not become overly complex.

### Protected Operators

Numerical issues (such as division by zero or taking the logarithm of zero) can lead to errors or non-numeric outputs. To mitigate this, several protected operator functions are implemented:

- **`p_log(x)`:**  
  Computes `log(|x|)` elementwise. If `x` is zero, the result is `-inf`. No input substitution is performed; problematic values are simply passed as-is and later penalized via fitness evaluation.
- **`p_sqrt(x)`:**  
  Returns the square root of `|x|` to avoid complex numbers.
- **`p_power(x, y)`:**  
  Computes `|x|` raised to the power `y` elementwise. Negative bases are made positive using the absolute value to ensure real results.

These functions are used in place of the standard NumPy functions within the expression trees to ensure robustness during evolution.

### Evolutionary Process

The GP algorithm proceeds as follows:

1. **Initialization:**  
   A random population of expression trees is generated using a recursive method that balances the probability of selecting a constant versus a variable at the leaves, while ensuring the presence of at least one variable.

2. **Fitness Evaluation:**  
   The fitness of each tree is computed as the Mean Squared Error (MSE) between the predicted outputs (obtained by evaluating the tree on input data `X`) and the target values `Y`. Trees that result in non-numeric values (e.g., NaN or infinity) are penalized by assigning an infinite fitness.

3. **Selection:**  
   A tournament selection strategy is used to choose individuals for reproduction. The top 30-40% of the population (by fitness) is selected as parents.

4. **Crossover:**  
   Subtree swapping is performed between pairs of selected parent trees. The crossover operator ensures that the resulting offspring do not exceed the maximum allowed tree depth by retrying the swap up to 10 times if necessary.

5. **Mutation:**  
   With a set mutation probability, parts of the tree (either constant leaves or subtrees) are altered. Constant leaves are fine-tuned by adding a small Gaussian perturbation, while other subtrees may be replaced entirely with newly generated subtrees.

6. **Elitism:**  
   A fraction (10%) of the best individuals is carried over unchanged to the next generation to preserve high-quality solutions.

7. **Evolution Loop:**  
   The population evolves over a specified number of generations, with the best expression tracked throughout the process.

---

### Conclusion
Each expression is represented as tree structures using a custom Node class that enables flexible composition of operators, constants, and variables while providing intuitive evaluation and a human-readable string representation of the resulting expressions. The evolutionary process is guided by tournament selection, subtree crossover with depth control, and mutation strategies that fine-tune constant values. Through careful tuning of parameters like population size, number of generations, mutation and crossover rates, and maximum tree depth, a balance between exploration and exploitation is achieved, enabling the evolution of mathematical expressions that are both accurate in approximating the target data and interpretable in structure.
