class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxF = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res



### Intuition and Approach

# The problem asks for the length of the longest substring with the same character where we are allowed to replace at most k characters.

# 1. **Initialization**:
#    - Initialize a dictionary `count` to store the count of characters in the current window.
#    - Initialize two pointers `l` and `r` to track the left and right ends of the current window.
#    - Initialize a variable `res` to store the length of the longest substring.
#    - Initialize a variable `maxF` to store the maximum frequency of a character in the current window.

# 2. **Sliding Window Approach**:
#    - Iterate over the characters of the string `s` using the right pointer `r`.
#    - Update the count of `s[r]` in `count`.
#    - Update `maxF` with the maximum count of any character in the current window.
#    - While the length of the current window minus the maximum frequency of a character in that window is greater than `k`, shrink the window from the left (`l`) by one character:
#      - Decrement the count of `s[l]` in `count`.
#      - Increment `l`.
#    - Update `res` with the maximum length of the current window.
   
# 3. **Return**:
#    - Return `res` as the length of the longest substring.

# 4. **Time Complexity**:
#    - The time complexity is O(n), where n is the length of the input string `s`. Both pointers `l` and `r` traverse the string only once.

# 5. **Space Complexity**:
#    - The space complexity is O(1) because the size of the `count` dictionary is constant regardless of the input size. It only stores the counts of characters in the window.