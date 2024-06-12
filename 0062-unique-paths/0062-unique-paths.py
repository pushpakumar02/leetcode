class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            dp.append([0] * n)

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue                
                val = 0
                if i > 0:
                    val += dp[i-1][ j]
                if j > 0:
                    val += dp[i][j - 1]
                dp[i][j] = val
        return dp[m-1][n-1]


### Intuition
# The problem is to find the number of unique paths from the top-left corner to the bottom-right corner of an `m x n` grid, moving only down or right. This can be solved using dynamic programming by building up the number of ways to reach each cell from the starting cell.

# ### Approach
# 1. **Initialization**: Create a 2D list `dp` of size `m x n` initialized to 0, which will store the number of unique paths to reach each cell.
# 2. **Base Case**: The starting cell `dp[0][0]` should be set to 1 because there is exactly one way to be at the starting point (start there).
# 3. **Filling the DP Table**:
#    - Iterate through each cell in the grid.
#    - For each cell `(i, j)`, calculate the number of ways to reach that cell by summing the number of ways to reach the cell directly above it (`dp[i-1][j]`) and the cell directly to the left of it (`dp[i][j-1]`), if these cells are within the grid bounds.
# 4. **Result**: The value in the bottom-right corner `dp[m-1][n-1]` will be the total number of unique paths from the top-left to the bottom-right corner.

# ### Time Complexity
# - **Time**: \(O(m \times n)\), since we need to fill out an `m x n` matrix.
# - **Space**: \(O(m \times n)\), for storing the DP table.

# ### Summary
# 1. Initialize a DP table with all zeros.
# 2. Set the starting cell to 1.
# 3. Fill in the table by summing the values from the cell above and the cell to the left for each cell.
# 4. Return the value in the bottom-right corner of the table.