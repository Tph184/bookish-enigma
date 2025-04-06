# Backtracking Algorithms

Backtracking is a systematic way to explore all possible solutions to a problem by building candidates incrementally and abandoning ("backtracking") those that fail constraints.

## Key Concepts
- **Choices**: Options at each step.
- **Constraints**: Conditions to prune invalid paths.
- **Goal**: Complete solution meeting all constraints.

---

## General Backtracking Template
```python
def backtrack(path, state):
    if is_solution(path):
        result.append(path.copy())
        return
    for choice in choices:
        if is_valid(choice, state):
            apply_choice(choice, path, state)
            backtrack(path, state)
            undo_choice(choice, path, state)
```
## Common Backtracking Problems
	1. Permutation
	**Problem**: Generate all permutations of [1, 2, 3].
	**Solution**:
```python
def permute(nums):
	def backtrack(path):
		if len(path) == len(nums):
			res.append(path.copy())
			return
		for num in nums:
			if num not in path:
				path.append(num)
				backtrack(path)
				path.pop()
	res = []
	backtrack([])
	return res
```
## Conclusion
Backtracking is ideal for combinatorial problems (permutations, subsets) and constraint satisfaction (N-Queens). Always:

1. Define valid choices.

2. Prune invalid paths.

3. Clone states to avoid side effects.
