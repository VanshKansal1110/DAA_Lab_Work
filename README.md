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

## 📄 File: 7_PermutationGenerator.cpp

Problem Statement:
```Generate all possible permutations of a given string.```

Solution Overview:
```The algorithm recursively swaps characters in the string and explores all possible arrangements. After fixing one character at a position, it recursively generates permutations for the remaining substring.```

Algorithm Used:
```Recursive Permutation Generation (Backtracking)```

Time Complexity:
```O(n!)```

Space Complexity:
```O(n) (recursion stack)```

Visualization Script:
```Graphs/7_PermutationGenerator.py```

Graph Screenshot:
```Graphs/Screenshots/7_PermutationGenerator.png```

Graph Analysis:
```The graph shows factorial growth as the input size increases. The number of permutations generated grows extremely fast, confirming the theoretical complexity of O(n!).```

----------------------------------------------------------------------------------------

## 📄 File: 8_MissingNumber.cpp

Problem Statement:
```Find the missing number from an array containing values from 0 to n.```

Solution Overview:
```The algorithm rearranges elements so that each value is placed at its corresponding index. When an element is not at its correct position, it swaps with the value at its target index. The index where mismatch occurs represents the missing number.```

Algorithm Used:
```Index Mapping (Cyclic Placement Technique)```

Time Complexity:
```O(n)```

Space Complexity:
```O(1)```

Visualization Script:
```Graphs/8_MissingNumber.py```

Graph Screenshot:
```Graphs/Screenshots/8_MissingNumber.png```

Graph Analysis:
```The graph demonstrates a linear increase in operations relative to input size. The experimental data aligns closely with the theoretical O(n) time complexity.```

----------------------------------------------------------------------------------------

## 📄 File: 9_PowerCalculator.cpp

Problem Statement:
```Compute the power of a number using an efficient recursive algorithm.```

Solution Overview:
```The algorithm uses fast exponentiation. Instead of multiplying the base repeatedly, it squares the base and halves the exponent, significantly reducing the number of recursive calls.```

Algorithm Used:
```Fast Exponentiation (Exponentiation by Squaring)```

Time Complexity:
```O(log n)```

Space Complexity:
```O(log n)```

Visualization Script:
```Graphs/9_PowerCalculator.py```

Graph Screenshot:
```Graphs/Screenshots/9_PowerCalculator.png```

Graph Analysis:
```The graph confirms logarithmic growth in the number of recursive calls as the exponent increases, validating the O(log n) complexity.```

----------------------------------------------------------------------------------------

## 📄 File: 10_NumOfBounces.cpp

Problem Statement:
```Determine how many times a ball will bounce before its velocity falls below a given threshold.```

Solution Overview:
```The algorithm recursively reduces the velocity after each bounce using a fixed decay factor until the velocity becomes less than or equal to the stopping threshold.```

Algorithm Used:
```Recursive Simulation```

Time Complexity:
```O(log v)```

Space Complexity:
```O(log v)```

Visualization Script:
```Graphs/10_NumOfBounces.py```

Graph Screenshot:
```Graphs/Screenshots/10_NumOfBounces.png```

Graph Analysis:
```The graph illustrates logarithmic behavior since the velocity decreases exponentially after each bounce. The number of recursive calls grows slowly relative to the initial velocity.```

----------------------------------------------------------------------------------------

## 📄 File: 11_FirstDuplicateNumber.cpp

Problem Statement:
```Find the index of the first duplicate element in an array.```

Solution Overview:
```The algorithm compares each element with all previously visited elements to detect the earliest duplicate occurrence.```

Algorithm Used:
```Nested Loop Comparison```

Time Complexity:
```O(n²)```

Space Complexity:
```O(1)```

Visualization Script:
```Graphs/11_FirstDuplicateNumber.py```

Graph Screenshot:
```Graphs/Screenshots/11_FirstDuplicateNumber.png```

Graph Analysis:
```The graph displays quadratic growth in comparisons as the array size increases, confirming the theoretical O(n²) time complexity.```

----------------------------------------------------------------------------------------

## 📄 File: 12_BinarySearch.cpp

Problem Statement:
```Search for a target value in a sorted array using the binary search technique.```

Solution Overview:
```Binary search repeatedly divides the search interval in half. If the target value is smaller than the middle element, the search continues in the left half; otherwise, it continues in the right half.```

Algorithm Used:
```Recursive Binary Search```

Time Complexity:
```O(log n)```

Space Complexity:
```O(log n)```

Visualization Script:
```Graphs/12_BinarySearch.py```

Graph Screenshot:
```Graphs/Screenshots/12_BinarySearch.png```

Graph Analysis:
```The graph demonstrates logarithmic growth in recursive calls, confirming the expected O(log n) performance.```

----------------------------------------------------------------------------------------

## 📄 File: 13_InsertionSort.cpp

Problem Statement:
```Sort an array using the Insertion Sort algorithm.```

Solution Overview:
```The algorithm builds the sorted array one element at a time by inserting each element into its correct position in the already sorted portion of the array.```

Algorithm Used:
```Insertion Sort```

Time Complexity:
```Best Case: O(n)```
```Average Case: O(n²)```
```Worst Case: O(n²)```

Space Complexity:
```O(1)```

Visualization Script:
```Graphs/13_InsertionSort.py```

