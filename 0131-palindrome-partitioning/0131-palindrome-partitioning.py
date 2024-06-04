class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part = []
        res = []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return 
            for j in range(i, len(s)):
                if self.ispali(s, i , j):
                    part.append(s[i : j+1])
                    dfs(j + 1)
                    part.pop()
            
        dfs(0)
        return res

    def ispali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1 , r - 1
        return True 


# **Intuition:**

# The problem asks for all possible ways to partition a string `s` into palindromic substrings. A palindrome is a word that reads the same backward as forward (e.g., "racecar", "madam"). This code employs a backtracking approach to explore every possible division of the string into substrings and checks if each substring is a palindrome.

# **Approach:**

# 1. **Initialization:**
#    - An empty list `part` stores the current partition (individual substrings) being constructed during backtracking.
#    - `res` is the final result list that will hold all valid partitions.

# 2. **DFS Function:**
#    - **Base Case:** If the current index `i` reaches the end of the string (`len(s)`), it signifies a complete partition has been constructed. Append a copy of the current partition (`part[:]`) to the result list (`res`) to avoid modifications in later recursive calls.
#    - **Iterate Through Substrings:** Loop through all possible substrings starting from index `i` up to the end of the string (`len(s)`).
#      - **Check for Palindrome:** Call the helper function `ispali(s, i, j)` to verify if the current substring (`s[i:j+1]`) is a palindrome.
#      - **If Palindrome:** If the substring is a palindrome, append it to the current partition (`part.append(s[i:j+1])`).
#      - **Recursive Call:** Make a recursive call to `dfs(j + 1)` to explore further possibilities. This call considers partitions where the current substring is included and moves to the next character (`j + 1`) to start exploring the remaining string.
#      - **Backtrack:** After the recursive call returns, remove the appended substring from the current partition (`part.pop()`) to consider other partitions and prevent modifications in later recursive calls.

# 3. **Main Function Call:**
#    - Initiate the DFS exploration by calling `dfs(0)`, starting from the beginning of the string (`i = 0`).

# 4. **Helper Function (ispali):**
#    - This function checks if a substring `s[l:r+1]` (inclusive) is a palindrome using a two-pointer approach.
#    - It iterates while the left pointer (`l`) is less than the right pointer (`r`).
#      - If the characters at `s[l]` and `s[r]` don't match, the substring is not a palindrome. Return `False`.
#      - If they match, increment `l` and decrement `r` to move towards the center of the substring.
#    - If the loop completes without finding mismatches, the entire substring is a palindrome. Return `True`.

# **Time Complexity:**

# - In the worst case, for each character `s[i]`, we might explore all possible substrings starting from it. This leads to a branching factor of `len(s) - i`.
# - The recursion tree can have a depth of `len(s)` (number of characters) in the worst case, as we explore all possible divisions.
# - However, the actual complexity depends on the number of palindromic substrings in the string.
# - The overall time complexity can be considered O(2^(len(s))) in the worst case, but the exact complexity might be lower based on how many palindromes exist.

# **Space Complexity:**

# - The recursion stack, in the worst case, can have a depth of `len(s)`.
# - The `part` list scales linearly with the depth of recursion, holding the current partition being constructed. In the worst case, it could be as large as `len(s)` when the entire string is considered a single palindrome.
# - Therefore, the space complexity is dominated by the recursion stack, which is O(len(s)).

# **Key Points:**

# - Backtracking helps systematically explore all possible partitions of the string.
# - The `ispali` function efficiently checks for palindromes using two pointers.
# - The time complexity is exponential in the worst case, but the actual complexity depends on the number of palindromic substrings.

# **Additional Considerations:**

# - The worst-case time complexity can be high for long strings. If optimization is crucial, consider using dynamic programming approaches that avoid redundant substring checks.
# - For very large strings, the space complexity might be a factor. If memory is a concern, explore alternative algorithms that might have lower space requirements.