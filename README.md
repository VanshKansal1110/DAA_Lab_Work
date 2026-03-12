# Algorithms Repository

## Introduction

I’m **Vansh Kansal, UE243120**. This repository is a collection of classical algorithms implemented as part of my academic coursework. The primary goal of this project is **learning, clarity, and correctness**—each algorithm is written in a clean and understandable manner so that anyone with basic programming knowledge can follow along.

---

## 📘 Repository Overview

This repository contains **multiple standalone programs**, each solving a well-known algorithmic problem. Every file focuses on **one algorithm only**, keeping implementations modular and easy to navigate.

Each program includes:

* A clear problem statement
* A structured solution approach
* Well-commented code (where applicable)
* Time and space complexity analysis

> **Language Used:**    C++,     Python

The repository is organized into:

- **Programs/** → Core algorithm implementations  
- **Graphs/** → Python-based visualizations illustrating algorithm behavior and performance  

This makes the repository suitable for:

- Academic evaluation  
- Technical interviews  
- Concept revision  
- Algorithm visualization and experimentation  

---

## 📂 File Structure

```
Algorithms-Repository/
│
├───Programs/
│├── 1_Sum_Of_N_Numbers.cpp
│├── 2_TowerOfHanoi.cpp
│├── 3_LinearSearch.cpp
│├── 4_TruthTable.cpp
│├── 5_HornerRule.cpp
│├── 6_SelectionSort.cpp
│├── 7_PermutationGenerator.cpp
│├── 8_MissingNumber.cpp
│├── 9_PowerCalculator.cpp
│├── 10_NumOfBounces.cpp
│├── 11_FirstDuplicateNumber.cpp
│├── 12_BinarySearch.cpp
│├── 13_InsertionSort.cpp
│├── 14_MergeSort.py
│├── 15_QuickSort.py
│├── 16_Min_Max_By_D&C.py
│├── 17_Knapsack.py
│├── 18_ConvexHull.py
│├── 19_MatrixMultiplication.py
│
├───Graphs/
│├── 1_Sum_Of_N_Numbers.cpp
│├── 2_TowerOfHanoi.cpp
│├── 3_LinearSearch.cpp
│├── 4_TruthTable.cpp
│├── 5_HornerRule.cpp
│├── 6_SelectionSort.cpp
│├── 7_PermutationGenerator.cpp
│├── 8_MissingNumber.cpp
│├── 9_PowerCalculator.cpp
│├── 10_NumOfBounces.cpp
│├── 11_FirstDuplicateNumber.cpp
│├── 12_BinarySearch.cpp
│├── 13_InsertionSort.cpp
│├── 14_MergeSort.py
│├── 15_QuickSort.py
│├── 16_Min_Max_By_D&C.py
│├── 17_Knapsack.py
│├── 18_ConvexHull.py
│├── 19_MatrixMultiplication.py
└── README.md

```

---

## 🧠 Algorithms Included

Below is a detailed explanation of each file present in the repository.

----------------------------------------------------------------------------------------

## 📄 File: 1_Sum_Of_N_Numbers.cpp

Problem Statement:
```Find the sum of all elements in a given array using recursion.```

Solution Overview:
```The program recursively traverses the array and adds each element to the total sum until the base condition is reached when the index equals the array length.```

Algorithm Used:
```Recursive Array Traversal```

Time Complexity:
```O(n)```

Space Complexity:
```O(n) (recursive call stack)```

Visualization Script:
```Graphs/1_SumOfNNumbers.py```

Graph Screenshot:
```Graphs/Screenshots/1_SumOfNNumbers.png```

Graph Analysis:
```The plotted graph shows a linear relationship between the input size and the execution time. The actual execution time curve closely follows the expected O(n) theoretical curve, confirming the linear time complexity of the algorithm.```

----------------------------------------------------------------------------------------

## 📄 File: 2_TowerOfHanoi.cpp

Problem Statement:
```Transfer n disks from the source rod to the destination rod using an auxiliary rod while following the rules of the Tower of Hanoi problem.```

Solution Overview:
```The recursive solution divides the problem into smaller subproblems. First n−1 disks are moved to the auxiliary rod, then the largest disk is transferred to the destination rod, and finally the remaining disks are moved from the auxiliary rod to the destination rod.```

Algorithm Used:
```Recursive Divide-and-Conquer```

Time Complexity:
```O(2ⁿ)```

Space Complexity:
```O(n)```

Visualization Script:
```Graphs/2_TowerOfHanoi.py```

Graph Screenshot:
```Graphs/Screenshots/2_TowerOfHanoi.png```

Graph Analysis:
```The graph demonstrates exponential growth in the number of operations as the number of disks increases. This behavior aligns with the theoretical time complexity O(2ⁿ).```

----------------------------------------------------------------------------------------

## 📄 File: 3_LinearSearch.cpp

Problem Statement:
```Search for a target value in an array using the linear search technique.```

Solution Overview:
```The algorithm sequentially traverses the array and compares each element with the target value until a match is found or the array ends.```

Algorithm Used:
```Linear Search```

Time Complexity:
```Best Case: O(1)```
```Average Case: O(n)```
```Worst Case: O(n)```

Space Complexity:
```O(1)```

Visualization Script:
```Graphs/3_LinearSearch.py```

Graph Screenshot:
```Graphs/Screenshots/3_LinearSearch.png```

Graph Analysis:
```The graph shows a linear increase in execution time as the array size increases. The measured execution time closely follows the theoretical O(n) curve.```

----------------------------------------------------------------------------------------

## 📄 File: 4_TruthTable.cpp

Problem Statement:
```Generate a truth table for a given number of logical statements.```

Solution Overview:
```The program recursively generates all possible combinations of truth values for the given number of logical variables. Each recursive step appends either True or False until the required length is reached.```

Algorithm Used:
```Recursive Backtracking```

Time Complexity:
```O(2ⁿ)```

Space Complexity:
```O(n)```

Visualization Script:
```Graphs/4_TruthTable.py```

Graph Screenshot:
```Graphs/Screenshots/4_TruthTable.png```

Graph Analysis:
```The graph shows exponential growth in the number of generated combinations as the number of logical variables increases, matching the theoretical complexity O(2ⁿ).```

----------------------------------------------------------------------------------------

## 📄 File: 5_HornerRule.cpp

Problem Statement:
```Evaluate a polynomial expression for a given value using Horner’s Rule.```

Solution Overview:
```Horner’s Rule evaluates the polynomial in nested form, reducing the number of multiplication operations required for polynomial evaluation.```

Algorithm Used:
```Horner’s Method```

Time Complexity:
```O(n)```

Space Complexity:
```O(1)```

Visualization Script:
```Graphs/5_HornerRule.py```

Graph Screenshot:
```Graphs/Screenshots/5_HornerRule.png```

Graph Analysis:
```The graph illustrates linear time behavior as the polynomial degree increases. The measured execution times align closely with the theoretical O(n) complexity curve.```

----------------------------------------------------------------------------------------

## 📄 File: 6_SelectionSort.cpp

Problem Statement:
```Sort an array using the Selection Sort algorithm implemented recursively.```

Solution Overview:
```The algorithm repeatedly selects the smallest element from the unsorted portion of the array and swaps it with the first element. The remaining array is then sorted recursively.```

Algorithm Used:
```Recursive Selection Sort```

Time Complexity:
```Best Case: O(n²)```
```Average Case: O(n²)```
```Worst Case: O(n²)```

Space Complexity:
```O(n) (recursive call stack)```

Visualization Script:
```Graphs/6_SelectionSort.py```

Graph Screenshot:
```Graphs/Screenshots/6_SelectionSort.png```

Graph Analysis:
```The graph demonstrates quadratic growth of execution time as the input size increases. The experimental results follow the expected O(n²) complexity curve.```

----------------------------------------------------------------------------------------
