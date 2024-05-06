class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        return len(word[-1])



# Intuition and Approach:

# - We're given a string `s` containing words separated by spaces.
# - The task is to find the length of the last word in the string.
# - We can first split the string `s` into words using the `split()` method.
# - The last word will be the last element in the resulting list.
# - We return the length of the last word.

# Time Complexity: O(n) - where n is the length of `s`. The `split()` method takes linear time.

# Space Complexity: O(m) - where m is the maximum length of any word in `s`. The space required by the split words list depends on the length of the longest word.
