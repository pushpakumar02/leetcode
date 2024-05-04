class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)

# Intuition and Approach:

# - The problem requires evaluating the total score based on a list of valid operations.
# - We use a stack to keep track of the scores during evaluation.
# - We iterate through each operation in the list.
# - For each operation:
#   - If it's a digit (an integer), we convert it to an integer and push it onto the stack.
#   - If it's "+", we add the last two scores from the stack and push the sum onto the stack.
#   - If it's "D", we double the last score on the stack and push it.
#   - If it's "C", we remove the last score from the stack.
# - Finally, we return the sum of all the scores remaining on the stack.

# Time Complexity: O(n) - where n is the length of the `operations` list. We iterate through the list once.

# Space Complexity: O(n) - where n is the length of the `operations` list. In the worst case, the stack could contain all elements of `operations`, for example, if all elements are digits.