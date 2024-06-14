class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin -1, leftMax - 1 
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if  leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0


### Intuition

# The problem is about checking whether a given string containing `(`, `)`, and `*` is a valid string. A string is valid if the parentheses are balanced, and the asterisks `*` can be treated as either `(`, `)`, or an empty string. The main challenge is handling the flexibility that `*` introduces.

# ### Approach

# We maintain two counters:
# 1. `leftMin`: The minimum number of unmatched left parentheses we could have.
# 2. `leftMax`: The maximum number of unmatched left parentheses we could have.

# The idea is to iterate through the string and update these counters based on the current character:
# - For `(`, we increment both `leftMin` and `leftMax` because it increases the potential for more unmatched left parentheses.
# - For `)`, we decrement both `leftMin` and `leftMax` because it closes one of the unmatched left parentheses.
# - For `*`, we consider it as three possibilities: an unmatched left parenthesis `(`, an unmatched right parenthesis `)`, or an empty string. Therefore, we decrement `leftMin` (treating `*` as `)`), and we increment `leftMax` (treating `*` as `(`).

# Throughout the process, if `leftMax` becomes negative, it means there are more closing parentheses than can be matched, and the string is invalid. If `leftMin` becomes negative, it means there are more closing parentheses than can be matched at that point, but we reset it to 0 because `leftMin` should never be less than zero (it represents a possible count of unmatched left parentheses, which cannot be negative).

# Finally, for the string to be valid, `leftMin` must be zero at the end because it represents the minimum possible count of unmatched left parentheses, which should be balanced.

# ### Time and Space Complexities

# - **Time Complexity**: \(O(N)\), where \(N\) is the length of the string. This is because we only traverse the string once.
# - **Space Complexity**: \(O(1)\), as we use only a fixed amount of extra space regardless of the input size.

# ### Implementation

# ```python
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         leftMin, leftMax = 0, 0

#         for c in s:
#             if c == "(":
#                 leftMin += 1
#                 leftMax += 1
#             elif c == ")":
#                 leftMin -= 1
#                 leftMax -= 1 
#             else:  # c == '*'
#                 leftMin -= 1
#                 leftMax += 1

#             # If at any point, the maximum number of unmatched left parentheses is negative, return False
#             if leftMax < 0:
#                 return False

#             # Ensure the minimum number of unmatched left parentheses does not go below zero
#             if leftMin < 0:
#                 leftMin = 0

#         # For the string to be valid, the minimum number of unmatched left parentheses should be zero
#         return leftMin == 0
# ```

# ### Explanation

# 1. **Initialization**: Start with `leftMin` and `leftMax` both set to 0.
# 2. **Update Counters**: For each character in the string, update `leftMin` and `leftMax` based on the rules explained.
# 3. **Check Validity**: If at any point `leftMax` becomes negative, the string is invalid. Reset `leftMin` to 0 if it becomes negative.
# 4. **Final Check**: After processing the entire string, return `True` if `leftMin` is 0, indicating that the string is balanced.

# This method efficiently handles the flexibility of `*` and ensures the string is valid by tracking the possible range of unmatched left parentheses throughout the string.