class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
                 

# Intuition and Approach:
 
# - We are given a string `s` containing only parentheses, brackets, and braces.
# - The task is to determine whether the parentheses are balanced.
# - We use a stack data structure to track opening symbols.
# - We also maintain a mapping `closeToOpen` where the keys are closing symbols and the values are corresponding opening symbols. This allows us to check if a closing symbol matches the most recent opening symbol in the stack.
# - We iterate through each character in `s`.
# - If the character is a closing symbol:
#   - If the stack is not empty and the top of the stack contains the matching opening symbol, we pop the opening symbol from the stack.
#   - If the above condition is not met, the parentheses are not balanced, so we return `False`.
# - If the character is an opening symbol, we push it onto the stack.
# - Finally, if the stack is empty, it means all opening symbols found their respective closing symbols and the parentheses are balanced. Otherwise, we have some opening symbols without closing symbols, and the parentheses are not balanced.

# Time Complexity: O(n) - where n is the length of the string `s`. We iterate through the string once.

# Space Complexity: O(n) - where n is the length of the string `s`. In the worst case, the stack can hold all characters of `s` if it consists only of opening symbols.
