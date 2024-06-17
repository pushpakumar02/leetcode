class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


### Intuition

# To traverse a matrix in a spiral order, we follow a systematic approach that moves in the following sequence:
# 1. **Left to Right**: Traverse the top row from the left boundary to the right boundary.
# 2. **Top to Bottom**: Traverse the right column from the top boundary to the bottom boundary.
# 3. **Right to Left**: Traverse the bottom row from the right boundary to the left boundary.
# 4. **Bottom to Top**: Traverse the left column from the bottom boundary to the top boundary.

# We continue this process while shrinking the boundaries (left, right, top, bottom) after each traversal until the entire matrix is covered.

# ### Steps

# 1. **Initialize Boundaries**:
#    - `left` and `top` start at 0.
#    - `right` is the number of columns.
#    - `bottom` is the number of rows.

# 2. **Traverse in Spiral Order**:
#    - **Left to Right**: Traverse the top row from `left` to `right-1`, then increment `top`.
#    - **Top to Bottom**: Traverse the right column from `top` to `bottom-1`, then decrement `right`.
#    - **Right to Left**: Traverse the bottom row from `right-1` to `left`, then decrement `bottom`.
#    - **Bottom to Top**: Traverse the left column from `bottom-1` to `top`, then increment `left`.

# 3. **Continue Until Boundaries Overlap**:
#    - Repeat the above steps until the `left` boundary crosses the `right` boundary or the `top` boundary crosses the `bottom` boundary.

# ### Time and Space Complexities

# - **Time Complexity**: O(m * n), where m is the number of rows and n is the number of columns. Each element is visited exactly once.
# - **Space Complexity**: O(1) extra space, aside from the space required to store the result, since we are modifying the result list in place.

# ### Implementation

# ```python
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#         left, right = 0, len(matrix[0])
#         top, bottom = 0, len(matrix)

#         while left < right and top < bottom:
#             # Traverse from left to right
#             for i in range(left, right):
#                 res.append(matrix[top][i])
#             top += 1
            
#             # Traverse from top to bottom
#             for i in range(top, bottom):
#                 res.append(matrix[i][right - 1])
#             right -= 1
            
#             if not (left < right and top < bottom):
#                 break
            
#             # Traverse from right to left
#             for i in range(right - 1, left - 1, -1):
#                 res.append(matrix[bottom - 1][i])
#             bottom -= 1
            
#             # Traverse from bottom to top
#             for i in range(bottom - 1, top - 1, -1):
#                 res.append(matrix[i][left])
#             left += 1

#         return res
# ```

# ### Explanation

# 1. **Initialization**:
#    - Define the boundaries (`left`, `right`, `top`, `bottom`).

# 2. **Traverse the Matrix**:
#    - Append elements to `res` while traversing from `left` to `right` on the top row.
#    - Move the `top` boundary down.
#    - Append elements while traversing from `top` to `bottom` on the right column.
#    - Move the `right` boundary left.
#    - Check if boundaries still make sense for further traversal.
#    - Append elements while traversing from `right` to `left` on the bottom row.
#    - Move the `bottom` boundary up.
#    - Append elements while traversing from `bottom` to `top` on the left column.
#    - Move the `left` boundary right.

# 3. **End Condition**:
#    - The loop terminates when the `left` boundary meets or exceeds the `right` boundary, or the `top` boundary meets or exceeds the `bottom` boundary.

# This method ensures that every element in the matrix is covered in a spiral order and appended to the result list `res`.