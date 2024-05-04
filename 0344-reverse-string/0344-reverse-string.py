class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r :
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r -1

        # k = s.reverse()
        
# Intuition and Approach:

# - We're given a list of characters `s`.
# - We want to reverse this list in-place.
# - We use a two-pointer approach:
#   - `l` starts from the beginning of the list.
#   - `r` starts from the end of the list.
# - We swap `s[l]` with `s[r]` until `l` crosses `r`.
# - We move `l` towards the right and `r` towards the left in each iteration.
# - Once `l` crosses `r`, the list is reversed.
# - Since we're modifying the list in-place, no additional space is used.

# Time Complexity: O(n) - where n is the length of the list `s`. We iterate through half of the list.
# Space Complexity: O(1) - We use constant space, as we are modifying the list in-place without using any additional space.