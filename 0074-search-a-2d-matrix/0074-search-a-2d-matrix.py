class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        l = 0
        r = t - 1

        while l <= r:
            m = (l + r) // 2
            i = m // n
            j = m % n 

            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                r = m - 1
            else:
                l = m + 1
        return False


### Intuition and Approach

# 1. **Matrix as 1D Array**:
#    - Treat the 2D matrix as a 1D sorted array to apply binary search. This can be done because the matrix rows are sorted and the first integer of each row is greater than the last integer of the previous row.

# 2. **Index Mapping**:
#    - Map the 1D index to 2D indices. Given a 1D index `m`, the corresponding row and column indices in the 2D matrix can be found using:
#      - `i = m // n` (row index)
#      - `j = m % n` (column index)
#    - Here, `n` is the number of columns in the matrix.

# 3. **Binary Search**:
#    - Initialize `l` as 0 and `r` as the total number of elements minus one.
#    - Calculate the middle index `m`.
#    - Map `m` to its corresponding 2D indices to find `mid_num`.
#    - Compare `mid_num` with `target`:
#      - If `target` is equal to `mid_num`, return `True`.
#      - If `target` is less than `mid_num`, search the left half by updating `r`.
#      - If `target` is greater than `mid_num`, search the right half by updating `l`.
#    - If the target is not found, return `False`.

# ### Time Complexity
# - **O(log(m * n))**: The binary search runs in logarithmic time relative to the number of elements in the matrix (m rows and n columns).

# ### Space Complexity
# - **O(1)**: The algorithm uses constant extra space, only using a few variables for indices and comparisons.

