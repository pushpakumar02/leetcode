class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or heights[r][c] < prevHeight:
                return

            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
                
        return res

### Intuition
# The problem requires identifying cells in a grid that can flow water to both the Pacific and Atlantic oceans. This can be approached by performing a Depth-First Search (DFS) from the cells adjacent to each ocean and marking the cells that can reach each ocean.

# ### Approach
# 1. **Initialization**:
#    - Define the dimensions of the grid.
#    - Create two sets, `pac` and `atl`, to store cells that can reach the Pacific and Atlantic oceans, respectively.

# 2. **DFS Function**:
#    - Implement a helper function `dfs(r, c, visited, prevHeight)` that performs DFS from a given cell.
#    - This function should:
#      - Return if the cell is out of bounds, already visited, or if the height of the current cell is less than the previous cell (indicating water cannot flow upwards).
#      - Add the cell to the visited set.
#      - Recursively call `dfs` for all four possible directions (up, down, left, right).

# 3. **Perform DFS from Ocean Borders**:
#    - For the Pacific Ocean (top and left borders):
#      - Perform DFS starting from each cell in the first row and each cell in the first column.
#    - For the Atlantic Ocean (bottom and right borders):
#      - Perform DFS starting from each cell in the last row and each cell in the last column.

# 4. **Collect Results**:
#    - Iterate through all cells in the grid.
#    - Add the cell to the result list if it is in both the `pac` and `atl` sets.

# ### Time Complexity
# - **Time**: \(O(m \times n)\), where \(m\) is the number of rows and \(n\) is the number of columns. Each cell is processed at most once for each ocean.

# ### Space Complexity
# - **Space**: \(O(m \times n)\), for the visited sets and the call stack during DFS.

