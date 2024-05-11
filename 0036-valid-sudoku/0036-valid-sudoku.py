class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                # else:
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])
        return True



# Intuition:
# - To determine if a Sudoku board is valid, we need to ensure that no number is repeated within each row, each column, and each 3x3 subgrid.

# Approach:
# 1. We use three defaultdicts: `rows`, `cols`, and `squares` to keep track of the numbers seen in each row, column, and 3x3 subgrid respectively.
# 2. We iterate through each cell in the Sudoku board.
# 3. For each non-empty cell:
#    - We check if the number is already present in the corresponding row, column, or subgrid. If it is, the board is invalid, and we return `False`.
#    - If the number is not present, we add it to the respective sets in `rows`, `cols`, and `squares`.
# 4. If all cells are checked without any conflicts, we return `True`, indicating that the board is valid.

# Time Complexity: O(1), because the size of the Sudoku board is fixed (9x9), and the solution iterates through each cell exactly once.

# Space Complexity: O(1), as the space used is constant regardless of the input size. The space complexity is also O(1) because the size of the Sudoku board is fixed, and the solution uses three defaultdicts with a constant number of elements.