class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res) 


# Intuition and Approach:

# - We have two input strings, `word1` and `word2`.
# - We initialize two pointers, `i` and `j`, to track the current index of `word1` and `word2` respectively.
# - We initialize an empty list `res` to store the merged characters.
# - We iterate through both `word1` and `word2` simultaneously using the pointers `i` and `j`.
# - At each step, we append the character at the current index of `word1` to `res`, followed by the character at the current index of `word2`.
# - We increment `i` and `j` after appending characters to move to the next index.
# - Once we reach the end of either `word1` or `word2`, we append the remaining substring of the other word (if any) to `res`.
# - Finally, we join all the characters in `res` to form the merged string and return it.

# Time Complexity: O(n) - where n is the maximum length of `word1` or `word2`. We iterate through both strings once.
# Space Complexity: O(n) - We create a list `res` to store the merged characters, which can be at most of length `2n`.
