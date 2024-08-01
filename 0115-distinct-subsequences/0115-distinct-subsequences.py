class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
        
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i, j)]
        return dfs(0, 0)



### Intuition and Approach

# The problem is to count the number of distinct subsequences of string `s` which equals string `t`. This problem can be approached using a recursive strategy with memoization (top-down dynamic programming).

# ### Detailed Steps

# 1. **Recursive Function Definition**:
#    - Define a recursive function `dfs(i, j)` which returns the number of distinct subsequences of the substring `s[i:]` that equals the substring `t[j:]`.

# 2. **Base Cases**:
#    - If `j` reaches the length of `t`, it means we've found a valid subsequence, so return `1`.
#    - If `i` reaches the length of `s` but `j` has not reached the length of `t`, it means `t` cannot be formed from the remaining characters of `s`, so return `0`.

# 3. **Memoization**:
#    - Use a dictionary `cache` to store the results of already computed states to avoid redundant calculations.

# 4. **Recursive Cases**:
#    - If the characters `s[i]` and `t[j]` match, we have two options:
#      - Include `s[i]` in the subsequence, move to the next characters in both strings (`dfs(i + 1, j + 1)`).
#      - Exclude `s[i]` and move to the next character in `s` while keeping the position in `t` (`dfs(i + 1, j)`).
#    - If the characters do not match, the only option is to exclude `s[i]` and move to the next character in `s` (`dfs(i + 1, j)`).

# 5. **Return the Result**:
#    - Start the recursion from the beginning of both strings (`dfs(0, 0)`) and return the result.

# ### Time and Space Complexities

# - **Time Complexity**: \(O(M \times N)\), where \(M\) is the length of `s` and \(N\) is the length of `t`. Each state `(i, j)` is computed once and stored in the cache.
# - **Space Complexity**: \(O(M \times N)\) for the cache used to store intermediate results.



# ```python
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         cache = {}

#         def dfs(i, j):
#             if j == len(t):
#                 return 1
#             if i == len(s):
#                 return 0
#             if (i, j) in cache:
#                 return cache[(i, j)]
        
#             if s[i] == t[j]:
#                 cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
#             else:
#                 cache[(i, j)] = dfs(i + 1, j)
#             return cache[(i, j)]
        
#         return dfs(0, 0)
# ```

# This solution uses a top-down dynamic programming approach with memoization to efficiently count the number of distinct subsequences of `s` that match `t`.