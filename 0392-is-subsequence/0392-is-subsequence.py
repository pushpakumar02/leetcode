class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


# Intuition and Approach:

# - We're given two strings, `s` and `t`.
# - We want to determine if `s` is a subsequence of `t`, meaning that the characters of `s` appear in the same order within `t`, but not necessarily consecutively.
# - We use two pointers, `i` and `j`, to traverse `s` and `t` respectively.
# - We start by initializing both pointers to 0.
# - We iterate through `s` and `t` using the pointers until either `s` is exhausted or `t` is exhausted.
# - At each step:
#   - If `s[i]` matches `t[j]`, we increment `i` to move to the next character in `s`.
#   - Regardless, we always increment `j` to move to the next character in `t`.
# - If we successfully traverse the entire `s`, `i` will be equal to the length of `s`, and we return `True`.
# - If `s` is not fully traversed, we return `False`.

# Time Complexity: O(n) - where n is the length of `t`. We iterate through `t` once.

# Space Complexity: O(1) - We use only a constant amount of extra space for variables (`i` and `j`) regardless of the size of the inputs `s` and `t`.
