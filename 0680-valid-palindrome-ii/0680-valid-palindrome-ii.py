class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1 : r+1], s[l: r] 
                return (skipL == skipL[::-1] or skipR == skipR[::-1] ) 
            l, r = l +1, r - 1
        return True


# Intuition and Approach:

# - We're using a two-pointer approach, where `l` starts from the beginning of the string and `r` starts from the end.
# - We iterate through the string until `l` crosses `r`.
# - At each step, we check if `s[l]` and `s[r]` are equal. If they are not:
#   - We create two substrings, `skipL` and `skipR`, where we skip one character from either the left or the right pointer.
#   - We check if either of these substrings, after skipping a character, forms a palindrome. We do this by comparing them to their reversed counterparts.
#   - If either `skipL` or `skipR` is a palindrome, we return `True`, indicating that the string can be a palindrome by removing at most one character.
# - If `s[l]` and `s[r]` are equal, we move the pointers towards each other.
# - If we complete the loop without finding any mismatch, it means the string is a palindrome, and we return `True`.
# - If we find a mismatch and none of the skipped substrings form a palindrome, we return `False`.

# Time Complexity: O(n) - We traverse the string once.
# Space Complexity: O(n) - We create two substrings with a maximum length of n.