class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            else:
                grid[i][j] = 0
                return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
                    
        return max_area

### Intuition
# To find the maximum area of an island in a grid, treat the grid as a graph where each cell is a node. An island is a connected component of 1's (land) surrounded by 0's (water). Use Depth-First Search (DFS) to explore each island and calculate its area.

# ### Approach
# 1. **Initialization**:
#    - Get the dimensions of the grid.
#    - Initialize a variable to keep track of the maximum area of an island found.

# 2. **DFS Helper Function**:
#    - Recursively visit all connected 1's (land) from the current cell.
#    - Mark each visited cell as 0 (water) to avoid counting it again.
#    - Return the total area of the island.

# 3. **Traversal**:
#    - Iterate through each cell in the grid.
#    - If a cell contains 1 (land), it is the start of a new island.
#    - Use DFS to calculate the area of the island and update the maximum area if necessary.

# ### Time Complexity
# - **Time**: \(O(m \times n)\), where \(m\) is the number of rows and \(n\) is the number of columns. Each cell is visited at most once.

# ### Space Complexity
# - **Space**: \(O(m \times n)\) in the worst case due to the recursion stack in DFS when the grid is filled with 1's.

# This approach ensures that every cell is visited once, and the area of each island is calculated accurately.
