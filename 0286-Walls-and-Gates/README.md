# Islands and Treasure
 
## MEDIUM - GRAPHS

## Problem Description

You are given a `m × n` 2D grid initialized with these three possible values:

- `-1`: A water cell that cannot be traversed.
- `0`: A treasure chest.
- `INF`: A land cell that can be traversed. We use the integer `2^31 - 1 = 2147483647` to represent `INF`.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest, then the value should remain `INF`.

Assume the grid can only be traversed up, down, left, or right.

## Examples

### Example 1:

**Input:**

```python
[
  [2147483647, -1, 0, 2147483647],
  [2147483647, 2147483647, 2147483647, -1],
  [2147483647, -1, 2147483647, -1],
  [0, -1, 2147483647, 2147483647]
]
```

**Output:**

```python
[
  [3, -1, 0, 1],
  [2, 2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3, 4]
]
```

### Example 2:

**Input:**

```python
[
  [0, -1],
  [2147483647, 2147483647]
]
```

**Output:**

```python
[
  [0, -1],
  [1, 2]
]
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is one of `{-1, 0, 2147483647}`

## Notes

- The grid can only be traversed in four directions: up, down, left, or right.
- The problem ensures that there is always at least one treasure chest (0) in the grid.
- If a land cell cannot reach a treasure chest, it should remain as `INF`.

## Acceptance Rate

- Accepted: 4148
- Submitted: 11396
- Acceptance Rate: 36%
