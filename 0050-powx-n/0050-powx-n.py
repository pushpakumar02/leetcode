class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            res = helper(x*x , n//2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1/res



# To solve the problem of computing \( x \) raised to the power \( n \) (i.e., \( x^n \)), we can utilize a divide-and-conquer approach known as exponentiation by squaring. This approach is efficient and reduces the time complexity to \( O(\log n) \). Here's a step-by-step explanation and implementation:

# ### Steps

# 1. **Base Cases**:
#    - If \( x \) is 0, the result is always 0 (assuming \( n \neq 0 \)).
#    - If \( n \) is 0, the result is always 1 (any number raised to the power of 0 is 1).

# 2. **Recursive Function (helper)**:
#    - The main idea is to reduce the problem size by half at each step. This is done by squaring the base \( x \) and halving the exponent \( n \).
#    - If \( n \) is even, \( x^n = (x^2)^{n/2} \).
#    - If \( n \) is odd, \( x^n = x \times (x^2)^{(n-1)/2} \).

# 3. **Handling Negative Exponents**:
#    - If \( n \) is negative, compute \( x^{-n} \) and take the reciprocal of the result.

# 4. **Combine Results**:
#    - Use the results of recursive calls to build up the final result.

# ### Time and Space Complexity

# - **Time Complexity**: \( O(\log n) \) because we halve the exponent at each recursive step.
# - **Space Complexity**: \( O(\log n) \) due to the recursion stack.

# ### Implementation

# Here's the implementation of the described approach:

# ```python
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def helper(x, n):
#             if x == 0: 
#                 return 0
#             if n == 0: 
#                 return 1
#             res = helper(x * x, n // 2)
#             return x * res if n % 2 else res

#         res = helper(x, abs(n))
#         return res if n >= 0 else 1 / res
# ```

# ### Explanation of the Implementation

# 1. **Base Cases**:
#    - `if x == 0: return 0`: Handles the case where the base \( x \) is zero.
#    - `if n == 0: return 1`: Handles the case where the exponent \( n \) is zero.

# 2. **Recursive Function (helper)**:
#    - `res = helper(x * x, n // 2)`: Recursively calls the helper function with the squared base and halved exponent.
#    - `return x * res if n % 2 else res`: If \( n \) is odd, multiply the result by \( x \); otherwise, return the result.

# 3. **Handling Negative Exponents**:
#    - `res = helper(x, abs(n))`: Compute the power for the absolute value of \( n \).
#    - `return res if n >= 0 else 1 / res`: If \( n \) is negative, return the reciprocal of the computed result.

# This implementation efficiently computes the power function using recursion and handles both positive and negative exponents correctly.