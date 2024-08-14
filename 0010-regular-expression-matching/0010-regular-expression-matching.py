class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or ( 
                    match and dfs(i + 1, j))

                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False
        return dfs(0, 0)



### Intuition and Approach

# The problem "Regular Expression Matching" asks if a given string `s` matches a pattern `p`, where the pattern `p` may include:
# - `.` which matches any single character.
# - `*` which matches zero or more of the preceding element.

# This is a classic dynamic programming problem. The goal is to determine whether the string `s` can be fully matched with the pattern `p` by exploring all possible matching paths and storing the results to avoid redundant computations.

# ### Detailed Steps

# 1. **Recursive Function with Memoization**:
#    - Use a recursive function `dfs(i, j)` that checks whether the substring `s[i:]` matches the pattern `p[j:]`.
#    - Use a dictionary `cache` to store the results of subproblems `(i, j)` to avoid recalculating them.

# 2. **Base Cases**:
#    - If both `i` and `j` have reached the end of their respective strings (`s` and `p`), return `True` because both the string and the pattern have been fully matched.
#    - If only `j` has reached the end of `p` but `i` hasn't reached the end of `s`, return `False` because the pattern is exhausted but the string is not.

# 3. **Matching Logic**:
#    - **Direct Match or `.`**: Check if the current characters `s[i]` and `p[j]` match (they are equal or `p[j]` is `.`).
#    - **Handling `*`**: If the next character in the pattern (`p[j+1]`) is `*`, we have two options:
#      1. Skip the current pattern element and `*` (i.e., `dfs(i, j+2)`).
#      2. Use the current pattern element and `*` to match one or more characters in `s` (i.e., `dfs(i+1, j)` if there is a match).
#    - If the pattern doesn't involve a `*`, simply check if the current characters match and proceed to the next characters (`dfs(i+1, j+1)`).

# 4. **Store and Return Results**:
#    - Store the result of each subproblem `(i, j)` in the `cache` and return it.

# ### Time and Space Complexities

# - **Time Complexity**: \(O(m \times n)\), where \(m\) is the length of `s` and \(n\) is the length of `p`. This is because each subproblem is computed only once and there are at most \(m \times n\) unique subproblems.
# - **Space Complexity**: \(O(m \times n)\) for storing the results of the subproblems in the `cache`.

# Here is the complete code:

# ```python
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         cache = {}

#         def dfs(i, j):
#             if (i, j) in cache:
#                 return cache[(i, j)]
#             if i >= len(s) and j >= len(p):
#                 return True
#             if j >= len(p):
#                 return False
            
#             match = i < len(s) and (s[i] == p[j] or p[j] == ".")
#             if (j + 1) < len(p) and p[j + 1] == "*":
#                 cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
#                 return cache[(i, j)]
            
#             if match:
#                 cache[(i, j)] = dfs(i + 1, j + 1)
#                 return cache[(i, j)]
                
#             cache[(i, j)] = False
#             return False
        
#         return dfs(0, 0)
# ```

# This solution efficiently matches the string `s` against the pattern `p` using dynamic programming and memoization, ensuring that each subproblem is solved only once.
