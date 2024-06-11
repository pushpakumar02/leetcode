class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if( (i + 1) < len(s) and (s[i] =="1" or
             s[i] == "2") and( s[i + 1] in "0123456")):
               dp[i]  +=  dp[i + 2]
        return dp[0] 



### Intuition
# The problem is to count the number of ways to decode a string of digits, where each digit or pair of digits represents a letter (1-26 corresponds to 'A'-'Z'). 

# ### Approach
# 1. **Dynamic Programming (DP)**:
#    - Use a dictionary `dp` to store the number of ways to decode the substring starting at each position `i`.
#    - `dp[i]` represents the number of ways to decode the substring starting from index `i`.
#    - Initialize `dp[len(s)] = 1`, as there is one way to decode an empty substring.

# 2. **Iterate Backwards**:
#    - Iterate through the string from the end to the beginning.
#    - For each position `i`:
#      - If the character at `s[i]` is '0', set `dp[i]` to 0 since '0' cannot be decoded.
#      - Otherwise, set `dp[i]` to `dp[i + 1]` (decoding the current character as a single digit).
#      - Check if the current and next characters form a valid two-digit number (10 to 26). If so, add `dp[i + 2]` to `dp[i]` (decoding the current character and the next character as a pair).

# ### Time Complexity
# - **Time**: \(O(n)\), where \(n\) is the length of the string. This is because we iterate through the string once.

# ### Space Complexity
# - **Space**: \(O(n)\), for the `dp` dictionary that stores the number of ways to decode each substring.

# ### Summary
# 1. Use dynamic programming to iteratively calculate the number of ways to decode the string.
# 2. Iterate through the string from the end to the beginning, updating the `dp` dictionary based on single and double digit decodings.
# 3. The final result is stored in `dp[0]`, representing the number of ways to decode the entire string.