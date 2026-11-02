<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Fibonacci Number

**Difficulty:** `Easy`

## Problem

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is:

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n). The first terms of the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 and so on. Note that the sequence is 0 indexed, so F(0) is the first term and F(1) is the second.

A direct recursive solution recomputes the same values many times; building the sequence from the bottom up, or keeping only the last two values, computes F(n) in O(n) time.

Input format: a single line with the integer n.

Output format: print a single integer, F(n).

## Examples

### Example 1

**Input**
```
n = 2
```
**Output**
```
1
```

**Explanation:** F(2) = F(1) + F(0) = 1 + 0 = 1.

### Example 2

**Input**
```
n = 3
```
**Output**
```
2
```

**Explanation:** F(3) = F(2) + F(1) = 1 + 1 = 2.

### Example 3

**Input**
```
n = 10
```
**Output**
```
55
```

**Explanation:** The sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, so F(10) = 55.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/fibonacci-number).