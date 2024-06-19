class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while (b&mask) > 0:
            a, b = a ^ b, (a&b) << 1
            print(bin(mask&a), mask&a,bin(a) ,a,bin(b), b, bin(mask&b), mask&b)
        print(bin(mask&a), mask&a,bin(a) ,a,bin(b), b, bin(mask&b), mask&b)
        return (a&mask) if b > 0 else a
        



### Intuition and Approach

# To compute the sum of two integers `a` and `b` without using the `+` or `-` operators, we can utilize bit manipulation. Specifically, we can use the bitwise XOR and AND operations along with bit shifting to simulate the process of addition.

# #### Approach:

# 1. **Bitwise XOR and AND**:
#    - The XOR operation `a ^ b` gives the sum without considering the carry.
#    - The AND operation `(a & b) << 1` gives the carry bits that need to be added to the result.

# 2. **Loop Until No Carry**:
#    - Repeat the process until there are no carry bits left to add.
#    - Use a mask `0xffffffff` to handle overflow and limit the result to 32 bits.

# 3. **Handling Negative Results**:
#    - If the final result needs to be signed (to handle negative numbers in 32-bit signed integer format), adjust accordingly.

# ### Time Complexity

# - **Time Complexity**: \(O(1)\) in the sense that the number of operations is bounded by the bit-length of the integers (usually 32 or 64), but practically it can be considered \(O(n)\) where `n` is the number of bits.

# ### Space Complexity

# - **Space Complexity**: \(O(1)\) as we use a constant amount of space.

# ### Implementation

# Here’s the implementation of the described approach:

# ```python
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         mask = 0xffffffff  # Mask to get the last 32 bits

#         while (b & mask) > 0:
#             a, b = a ^ b, (a & b) << 1
#             print(bin(mask & a), mask & a, bin(a), a, bin(b), b, bin(mask & b), mask & b)
        
#         # Handle overflow for negative numbers
#         return a if b == 0 else (a & mask) if a <= 0x7fffffff else ~(a ^ mask)
# ```

# ### Explanation

# 1. **Initialize Mask**:
#    - `mask = 0xffffffff` ensures that we only consider the last 32 bits of the integers.

# 2. **Loop to Add Without Carry**:
#    - The XOR `a ^ b` computes the sum of `a` and `b` without the carry.
#    - The AND `(a & b) << 1` computes the carry bits that need to be added in the next iteration.
#    - Print statements (which you might want to remove or comment out in production code) show intermediate steps and bit values for debugging purposes.

# 3. **Return Result**:
#    - If `b` becomes 0, it means there are no more carry bits left, and `a` contains the final sum.
#    - If `a` exceeds the range of a 32-bit signed integer, it adjusts to return the correct negative number using bitwise operations.

# ### Example

# Let's see an example to understand the process:

# Consider `a = 1` and `b = 2`:

# - Initial values: `a = 1`, `b = 2`
# - First iteration:
#   - `a ^ b` results in `3` (binary: `0b11`)
#   - `(a & b) << 1` results in `0` (binary: `0b0`)
# - Since `b` becomes 0, the loop stops, and the result is `3`.

# ### Conclusion

# This approach efficiently simulates the addition of two integers using bitwise operations, which are fundamental and fast operations in most processors. This method also handles potential overflow and negative values using appropriate bit masks and conditional checks.