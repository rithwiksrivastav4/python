# 🧮 NumPy Floor, Ceil, and Rint

## Problem Description
You are given a **1-D array** `A`.  
Your task is to print the **floor**, **ceil**, and **rint** of all the elements in `A`.

---

## 🔹 Definitions

- **Floor**:  
  The floor of `x` is the **largest integer ≤ x**.  
  Example: `floor(2.9) = 2`

- **Ceil**:  
  The ceil of `x` is the **smallest integer ≥ x**.  
  Example: `ceil(2.1) = 3`

- **Rint**:  
  Rounds `x` to the **nearest integer** (with halfway cases rounded to the nearest even integer).  
  Example: `rint(5.5) = 6`, `rint(2.5) = 2`

---

## 🔹 Code Template

```python
import numpy as np

# Ensures correct formatting of signs (important in HackerRank)
np.set_printoptions(sign=' ')  

# Read input as space-separated floats
A = np.array(list(map(float, input().split())))

# Apply operations
print(np.floor(A))   # Floor
print(np.ceil(A))    # Ceil
print(np.rint(A))    # Round
```

---

## 🔹 Input Format
A single line of space-separated floating-point numbers.

---

## 🔹 Output Format

1. First line → floor of `A`
2. Second line → ceil of `A`  
3. Third line → rint of `A`

---

## 🔹 Example

### Input

```
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
```

### Output

```
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[ 2.  3.  4.  5.  6.  7.  8.  9. 10.]
[ 1.  2.  3.  4.  6.  7.  8.  9. 10.]
```

---

## 🔹 Explanation

- **Floor:**  
  `1.1 → 1`, `2.2 → 2`, `9.9 → 9`

- **Ceil:**  
  `1.1 → 2`, `2.2 → 3`, `9.9 → 10`

- **Rint:**  
  `1.1 → 1`, `2.2 → 2`, `5.5 → 6`, `9.9 → 10`
