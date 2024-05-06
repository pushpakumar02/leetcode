class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


# Intuition and Approach:

# - The task is to find the length of the longest consecutive sequence of numbers in the given list `nums`.
# - We can first convert `nums` into a set `numSet`, which allows for constant time lookup.
# - We initialize a variable `longest` to keep track of the length of the longest consecutive sequence found.
# - We iterate through each number `n` in `nums`.
# - For each number `n`, if `n-1` is not in `numSet`, it means `n` is the start of a new consecutive sequence.
#   - We initialize a variable `length` to 0 and increment it while `n + length` is in `numSet`.
#   - We update `longest` to be the maximum of `length` and `longest`.
# - Finally, we return the value of `longest`, which represents the length of the longest consecutive sequence found.

# Time Complexity: O(n) - where n is the number of elements in `nums`. The set `numSet` allows for constant time lookup, and we iterate through `nums` once.

# Space Complexity: O(n) - where n is the number of elements in `nums`. The set `numSet` requires additional space proportional to the size of `nums`. Additionally, we use a constant amount of extra space for variables.
