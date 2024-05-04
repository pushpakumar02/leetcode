class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
        j = 0    
        while stack:
            s[j] = stack.pop()
            j += 1


# Intuition and Approach:

# - The given code reverses the list `s` in-place.
# - The first approach uses a stack to reverse the list:
#   - It iterates through each character of `s` and pushes them onto a stack.
#   - Then, it iterates through `s` again, popping characters from the stack and placing them back into `s`.
#   - This effectively reverses the list.
# - The second approach is a more efficient in-place reversal:
#   - It initializes two pointers, `l` and `r`, where `l` starts from the beginning of the list and `r` starts from the end.
#   - It swaps `s[l]` with `s[r]` until `l` crosses `r`.
#   - This in-place swapping reverses the list.
# - Both approaches modify `s` in-place, fulfilling the requirement of the problem.

# Time Complexity:
# - For the stack approach: O(n) - where n is the length of the list `s`. The loop to push elements into the stack and the loop to pop elements from the stack both take O(n) time.
# - For the two-pointer approach: O(n/2) ≈ O(n) - It iterates through half of the list.

# Space Complexity:
# - For the stack approach: O(n) - It uses a stack of size proportional to the length of the list `s`.
# - For the two-pointer approach: O(1) - It uses only a constant amount of extra space, as it doesn't create any new data structures.