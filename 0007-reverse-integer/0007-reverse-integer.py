class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31
        MAX = 2147483647   # 2^31 - 1

        res = 0
        while x:
            # Extract the digit
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            
            # Check for overflow/underflow
            if res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10):
                return 0
            
            # Append the digit
            res = (res * 10) + digit 
        
        return res



### Intuition and Approach

# To reverse an integer `x`, we need to handle several edge cases, including:

# 1. **Handling Negative Numbers**: The approach should be able to reverse both positive and negative integers.
# 2. **Avoiding Overflow**: Since reversing a large integer might lead to overflow, we need to check whether the result is within the 32-bit signed integer range \([-2^{31}, 2^{31} - 1]\).

# ### Approach

# 1. **Initialization**:
#    - Define `MIN` and `MAX` constants to represent the minimum and maximum bounds of a 32-bit signed integer.

# 2. **Digit Extraction and Building the Result**:
#    - Use a loop to extract digits from `x` from the least significant to the most significant.
#    - Use modulo operation to get the last digit.
#    - Use integer division to remove the last digit from `x`.

# 3. **Check for Overflow/Underflow**:
#    - Before appending a new digit to `res`, check if it will overflow or underflow.
#    - For positive overflow, if `res` is greater than `MAX // 10` or equal to `MAX // 10` and the current digit is greater than `MAX % 10`, return 0.
#    - For negative overflow, if `res` is less than `MIN // 10` or equal to `MIN // 10` and the current digit is less than `MIN % 10`, return 0.

# 4. **Build the Result**:
#    - Multiply `res` by 10 and add the extracted digit.

# 5. **Return the Result**:
#    - After the loop, return the reversed integer stored in `res`.

# ### Time Complexity

# - **Time Complexity**: \(O(\log_{10}(\text{x}))\), because we process each digit of `x` once.
# - **Space Complexity**: \(O(1)\), since we use a constant amount of extra space.

# ### Implementation

# Here's the implementation of the described approach:

# ```python
# import math

# class Solution:
#     def reverse(self, x: int) -> int:
#         MIN = -2147483648  # -2^31
#         MAX = 2147483647   # 2^31 - 1

#         res = 0
#         while x != 0:
#             # Extract the digit
#             digit = int(math.fmod(x, 10))
#             x = int(x / 10)
            
#             # Check for overflow/underflow
#             if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
#                 return 0
#             if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
#                 return 0
            
#             # Append the digit
#             res = res * 10 + digit
        
#         return res
# ```

# ### Explanation

# 1. **Extract the Digit**:
#    - `digit = int(math.fmod(x, 10))` extracts the last digit of `x`.
#    - `x = int(x / 10)` updates `x` by removing the last digit.

# 2. **Check for Overflow/Underflow**:
#    - `res > MAX // 10` checks if appending another digit will overflow the positive bound.
#    - `res < MIN // 10` checks if appending another digit will underflow the negative bound.

# 3. **Build the Result**:
#    - `res = res * 10 + digit` appends the extracted digit to `res`.

# 4. **Return the Result**:
#    - Finally, return the reversed integer stored in `res`.

# This approach efficiently reverses an integer while handling potential overflow and ensuring that the result remains within the bounds of a 32-bit signed integer.