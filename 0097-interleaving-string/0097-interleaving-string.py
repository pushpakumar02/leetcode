class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]


### Intuition
# To determine if `s3` is formed by interleaving `s1` and `s2`, we can use dynamic programming. The key idea is to check if each character in `s3` can be matched by either `s1` or `s2` while maintaining the order of characters in `s1` and `s2`.

# ### Approach
# 1. **Check Lengths**: If the sum of the lengths of `s1` and `s2` is not equal to the length of `s3`, return `False` because it's impossible for `s3` to be an interleaving of `s1` and `s2`.

# 2. **Dynamic Programming Table**: Create a 2D DP table where `dp[i][j]` represents whether `s3` up to `i + j` can be formed by interleaving `s1` up to `i` and `s2` up to `j`.

# 3. **Initialization**: 
#    - Initialize the DP table with `False`.
#    - Set `dp[len(s1)][len(s2)]` to `True` because an empty `s1` and `s2` can form an empty `s3`.

# 4. **Fill the DP Table**:
#    - Iterate from the end of `s1` and `s2` to the start.
#    - For each position `(i, j)`, check two conditions:
#      - If the current character in `s1` matches the corresponding character in `s3` and `dp[i+1][j]` is `True`, set `dp[i][j]` to `True`.
#      - If the current character in `s2` matches the corresponding character in `s3` and `dp[i][j+1]` is `True`, set `dp[i][j]` to `True`.

# 5. **Result**: Return the value of `dp[0][0]` which indicates whether the entire `s3` can be formed by interleaving `s1` and `s2`.

# ### Time and Space Complexities
# - **Time Complexity**: \(O(n \cdot m)\) where \(n\) and \(m\) are the lengths of `s1` and `s2` respectively.
# - **Space Complexity**: \(O(n \cdot m)\) due to the DP table.