Graph Screenshot:
```Graphs/Screenshots/13_InsertionSort.png```

Graph Analysis:
```The graph shows linear behavior in the best case and quadratic behavior in the worst case, matching the theoretical complexity of insertion sort.```

----------------------------------------------------------------------------------------

## 📄 File: 14_MergeSort.py

Problem Statement:
```Sort a list of numbers using the Merge Sort algorithm.```

Solution Overview:
```Merge sort divides the array into two halves recursively, sorts each half, and then merges the sorted halves to produce the final sorted array.```

Algorithm Used:
```Divide and Conquer (Merge Sort)```

Time Complexity:
```Best Case: O(n log n)```
```Worst Case: O(n log n)```

Space Complexity:
```O(n)```

Visualization Script:
```Graphs/14_MergeSort.py```

Graph Screenshot:
```Graphs/Screenshots/14_MergeSort.png```

Graph Analysis:
```The graph follows the expected O(n log n) growth pattern. Both best and worst cases show similar performance due to the consistent divide-and-conquer process.```

----------------------------------------------------------------------------------------

## 📄 File: 15_QuickSort.py

Problem Statement:
```Sort a list of numbers using the Quick Sort algorithm.```

Solution Overview:
```The algorithm selects a pivot element and partitions the array so that elements smaller than the pivot appear before it and larger elements appear after it. The process is recursively applied to subarrays.```

Algorithm Used:
```Divide and Conquer (Quick Sort)```

Time Complexity:
```Best Case: O(n log n)```
```Worst Case: O(n²)```

Space Complexity:
```O(log n)```

Visualization Script:
```Graphs/15_QuickSort.py```

Graph Screenshot:
```Graphs/Screenshots/15_QuickSort.png```

Graph Analysis:
```The graph illustrates efficient performance in average cases with O(n log n) complexity, while worst-case inputs demonstrate quadratic growth.```

----------------------------------------------------------------------------------------

## 📄 File: 16_Min_Max_By_D&C.py

Problem Statement:
```Find the minimum and maximum values in an array using a divide-and-conquer approach.```

Solution Overview:
```The algorithm splits the array into two halves recursively, finds the minimum and maximum in each half, and combines the results by comparing the two minimums and two maximums.```

Algorithm Used:
```Divide and Conquer```

Time Complexity:
```O(n)```

Space Complexity:
```O(log n)```

Visualization Script:
```Graphs/16_Min_Max_By_D&C.py```

Graph Screenshot:
```Graphs/Screenshots/16_Min_Max_By_D&C.png```

Graph Analysis:
```The graph confirms linear time complexity as the algorithm processes each element while minimizing the number of comparisons using divide-and-conquer.```

----------------------------------------------------------------------------------------

## 📄 File: 17_Knapsack.py

Problem Statement:
```Solve the Knapsack problem using different greedy strategies.```

Solution Overview:
```Three greedy strategies are implemented: sorting by profit-to-weight ratio, by weight, and by profit. The algorithm selects items greedily until the capacity constraint is reached.```

Algorithm Used:
```Greedy Algorithm```

Time Complexity:
```O(n log n)```

Space Complexity:
```O(n)```

Visualization Script:
```Graphs/17_Knapsack.py```

Graph Screenshot:
```Graphs/Screenshots/17_Knapsack.png```

Graph Analysis:
```The graph compares different greedy strategies and shows how sorting criteria affect the total profit achieved for varying knapsack capacities.```

----------------------------------------------------------------------------------------

## 📄 File: 18_ConvexHull.py

Problem Statement:
```Determine the convex hull of a set of points in a two-dimensional plane.```

Solution Overview:
```The algorithm uses the QuickHull method, which recursively finds the farthest point from a line segment and divides the remaining points into subsets to construct the convex hull.```

Algorithm Used:
```Divide and Conquer (QuickHull)```

Time Complexity:
```Average Case: O(n log n)```
```Worst Case: O(n²)```

Space Complexity:
```O(n)```

Visualization Script:
```Graphs/18_ConvexHull.py```

Graph Screenshot:
```Graphs/Screenshots/18_ConvexHull.png```

Graph Analysis:
```The graph demonstrates the algorithm’s typical n log n behavior in average cases, while certain point configurations may produce quadratic complexity.```

----------------------------------------------------------------------------------------

## 📄 File: 19_MatrixMultiplication.py

Problem Statement:
```Multiply two matrices using both Divide-and-Conquer and Strassen's algorithm.```

Solution Overview:
```Two matrix multiplication approaches are implemented. The first uses the classical divide-and-conquer method, while the second applies Strassen's algorithm to reduce the number of multiplications required.```

Algorithm Used:
```Divide and Conquer & Strassen's Matrix Multiplication```

Time Complexity:
```Divide and Conquer: O(n³)```
```Strassen's Algorithm: O(n^2.81)```

Space Complexity:
```O(n²)```

Visualization Script:
```Graphs/19_MatrixMultiplication.py```

Graph Screenshot:
```Graphs/Screenshots/19_MatrixMultiplication.png```

Graph Analysis:
```The graph compares the execution times of the divide-and-conquer approach and Strassen's algorithm. For larger matrix sizes, Strassen's method becomes more efficient due to reduced multiplication operations.```

----------------------------------------------------------------------------------------
