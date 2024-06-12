class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w: 
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]  

### Intuition
# The problem is to determine if a given string can be segmented into a sequence of one or more dictionary words. This is a classic dynamic programming problem where we use a boolean array to track whether a substring of the given string can be segmented into words from the dictionary.

# ### Approach
# 1. **Initialization**: Create a boolean array `dp` of size `len(s) + 1`, initialized to `False`. The last element `dp[-1]` is set to `True`, indicating that an empty substring can be considered as successfully segmented.
# 2. **Dynamic Programming Table Update**:
#    - Iterate over the string `s` from the end to the beginning.
#    - For each position `i`, check all words in the dictionary `wordDict`:
#      - If the word matches the substring starting at `i` and its length fits within the remaining part of the string, update `dp[i]` to `dp[i + len(w)]`.
#      - If `dp[i]` becomes `True`, break out of the loop to avoid unnecessary checks.
# 3. **Result**: The value `dp[0]` will indicate whether the entire string `s` can be segmented into words from the dictionary.

# ### Time Complexity
# - **Time**: \(O(n \cdot m)\), where \(n\) is the length of the string `s` and \(m\) is the number of words in the dictionary. In the worst case, for each character in `s`, we check every word in `wordDict`.
# - **Space**: \(O(n)\), for the `dp` array of size `len(s) + 1`.

# ### Summary
# 1. Create a `dp` array to keep track of whether substrings of `s` can be segmented using words from `wordDict`.
# 2. Iterate from the end of the string to the beginning, updating the `dp` array based on matches found in the dictionary.
# 3. Return `dp[0]` to check if the entire string can be segmented.