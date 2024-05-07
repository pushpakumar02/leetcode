class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return 

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN: 
                stack.append(")")
                backtrack(openN , closeN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res



# Intuition:
# - To generate all valid parentheses combinations, we can use backtracking.
# - At each step, we have two choices: to open a new left parenthesis or to close a previously opened parenthesis.
# - We maintain counts of open and close parentheses to ensure that we generate valid combinations.

# Approach:
# - We use backtracking to generate all valid combinations of parentheses.
# - We start with an empty stack and an empty result list.
# - In the `backtrack` function, we keep track of the counts of open and close parentheses (`openN` and `closeN`).
# - If both counts reach `n`, we've formed a valid combination, so we append it to the result.
# - If the count of open parentheses (`openN`) is less than `n`, we can add an open parenthesis. We add it to the stack, increment `openN`, and recursively call `backtrack`.
# - If the count of close parentheses (`closeN`) is less than `openN`, we can add a close parenthesis. We add it to the stack, increment `closeN`, and recursively call `backtrack`.
# - After each recursive call, we remove the last added parenthesis from the stack to backtrack.
# - Finally, we call `backtrack(0, 0)` to start the recursion with initial counts of open and close parentheses being zero.

# Time Complexity: \(O(2^n)\) - In each recursive call, we have two choices (either open or close a parenthesis), and we make \(2n\) total decisions (n decisions for opening and n decisions for closing).

# Space Complexity: \(O(n)\) - The maximum size of the call stack is \(n\) due to recursion, and the stack stores the sequence of parentheses. Additionally, the `res` list may store up to \(2n\) strings, where each string has length \(2n\), giving an overall space complexity of \(O(n)\).