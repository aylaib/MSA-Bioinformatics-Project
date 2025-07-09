# Multiple Sequence Alignment Algorithms Implementation and Comparison
This project, carried out as part of the Bio-Algorithmics module (Master 1 Bioinformatics, USTHB), explores the implementation and performance analysis of different methods for multiple sequence alignment (MSA).
The main objective is to compare two fundamental approaches: the **progressive approach** (heuristic) and the **iterative approach** based on a genetic algorithm (SAGA).
## 📊 Comparative Performance Analysis
The `Comp.py` script analyzes the execution time data of the two main methods and generates the following comparative graph, demonstrating the performance difference in terms of speed between the progressive approach and SAGA.
## 🤖 Implemented Algorithms
This repository contains a collection of Python scripts, each demonstrating a key algorithm or concept:
1.  **`Needelman.py` : Pairwise Alignment (Needleman-Wunsch)**
    - Implements the classic dynamic programming algorithm for global alignment of two sequences.
    - Uses the **BLOSUM62** similarity matrix and a linear gap penalty.
    - Generates random protein sequences for testing.
2.  **`ProgressiveMultiple.py` : Progressive Multiple Alignment**
    - An implementation of a fast heuristic method for multiple alignment.
    - Progressively aligns sequences based on a profile that is updated at each step.
    - Very efficient in computational time, this is an approach similar to that used by tools like ClustalW.
3.  **`SAGA.py` : Genetic Algorithm Alignment (SAGA)**
    - Implements an iterative method that uses evolutionary principles (selection, crossover, mutation) to find a high-quality alignment.
    - Aims to optimize an alignment score over multiple generations.
    - Although slower, this algorithm can potentially find better alignments for complex cases.
4.  **`Comp.py` : Analysis and Visualization Script**
    - Does not perform alignment.
    - Takes performance data (execution time) as input and uses `matplotlib` to visualize the comparison between methods.
## 🚀 How to Run
Each script is standalone and can be executed individually.
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/MSA-Bioinformatics-Project.git
    cd MSA-Bioinformatics-Project
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the script of your choice:**
    - For pairwise alignment:
      ```bash
      python Needelman.py
      ```
    - For progressive alignment:
      ```bash
      python ProgressiveMultiple.py
      ```
    - For alignment with SAGA:
      ```bash
      python SAGA.py
      ```
    - To generate the comparison graph:
      ```bash
      python Comp.py
      ```
Each script will guide you by asking for the necessary parameters (sequence size, number of sequences, etc.).
## 📚 Reference Documents
- **[Complete Project Report](./rapport_alignement_multiple.pdf)** : This document contains the detailed theoretical analysis, methodology, test results and project conclusion.
- **[Project Statement](./enonce_projet.pdf)** : The original specifications of the mini-project.
