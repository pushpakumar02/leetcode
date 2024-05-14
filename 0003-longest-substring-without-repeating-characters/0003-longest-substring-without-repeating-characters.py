class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res


# ### Intuition and Approach

# To find the length of the longest substring without repeating characters in a given string `s`, we can use a sliding window approach with a HashSet to track the characters in the current substring.

# 1. **Initialization**:
#    - Initialize an empty set `charSet` to store unique characters in the current substring.
#    - Initialize two pointers `l` and `r` to track the left and right ends of the current substring.
#    - Initialize a variable `res` to store the length of the longest substring without repeating characters. Set `res` to 0.

# 2. **Sliding Window Approach**:
#    - Iterate over the characters of the string `s` using the right pointer `r`.
#    - For each character `s[r]`:
#      - If `s[r]` is not in `charSet`, add it to `charSet`.
#      - If `s[r]` is in `charSet`, it means the current character is repeating in the current substring.
#        - Increment `l` (the left pointer) until there are no repeating characters in the current substring. Remove the characters at `s[l]` from `charSet` and increment `l`.
#      - Update `res` to be the maximum of the current length of the substring (`r - l + 1`) and the previous `res`.
#    - Return `res` as the length of the longest substring without repeating characters.

# 3. **Time Complexity**:
#    - The time complexity is O(n), where n is the length of the input string `s`. Both pointers `l` and `r` traverse the string only once.

# 4. **Space Complexity**:
#    - The space complexity is O(min(m, n)), where n is the length of the input string `s` and m is the size of the character set (maximum number of unique characters in `s`). In the worst case, the entire string `s` consists of distinct characters, so the space used by `charSet` would be O(n). However, if the character set is limited (e.g., ASCII characters), the space complexity would be O(1).
