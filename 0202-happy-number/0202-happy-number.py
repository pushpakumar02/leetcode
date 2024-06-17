class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.SumOfSquered(n)

            if n == 1:
                return True
        return False
        
    def SumOfSquered(self, n):
        output = 0

        while n:
            num1 = (n % 10) ** 2
            output += num1
            n = n // 10
        return output



### Intuition

# To determine if a number is a "happy" number, we need to repeatedly replace the number with the sum of the squares of its digits. A number is considered happy if this process eventually leads to 1. If it leads to a cycle (i.e., we encounter the same number again), the number is not happy.

# ### Approach

# 1. **Detect Cycle**: Use a set to keep track of numbers we have already encountered. If we encounter the same number again before reaching 1, we have detected a cycle.
# 2. **Sum of Squares Function**: Implement a helper function to calculate the sum of the squares of the digits of a number.

# ### Steps

# 1. Initialize an empty set `visit` to store the numbers we encounter during the process.
# 2. Iterate until we either reach 1 or detect a cycle:
#    - Add the current number to the set.
#    - Replace the number with the sum of the squares of its digits using the helper function.
#    - If the new number is 1, return `True`.
# 3. If we encounter a number that is already in the set, return `False` as it indicates a cycle.

# ### Time and Space Complexities

# - **Time Complexity**: The time complexity is difficult to pinpoint exactly due to the nature of the problem, but generally, it should be O(log n), where n is the current number, because the number of digits in n decreases over iterations.
# - **Space Complexity**: O(log n) for storing the intermediate results in the set.

# ### Implementation

# ```python
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         visit = set()

#         while n not in visit:
#             visit.add(n)
#             n = self.sumOfSquares(n)

#             if n == 1:
#                 return True
#         return False
        
#     def sumOfSquares(self, n):
#         output = 0
#         while n:
#             digit = n % 10
#             output += digit ** 2
#             n //= 10
#         return output
# ```

# ### Explanation

# 1. **Main Function `isHappy`**:
#    - Initialize a set `visit` to keep track of seen numbers.
#    - Use a while loop to continue the process until either we find 1 or detect a cycle.
#    - In each iteration, add the current number to the set and compute the sum of the squares of its digits using the `sumOfSquares` function.
#    - If the new number is 1, return `True`. If we encounter a number that is already in the set, return `False`.

# 2. **Helper Function `sumOfSquares`**:
#    - Initialize `output` to 0.
#    - While `n` is not 0, extract the last digit of `n`, square it, and add it to `output`.
#    - Remove the last digit from `n` using integer division.
#    - Return `output` after the loop completes.

# This approach ensures that we can detect cycles and correctly identify happy numbers.