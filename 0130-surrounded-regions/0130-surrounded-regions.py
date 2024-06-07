class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return 
            board[r][c] = "T"

            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"  
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

### Intuition
# To solve the problem of capturing surrounded regions in a board, we can leverage Depth-First Search (DFS) to mark all 'O's that are connected to the boundary and thus should not be captured. All other 'O's that are not connected to the boundary will be surrounded by 'X's and should be captured.

# ### Approach
# 1. **Initialization**:
#    - Get the dimensions of the board.
#    - Define a helper function `capture` that performs DFS to mark connected 'O's starting from a given cell.

# 2. **Mark Boundary Connected 'O's**:
#    - Iterate through the cells on the borders of the board.
#    - If a cell contains 'O', perform DFS from that cell to mark all connected 'O's with a temporary marker 'T'.

# 3. **Capture Surrounded Regions**:
#    - Iterate through the entire board.
#    - Change all remaining 'O's (which are surrounded) to 'X'.

# 4. **Restore Boundary Connected 'O's**:
#    - Iterate through the board again.
#    - Change all 'T's back to 'O'.

# ### Time Complexity
# - **Time**: \(O(m \times n)\), where \(m\) is the number of rows and \(n\) is the number of columns. Each cell is processed at most once during marking and capturing.

# ### Space Complexity
# - **Space**: \(O(m \times n)\), for the recursion stack in the worst case during DFS.

