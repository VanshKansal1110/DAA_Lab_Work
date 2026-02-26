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
```The program recursively adds array elements by advancing the pointer and reducing the size of the array until the base condition is reached.```

Algorithm Used:
```Recursive array traversal```

Time Complexity:
```O(n)```

Space Complexity:
```O(n) (recursive call stack)```

-----------------------------------------------------------------------------------------

## 📄 File: 2_TowerOfHanoi.cpp

Problem Statement:
```Transfer n plates from the source stack to the destination stack using an auxiliary stack by following the rules of the Tower of Hanoi problem.```

Solution Overview:
```The solution uses recursion to move n-1 plates, transfer the largest plate, and then move the remaining plates, displaying each step clearly.```

Algorithm Used:
```Recursive Divide-and-Conquer```

Time Complexity:
```O(2ⁿ)```

Space Complexity:
```O(n)```

-----------------------------------------------------------------------------------------

## 📄 File: 3_LinearSearch.cpp

Problem Statement:
```Search for a target value in an array using the linear search technique.```

Solution Overview:
```The array is traversed sequentially until the target element is found or the array ends.```

Algorithm Used:
```Linear Search```

Time Complexity:
```Best Case: O(1)```
```Worst Case: O(n)```

Space Complexity:
```O(1)```

-----------------------------------------------------------------------------------------

## 📄 File: 4_TruthTable.cpp

Problem Statement:
```Generate a truth table for a given number of logical statements.```

Solution Overview:
```All possible combinations of truth values are generated using recursion by appending True and False until the required length is reached.```

Algorithm Used:
```Recursive backtracking```

Time Complexity:
```O(2ⁿ)```

Space Complexity:
```O(n)```

-----------------------------------------------------------------------------------------

## 📄 File: 5_HornerRule.cpp

Problem Statement:
```Evaluate a polynomial expression for a given value using Horner’s Rule.```

Solution Overview:
```The polynomial is evaluated in nested form using recursion to reduce the number of multiplications.```

Algorithm Used:
```Horner’s Method```

Time Complexity:
```O(n)```

Space Complexity:
```O(n)```

-----------------------------------------------------------------------------------------

## 📄 File: 6_SelectionSort.cpp

Problem Statement:
```Sort an array using the Selection Sort algorithm implemented recursively.```

Solution Overview:
```The smallest element is selected and placed at the beginning in each recursive step.```

Algorithm Used:
```Selection Sort (Recursive)```

Time Complexity:
```O(n²)```

Space Complexity:
```O(n)```

-----------------------------------------------------------------------------------------
## 📄 File: 7_PermutationFinder.cpp

**Problem Statement:**
```Generate all permutations of a given string.```

Solution Overview:
```Characters are swapped recursively to generate all possible permutations of the string.```

Algorithm Used:
```Recursive permutation generation```

Time Complexity:
```O(n!)```

Space Complexity:
```O(n)```

-----------------------------------------------------------------------------------------

## 📄 File: 8_MissingNumber.cpp

Problem Statement:
```Find the missing number in an array containing values from 0 to n.```

Solution Overview:
```Elements are placed at their correct indices, and the mismatch index indicates the missing value.```

Algorithm Used:
```Index mapping (in-place)```

Time Complexity:
```O(n)```

Space Complexity:
```O(1)```

-----------------------------------------------------------------------------------------

## 📄 File: 9_PowerCalculator.cpp

Problem Statement:
```Compute the power of a number using recursion, including negative powers.```

Solution Overview:
```Fast exponentiation is used to reduce computation by dividing the power into halves.```

Algorithm Used:
```Recursive fast exponentiation```

Time Complexity:
```O(log n)```

Space Complexity:
```O(log n)```

-----------------------------------------------------------------------------------------

## 📄 File: 10_NumOfBounces.cpp

Problem Statement:
```Calculate the number of bounces a ball makes until its velocity falls below a threshold.```

Solution Overview:
````Velocity is reduced recursively after each bounce until the stopping condition is met.```

Algorithm Used:
```Recursive simulation```

Time Complexity:
```O(k)```

Space Complexity:
```O(k)```

-----------------------------------------------------------------------------------------

## 📄 File: 11_FirstDuplicateNumber.cpp

Problem Statement:
```Find the index of the first duplicate element in an array.```

Solution Overview:
```Each element is compared with previously encountered values to detect the earliest duplicate.```

Algorithm Used:
```Nested loop comparison```

Time Complexity:
```O(n²)```

Space Complexity:
```O(1)```

-----------------------------------------------------------------------------------------

