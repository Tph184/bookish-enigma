# Recursion in Problem Solving

Recursion solves problems by breaking them into smaller subproblems. A recursive function calls itself with modified parameters until reaching a base case.

## General Recursion Template
```python
def recursive_function(params):
    # Base case: simplest scenario with direct answer
    if base_case_condition(params):
        return base_case_value
    
    # Recursive case: reduce problem and call itself
    result = process(params)
    modified_params = reduce_problem(params)
    return combine(result, recursive_function(modified_params))
```

---

## Common Recursive Problems

### 1. Fibonacci Sequence
**Problem**: Compute the nth Fibonacci number (0, 1, 1, 2, 3, 5...).  
**Solution**:
```python
def fibonacci(n):
    if n <= 1:  # Base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Recursive case
```
**Time Complexity**: O(2<sup>n</sup>)  
**Optimization**: Use memoization for O(n) time.

---

### 2. Factorial
**Problem**: Compute factorial of `n` (n! = n × (n-1) × ... × 1).  
**Solution**:
```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n-1)  # Recursive case
```
**Time Complexity**: O(n)

---

### 3. Binary Tree Traversal (In-Order)
**Problem**: Visit all nodes of a binary tree in left-root-right order.  
**Solution**:
```python
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if not root:  # Base case
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)  # Recursive
```
**Time Complexity**: O(n)  
**Key**: Recursively process left, root, then right.

---

### 4. Tower of Hanoi
**Problem**: Move `n` disks from source to target using an auxiliary rod.  
**Solution**:
```python
def hanoi(n, source, target, auxiliary):
    if n == 1:  # Base case
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)  # Move n-1 disks to auxiliary
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)  # Move n-1 disks to target
```
**Time Complexity**: O(2<sup>n</sup>)  
**Steps**: For `n=3`, it takes 7 moves.

---

### 5. Merge Sort (Divide and Conquer)
**Problem**: Sort an array using recursion.  
**Solution**:
```python
def merge_sort(arr):
    if len(arr) <= 1:  # Base case
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursive split
    right = merge_sort(arr[mid:])
    return merge(left, right)  # Combine results

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
**Time Complexity**: O(n log n)

---

## When to Use Recursion?
- **Hierarchical structures**: Trees, graphs.  
- **Divide and conquer**: Merge sort, quick sort.  
- **Exhaustive search**: Permutations, subsets.  

## Key Principles
1. **Base case**: Always define a stopping condition.  
2. **Progress toward base case**: Parameters must evolve in each call.  
3. **Stack management**: Avoid stack overflow with tail recursion (Python doesn’t optimize this).  

---

## Pitfalls
- **Stack overflow**: Deep recursion crashes (use iteration for large `n`).  
- **Redundant computation**: Repeated work (e.g., Fibonacci without memoization).  
- **Complex debugging**: Hard to trace nested calls.  

---

## Conclusion
Recursion simplifies complex problems but requires careful design. For exponential-time problems (e.g., Fibonacci), prefer memoization or iteration. For tree/graph traversals, recursion is often the most intuitive approach.