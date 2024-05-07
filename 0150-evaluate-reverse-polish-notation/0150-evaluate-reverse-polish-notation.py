class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a , b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a , b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]



# Intuition:
# - Reverse Polish Notation (RPN) is a mathematical notation where every operator follows all of its operands.
# - In this problem, we're given a list of tokens representing an RPN expression, and we need to evaluate it.

# Approach:
# - We use a stack to keep track of intermediate results.
# - We iterate through each token in the given list of tokens:
#   - If the token is an operand (a number), we push it onto the stack.
#   - If the token is an operator ("+", "-", "*", "/"):
#     - For addition and multiplication, we pop the last two operands from the stack, perform the operation, and push the result back onto the stack.
#     - For subtraction and division, since the order matters (last operand subtracted from the penultimate operand, and last operand divides the penultimate operand), we pop the last two operands in reversed order, perform the operation, and push the result back onto the stack.
# - After processing all tokens, the final result will be the only remaining element in the stack.

# Time Complexity: O(n), where n is the number of tokens in the input list. We iterate through each token once.

# Space Complexity: O(n), where n is the number of tokens in the input list. We use a stack to store the operands and intermediate results. In the worst case, the stack size will be the same as the number of tokens.