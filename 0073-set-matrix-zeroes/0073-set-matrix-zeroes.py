class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = col_flag = False
        ROWS, COLS = len(matrix), len(matrix[0])

        for m in range(ROWS):
            for n in range(COLS):
                if matrix[m][n] == 0:
                    if m == 0:
                        row_flag = True
                    if n == 0:
                        col_flag = True
                    elif m != 0 and n!= 0:
                        matrix[m][0] = 0
                        matrix[0][n] = 0
        
        for m in range(1, ROWS):
            for n in range(1, COLS):
                if matrix[m][0] == 0 or matrix[0][n] == 0:
                    matrix[m][n] = 0

        if row_flag:
            matrix[0] = [0] * COLS
        if col_flag:
            for m in range(ROWS):
                matrix[m][0] = 0


# To solve the problem of setting the entire row and column to zero when a zero is found in a matrix, we can use an efficient in-place algorithm that avoids using extra space for a separate marker matrix. Instead, we can utilize the first row and first column of the given matrix to store the markers. Here's a step-by-step breakdown of the solution:

# ### Steps

# 1. **Initialize Flags**:
#    - Use `row_flag` to check if the first row contains any zero.
#    - Use `col_flag` to check if the first column contains any zero.

# 2. **Mark Zeros in the First Row and Column**:
#    - Traverse through the matrix to find zeros. For any zero found at position `(m, n)`:
#      - If the zero is in the first row, set `row_flag` to `True`.
#      - If the zero is in the first column, set `col_flag` to `True`.
#      - Otherwise, mark the zero by setting `matrix[m][0]` and `matrix[0][n]` to zero.

# 3. **Use Markers to Set Zeros**:
#    - Traverse the matrix again starting from `1,1` (ignoring the first row and column for now). Use the markers in the first row and column to set the corresponding rows and columns to zero.

# 4. **Set the First Row and Column**:
#    - If `row_flag` is `True`, set the entire first row to zero.
#    - If `col_flag` is `True`, set the entire first column to zero.

# ### Time and Space Complexity

# - **Time Complexity**: O(m * n), where `m` is the number of rows and `n` is the number of columns. This is because we traverse the matrix twice.
# - **Space Complexity**: O(1) extra space, as we are modifying the matrix in-place and using only a few additional variables.

# ### Implementation

# ```python
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         row_flag = col_flag = False
#         ROWS, COLS = len(matrix), len(matrix[0])

#         # Step 1: Use the first row and column as markers
#         for m in range(ROWS):
#             for n in range(COLS):
#                 if matrix[m][n] == 0:
#                     if m == 0:
#                         row_flag = True
#                     if n == 0:
#                         col_flag = True
#                     elif m != 0 and n != 0:
#                         matrix[m][0] = 0
#                         matrix[0][n] = 0
        
#         # Step 2: Use markers to set corresponding rows and columns to zero
#         for m in range(1, ROWS):
#             for n in range(1, COLS):
#                 if matrix[m][0] == 0 or matrix[0][n] == 0:
#                     matrix[m][n] = 0

#         # Step 3: Set the first row and column if needed
#         if row_flag:
#             matrix[0] = [0] * COLS
#         if col_flag:
#             for m in range(ROWS):
#                 matrix[m][0] = 0
# ```

# This approach ensures that we efficiently set the required rows and columns to zero without needing additional space, making it optimal in terms of both time and space complexity.