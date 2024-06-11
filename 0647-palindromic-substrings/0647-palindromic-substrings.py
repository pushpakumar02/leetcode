class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPoli(s, i, i)
            res += self.countPoli(s, i, i + 1)
        return res

    def countPoli(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res


### Intuition
# The problem is to count the number of palindromic substrings in a given string `s`. A substring is palindromic if it reads the same forwards and backwards.

# ### Approach
# The approach used here involves expanding around potential centers of the palindromic substrings. Each character and each pair of consecutive characters in the string can serve as the center of a potential palindrome.

# ### Detailed Steps
# 1. **Expand Around Center**:
#    - Define a helper function `countPoli(s, l, r)` that expands around the center defined by indices `l` and `r` as long as the characters at these indices are the same and the indices are within bounds.
#    - This function returns the count of palindromic substrings centered at `l` and `r`.

# 2. **Check All Possible Centers**:
#    - Iterate through each character in the string.
#    - For each character, consider it as a single-character center and use the `countPoli` function to count the palindromic substrings centered there.
#    - Also, consider each pair of consecutive characters as the center for even-length palindromes and use the `countPoli` function to count the palindromic substrings centered there.

# 3. **Sum the Results**:
#    - Accumulate the counts of palindromic substrings from each center to get the total number of palindromic substrings in the string.

# ### Time Complexity
# - **Time**: \(O(n^2)\), where \(n\) is the length of the string. This is because for each character (or pair of characters) in the string, we expand around the center which takes linear time.

# ### Space Complexity
# - **Space**: \(O(1)\), only a constant amount of extra space is used for the variables.

# ### Summary
# 1. Iterate through the string, treating each character and each pair of consecutive characters as potential centers of a palindrome.
# 2. Use a helper function to expand around each center and count the palindromic substrings.
# 3. Sum the counts from all centers to get the total number of palindromic substrings.
