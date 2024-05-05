class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
                

# Intuition and Approach:

# - We're given a list of integers `nums`.
# - The task is to determine whether there are any duplicate elements in `nums`.
# - We use a set `hashset` to keep track of unique elements encountered so far.
# - We iterate through each element `i` in `nums`.
# - For each element `i`, we check if it exists in `hashset`.
#   - If it does, it means `i` is a duplicate, so we return `True`.
#   - If not, we add `i` to `hashset`.
# - If we complete the loop without finding any duplicates, we return `False`.

# Time Complexity: O(n) - where n is the length of `nums`. We iterate through `nums` once.

# Space Complexity: O(n) - where n is the length of `nums`. In the worst case, all elements of `nums` are unique, so the space used by `hashset` will be equal to the size of `nums`.
