class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j] 


### Intuition

# To rotate a matrix by 90 degrees clockwise in-place, we can use a two-step process:

# 1. **Transpose the Matrix**: Convert all rows to columns and vice versa.
# 2. **Reverse Each Row**: Reverse the elements in each row.

# This approach leverages the symmetry of the matrix and ensures that the rotation is done in-place, modifying the original matrix without requiring additional space.

# ### Steps

# 1. **Transpose the Matrix**: Swap elements at position `(i, j)` with `(j, i)`.
#    - Iterate through each element above the diagonal (`i < j`) and swap it with its counterpart.
# 2. **Reverse Each Row**: Reverse the order of elements in each row.
#    - Iterate through each row and swap elements from the start and end towards the center.

# ### Time and Space Complexities

# - **Time Complexity**: O(n^2), where n is the number of rows (or columns) in the matrix. We need to visit each element twice: once for transposing and once for reversing.
# - **Space Complexity**: O(1), as we are performing the operations in-place without using extra space.

# ### Implementation

# ```python
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)

#         # Transpose the matrix
#         for i in range(n):
#             for j in range(i + 1, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#         # Reverse each row
#         for i in range(n):
#             for j in range(n // 2):
#                 matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
# ```

# ### Explanation

# 1. **Transpose the Matrix**:
#    - We iterate through each element above the diagonal (`i < j`) and swap it with its counterpart to achieve the transpose.
#    - For example, element at position `(0, 1)` is swapped with `(1, 0)`.

# 2. **Reverse Each Row**:
#    - After transposing, each row is reversed to complete the 90-degree rotation.
#    - We swap elements from the start and end towards the center for each row.
#    - For example, in a row of length `n`, the element at position `j` is swapped with the element at position `n-j-1`.

# By following these steps, we achieve an in-place 90-degree clockwise rotation of the matrix. This approach is efficient and leverages the properties of matrix transposition and row reversal to perform the rotation correctly.