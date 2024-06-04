class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        ans, sol = [], []
        letter_map = {
            "2" : "abc", 
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        n = len(digits)
        def backtrack(i): 
            if n == i:
                ans.append("".join(sol))
                return 
            for letter in letter_map[digits[i]]:
                sol.append(letter)
                backtrack(i + 1)
                sol.pop()
        backtrack(0)
        return ans


# **Intuition:**

# The problem asks for all possible letter combinations corresponding to a phone number represented by digits. Each digit maps to a set of letters (e.g., "2" maps to "abc"). This code uses a backtracking approach to explore all possible combinations of letters for each digit in the phone number.

# **Approach:**

# 1. **Initialization:**
#    - An empty list `ans` stores the final result, which will contain all valid letter combinations.
#    - A temporary list `sol` holds the current combination being constructed during backtracking.
#    - A dictionary `letter_map` associates each digit with its corresponding set of letters.

# 2. **Base Case:**
#    - If the current index `i` reaches the length of the digits string (`n`), it signifies a complete combination has been formed. Join the letters in `sol` to form a string and append it to the result list `ans` using `"".join(sol)`.

# 3. **Backtracking Function:**
#    - For the current digit (`digits[i]`), iterate through all its corresponding letters (`letter in letter_map[digits[i]]`).
#      - Append the current letter (`letter`) to the temporary solution list (`sol.append(letter)`).
#      - Make a recursive call to `backtrack(i + 1)` to explore further possibilities. This call considers the current letter and explores combinations for the remaining digits (incrementing `i` by 1).
#      - After the recursive call returns, backtrack by removing the appended letter from `sol` (`sol.pop()`) to consider other combinations and avoid modifications in later recursive calls.

# 4. **Main Function Call:**
#    - Initiate the backtracking exploration by calling `backtrack(0)`, starting from the beginning of the digits string (`i = 0`).

# **Time Complexity:**

# - In the worst case, for each digit, we might explore all possible letters associated with it (branching factor of `len(letter_map[digits[i]])`).
# - The recursion tree can have a depth of `len(digits)` (number of digits).
# - The overall time complexity can be considered O(N^M), where `N` is the average number of letters per digit and `M` is the number of digits, due to the exponential nature of exploring all possibilities.

# **Space Complexity:**

# - The recursion stack, in the worst case, can have a depth of `len(digits)`.
# - The `sol` list scales linearly with the depth of recursion, holding the current combination being constructed.
# - Therefore, the space complexity is dominated by the recursion stack, which is O(len(digits)).

# **Key Points:**

# - Backtracking allows for systematic exploration of all possible letter combinations.
# - The `letter_map` dictionary efficiently maps digits to their corresponding letters.
# - The time complexity is exponential in the worst case, where the number of combinations grows with the number of digits.

# **Additional Considerations:**

# - The worst-case time complexity could be a concern for long phone numbers. If optimization is necessary, consider iterative approaches that might be more efficient for this specific problem.
# - For very large numbers of digits, the space complexity might be a factor. If memory is a concern, explore alternative algorithms that might have lower space requirements.