class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or 
                matrix[r][c] <= prevVal):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
        
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r,c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())




### Intuition and Approach

# The problem is to find the longest increasing path in a matrix. Each cell in the matrix can move in four directions: up, down, left, and right. The path must strictly increase in value.

# This problem can be efficiently solved using Depth-First Search (DFS) with memoization to avoid redundant calculations. The idea is to use a DFS to explore all possible paths starting from each cell, while caching the results to avoid re-computation.

# ### Detailed Steps

# 1. **Initialization**:
#    - Determine the number of rows (`ROWS`) and columns (`COLS`) in the matrix.
#    - Initialize a dictionary (`dp`) to store the results of the DFS calls for each cell. The key is a tuple `(r, c)` representing a cell, and the value is the length of the longest increasing path starting from that cell.

# 2. **DFS Function**:
#    - The DFS function `dfs(r, c, prevVal)` explores the matrix starting from cell `(r, c)` with `prevVal` being the value of the previous cell in the path.
#    - If the current cell is out of bounds or its value is not greater than `prevVal`, return `0` as it does not form a valid increasing path.
#    - If the result for the current cell `(r, c)` is already cached in `dp`, return the cached result to avoid re-computation.
#    - Initialize `res` to `1` since the cell itself forms a path of length 1.
#    - Recursively explore all four possible directions (up, down, left, right) and update `res` with the maximum path length found.
#    - Cache the result in `dp` and return it.

# 3. **Main Function**:
#    - Iterate over all cells in the matrix and call the DFS function starting from each cell.
#    - The longest increasing path is the maximum value stored in `dp` after all DFS calls.

# ### Time and Space Complexities

# - **Time Complexity**: \(O(M \times N)\), where \(M\) is the number of rows and \(N\) is the number of columns in the matrix. Each cell is visited once and each DFS call explores four possible directions, but the results are cached to avoid redundant calculations.
# - **Space Complexity**: \(O(M \times N)\) for the memoization dictionary `dp`.


# ```python
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         ROWS, COLS = len(matrix), len(matrix[0])
#         dp = {}

#         def dfs(r, c, prevVal):
#             if (r < 0 or r == ROWS or
#                 c < 0 or c == COLS or 
#                 matrix[r][c] <= prevVal):
#                 return 0
            
#             if (r, c) in dp:
#                 return dp[(r, c)]
        
#             res = 1
#             res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
#             res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
#             res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
#             res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
#             dp[(r,c)] = res
#             return res

#         for r in range(ROWS):
#             for c in range(COLS):
#                 dfs(r, c, -1)
#         return max(dp.values())
# ```

# This solution uses DFS with memoization to efficiently find the longest increasing path in the matrix by exploring all possible paths while caching results to avoid redundant computations.