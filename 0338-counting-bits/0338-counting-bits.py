class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp




### Intuition and Approach

# The task is to count the number of '1' bits (also known as the Hamming weight) for each number from 0 to `n`. We need to return an array where the `i`-th element is the count of '1' bits in the binary representation of `i`.

# #### Dynamic Programming Approach:

# 1. **Observation**:
#    - The number of '1' bits in a number `i` can be derived from the number of '1' bits in some smaller number plus one more '1' bit.
#    - Specifically, if `i` is a power of 2 (i.e., `i` is in the form of `2^k`), then `i` has exactly one '1' bit.
#    - For any number `i`, it can be represented as `i = 2^m + x`, where `2^m` is the largest power of 2 less than or equal to `i`, and `x` is some remainder.
#    - The count of '1' bits in `i` is then `1 +` the count of '1' bits in `x`.

# 2. **Dynamic Programming Table (DP Table)**:
#    - Create an array `dp` of size `n+1` where `dp[i]` represents the number of '1' bits in the binary representation of `i`.
#    - Initialize `dp[0]` to 0 since the number 0 has zero '1' bits.

# 3. **Filling the DP Table**:
#    - Use a variable `offset` to keep track of the largest power of 2 less than or equal to the current index.
#    - For each `i` from 1 to `n`:
#      - When `i` equals `offset * 2`, update `offset` to `i` since we've reached a new power of 2.
#      - Compute `dp[i]` as `1 + dp[i - offset]`.

# ### Time Complexity

# - **Time Complexity**: \(O(n)\)
#   - The loop runs from 1 to `n`, performing a constant amount of work in each iteration.

# ### Space Complexity

# - **Space Complexity**: \(O(n)\)
#   - The algorithm uses an array of size `n+1` to store the results.

# ### Implementation

# Here's the implementation of the described approach:

# ```python
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         dp = [0] * (n + 1)
#         offset = 1

#         for i in range(1, n + 1):
#             if offset * 2 == i:
#                 offset = i
#             dp[i] = 1 + dp[i - offset]
#         return dp
# ```

### Explanation

# 1. **Initialization**:
#    - `dp` array is initialized with zeros of size `n+1`.
#    - `offset` is initialized to 1, representing the smallest power of 2.

# 2. **Loop**:
#    - For each `i` from 1 to `n`:
#      - If `i` equals `offset * 2`, update `offset` to `i` (indicating that `i` is a power of 2).
#      - Calculate `dp[i]` as `1 + dp[i - offset]` where `i - offset` gives the remainder after subtracting the largest power of 2 less than or equal to `i`.

# 3. **Result**:
#    - After filling up the `dp` array, return it as the result. Each entry `dp[i]` will contain the number of '1' bits in the binary representation of `i`.