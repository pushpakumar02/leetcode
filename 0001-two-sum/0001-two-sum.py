class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val:index

        for i,n in enumerate (nums):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n]=i
        return


# Intuition and Approach:
        
# - We're given an array of integers `nums` and a target integer.
# - The task is to find two numbers in `nums` that add up to the target.
# - We use a hashmap (dictionary in Python) `prevMap` to store the indices of previously encountered numbers.
# - We iterate through each number in `nums` along with its index.
# - For each number `n`, we calculate the difference `diff` between the target and `n`.
# - If `diff` exists in `prevMap`, it means we've found the complement for `n`, and we return the indices of `diff` and `n`.
# - Otherwise, we store `n` in `prevMap` along with its index.
# - If no solution is found after iterating through `nums`, we return an empty list.

# Time Complexity: O(n) - where n is the length of `nums`. We iterate through `nums` once.

# Space Complexity: O(n) - where n is the length of `nums`. In the worst case, `prevMap` contains all elements of `nums`.
