class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l +=1
            while r > l and not self.alphaNum(s[r]):
                r -=1
            if  s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True

    def alphaNum(self, n):
        return (ord('A') <= ord(n) <= ord('Z') or 
                ord('a') <= ord(n) <= ord('z') or 
                ord('0') <= ord(n) <= ord('9'))      

# Intuition and Approach:

# - The task is to determine whether a given string `s` is a palindrome, considering only alphanumeric characters and ignoring cases.
# - We use a two-pointer approach, `l` starting from the beginning of the string and `r` starting from the end.
# - While `l` is less than `r`, we move both pointers towards each other.
# - At each step:
#   - We move `l` to the right until it points to an alphanumeric character, using the `alphaNum` helper function.
#   - We move `r` to the left until it points to an alphanumeric character, using the `alphaNum` helper function.
#   - We check if the characters at `l` and `r` (converted to lowercase) are equal.
#     - If they are not equal, `s` is not a palindrome, and we return `False`.
#   - We move `l` to the right and `r` to the left to continue the comparison.
# - If we complete the loop without finding any mismatch, `s` is a palindrome, and we return `True`.

# Time Complexity: O(n) - where n is the length of the input string `s`. We iterate through `s` once with the two-pointer approach.

# Space Complexity: O(1) - We use only a constant amount of extra space regardless of the size of `s`.
