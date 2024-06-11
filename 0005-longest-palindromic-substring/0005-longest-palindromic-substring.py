class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1: r]  

        res = ""
        for i in range(len(s)):
            sub1 = expand(i, i)
            if len(sub1) > len(res):
                res = sub1
            sub2 = expand(i, i + 1)
            if len(sub2) > len(res):
                res = sub2
        return res


# https://www.youtube.com/watch?v=E-tmN1OM9aA

### Intuition
# The problem is to find the longest palindromic substring in a given string `s`. A palindrome reads the same forwards and backwards.

# ### Approach
# The approach used here involves expanding around potential centers of the palindrome. Each character and each pair of consecutive characters in the string can serve as the center of a potential palindrome. 

# ### Detailed Steps
# 1. **Expand Around Center**:
#    - Define a helper function `expand(l, r)` that expands around the center defined by indices `l` and `r` as long as the characters at these indices are the same and the indices are within bounds.
#    - This function returns the longest palindromic substring centered at `l` and `r`.

# 2. **Check All Possible Centers**:
#    - Iterate through each character in the string.
#    - For each character, consider it as a single-character center and use the `expand` function to find the longest odd-length palindrome.
#    - Also, consider each pair of consecutive characters as the center for even-length palindromes and use the `expand` function to find the longest even-length palindrome.

# 3. **Update Result**:
#    - Keep track of the longest palindrome found by comparing lengths of the substrings obtained from each center.

# ### Time Complexity
# - **Time**: \(O(n^2)\), where \(n\) is the length of the string. This is because for each character (or pair of characters) in the string, we expand around the center which takes linear time.

# ### Space Complexity
# - **Space**: \(O(1)\), only a constant amount of extra space is used for the variables.

# ### Summary
# 1. Iterate through the string, treating each character and each pair of consecutive characters as potential centers of a palindrome.
# 2. Use a helper function to expand around each center and find the longest palindrome.
# 3. Track and return the longest palindrome found.
