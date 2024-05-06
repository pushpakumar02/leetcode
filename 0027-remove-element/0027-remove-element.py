class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
        return i

# Intuition and Approach:

# - We're given an array `nums` and a value `val`.
# - The task is to remove all occurrences of `val` from `nums` in-place and return the new length of the array.
# - We use a pointer `i` to keep track of the position where the next non-`val` element should be placed.
# - We iterate through each element `n` in `nums`.
# - For each element `n`, if it's not equal to `val`, we copy it to position `i` in `nums` and then increment `i`.
# - After iterating through all elements, `i` will represent the new length of the array with `val` removed.

# Time Complexity: O(n) - where n is the length of `nums`. We iterate through `nums` once.

# Space Complexity: O(1) - We use only a constant amount of extra space regardless of the size of `nums`. We are modifying `nums` in-place.
