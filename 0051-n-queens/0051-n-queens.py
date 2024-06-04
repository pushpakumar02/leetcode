class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set ()
        negDiag = set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if n == r:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or (r + c) in posDiag or ( r - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add((r + c))
                negDiag.add(( r - c))
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove((r + c))
                negDiag.remove(( r - c))
                board[r][c] = "."

        backtrack(0)
        return res

### Intuition and Approach for `solveNQueens`

#### Intuition
# The N-Queens problem is a classic backtracking problem where we need to place N queens on an N×N chessboard so that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

# #### Approach
# 1. **Board Setup**:
#    - Initialize the board as a list of lists with dots (".") representing empty spaces.
#    - Use sets to keep track of columns (`col`), positive diagonals (`posDiag`), and negative diagonals (`negDiag`) that are already occupied by queens.

# 2. **Backtracking Function**:
#    - Use a recursive function `backtrack(r)` where `r` is the current row.
#    - **Base Case**: If `r` equals `n`, it means all queens are placed successfully. Convert the board to the required format and add it to the result list.
#    - **Recursive Case**:
#      - Iterate over each column `c` in the current row.
#      - Skip the column if it's already occupied by another queen or if placing a queen at `(r, c)` would put it on an occupied diagonal.
#      - Place the queen at `(r, c)`, mark the column and diagonals as occupied.
#      - Recurse to the next row.
#      - After returning from the recursion, backtrack by removing the queen and unmarking the column and diagonals.

# 3. **Final Result**:
#    - Start the backtracking from the first row (0).
#    - Return the result list containing all valid board configurations.

# #### Time Complexity
# - **Exponential Time**: \(O(N!)\), where \(N\) is the number of queens. This is because the algorithm tries all possible placements for each queen.

# #### Space Complexity
# - **O(N^2)**: for the board and sets used to track columns and diagonals.
# - **O(N)**: for the recursion stack depth.

