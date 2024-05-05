class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or str[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res 


# Intuition and Approach:

# - We're given a list of strings `strs`.
# - The task is to find the longest common prefix among all strings in `strs`.
# - We start by initializing an empty string `res` to store the longest common prefix.
# - We iterate through the characters of the first string in `strs`.
# - For each character at index `i`:
#   - We iterate through all strings in `strs`.
#   - If the current string `s` is shorter than `strs[0]` or if the character at index `i` of `s` is not equal to the character at index `i` of `strs[0]`, we return the current value of `res`, as we've found the longest common prefix.
#   - Otherwise, we append the character at index `i` of `strs[0]` to `res`.
# - If we complete the loop without finding any mismatch, the entire first string is the common prefix, so we return `res`.

# Time Complexity: O(n * m), where n is the number of strings in `strs` and m is the length of the shortest string in `strs`. In the worst case, we iterate through all characters of the shortest string in `strs`.

# Space Complexity: O(m), where m is the length of the shortest string in `strs`. The space used is for the `res` variable.
