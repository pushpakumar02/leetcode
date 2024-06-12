class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]



### Intuition
# To find the longest common subsequence (LCS) between two strings, we use dynamic programming to systematically compare each character of the two strings and build a table (`dp`) that stores the length of the LCS up to each position in the strings.

# ### Approach
# 1. **Initialization**: Create a 2D list `dp` with dimensions `(len(text1)+1) x (len(text2)+1)`, initialized to 0. `dp[i][j]` will store the length of the LCS of the substrings `text1[i:]` and `text2[j:]`.
# 2. **Filling the DP Table**:
#    - Iterate backward through each character of `text1` and `text2`.
#    - If the characters `text1[i]` and `text2[j]` match, then `dp[i][j] = 1 + dp[i + 1][j + 1]`, because this character is part of the LCS.
#    - If they do not match, then `dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])`, representing the maximum LCS length by either skipping the character in `text1` or `text2`.
# 3. **Result**: The value at `dp[0][0]` will be the length of the LCS of `text1` and `text2`.

# ### Time Complexity
# - **Time**: \(O(m \times n)\), where \(m\) is the length of `text1` and \(n\) is the length of `text2`, because we fill a table of size `m x n`.
# - **Space**: \(O(m \times n)\), for storing the DP table.

# ### Summary
# 1. Create a DP table initialized to 0.
# 2. Iterate backwards through both strings and fill the DP table based on character matches or maximum values from adjacent cells.
# 3. The length of the LCS will be in the top-left cell of the table.
