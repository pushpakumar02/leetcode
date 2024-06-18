class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res


### Intuition and Approach

# The task is to count the number of '1' bits in the binary representation of a given integer `n`. This is also known as calculating the Hamming weight or population count of the integer.

# #### Efficient Approach using Bit Manipulation:

# 1. **Bit Manipulation Insight**:
#    - The expression `n & (n - 1)` clears the lowest set bit (i.e., the rightmost '1') in `n`.
#    - Repeatedly applying this operation will eventually turn `n` into 0, and the number of times this operation is performed corresponds to the number of '1' bits in `n`.

# 2. **Procedure**:
#    - Initialize a counter `res` to 0 to keep track of the number of '1' bits.
#    - While `n` is not zero, repeatedly apply `n = n & (n - 1)` and increment the counter `res`.
#    - The loop terminates when `n` becomes zero, and `res` will contain the Hamming weight.

# ### Time Complexity

# - **Time Complexity**: \(O(k)\), where \(k\) is the number of '1' bits in the binary representation of `n`.
#   - In the worst case, this is \(O(\log n)\), where \(n\) is the input number. This is because the number of bits in an integer `n` is approximately \(\log_2 n\).

# ### Space Complexity

# - **Space Complexity**: \(O(1)\)
#   - The algorithm uses a constant amount of additional space regardless of the size of the input integer.

# ### Implementation

# Here's the implementation of the described approach:

# ```python
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             n &= (n - 1)
#             res += 1
#         return res
# ```

# ### Explanation

# 1. **Initialization**: `res` is initialized to 0.
# 2. **Loop**:
#    - The condition `while n:` ensures that we continue the loop as long as `n` is not zero.
#    - Within each iteration, `n = n & (n - 1)` removes the lowest set bit from `n`.
#    - Each time a bit is removed, we increment the `res` counter.
# 3. **Termination**:
#    - The loop exits when all bits in `n` have been cleared (i.e., `n` becomes zero).
#    - `res` now contains the total number of '1' bits in the original binary representation of `n`.

# This approach is efficient and leverages a key property of binary numbers to count the '1' bits with minimal operations.