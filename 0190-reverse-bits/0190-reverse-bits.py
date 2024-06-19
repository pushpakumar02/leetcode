class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 
            res = res | (bit << 31 - i )
        return res 


# ### Intuition and Approach

# The task is to reverse the bits of a given 32-bit unsigned integer. To accomplish this, we'll examine each bit of the input integer from right to left, and set the corresponding bit in the result from left to right.

# #### Step-by-Step Approach:

# 1. **Initialize Result**:
#    - Start with a result `res` initialized to 0. This variable will accumulate the reversed bits.

# 2. **Loop Through Bits**:
#    - Iterate over each bit position from 0 to 31.
#    - In each iteration, perform the following steps:
#      - Extract the bit at the current position `i` from the input number `n` by using a bitwise right shift and bitwise AND operation: `(n >> i) & 1`.
#      - Set the corresponding bit in the result `res` by using a bitwise left shift and bitwise OR operation: `res | (bit << (31 - i))`.

# 3. **Return Result**:
#    - After completing the loop, the result `res` will contain the reversed bits of the input number `n`.

# ### Time Complexity

# - **Time Complexity**: \(O(1)\)
#   - The loop runs a fixed number of times (32 iterations), so the time complexity is constant.

# ### Space Complexity

# - **Space Complexity**: \(O(1)\)
#   - The algorithm uses a constant amount of extra space.

# ### Implementation

# Here's the implementation of the described approach:

# ```python
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         for i in range(32):
#             bit = (n >> i) & 1  # Extract the bit at position i
#             res = res | (bit << (31 - i))  # Set the corresponding bit in the result
#         return res 
# ```

# ### Explanation

# 1. **Initialize `res`**:
#    - `res` is set to 0. This variable will store the reversed bits.

# 2. **Loop Through Bits**:
#    - The loop runs from `i = 0` to `i = 31`.
#    - For each `i`:
#      - Extract the `i`-th bit of `n` by right-shifting `n` by `i` positions and then taking the bitwise AND with 1: `(n >> i) & 1`.
#      - Set the bit at position `31 - i` in `res` using a bitwise OR: `res | (bit << (31 - i))`.

# 3. **Return `res`**:
#    - After processing all 32 bits, `res` contains the reversed bits of `n`.

# ### Example

# For instance, let's consider reversing the bits of `n = 0b00000010100101000001111010011100`:

# - Initial `res = 0`.
# - On each iteration, extract the bit and set it in the correct position in `res`.

# After 32 iterations, the final `res` will be `0b00111001011110000010100101000000`, which is the reverse of the input bits.