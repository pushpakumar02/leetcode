class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for t in dp:
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False



### Intuition
# The problem is to determine if a given set of numbers can be partitioned into two subsets with equal sums. This is a variation of the subset sum problem, which can be solved using dynamic programming. The goal is to check if there exists a subset of the given numbers that sums up to half of the total sum of all numbers.

# ### Approach
# 1. **Initial Check**: First, check if the sum of all elements is odd. If it is, it is impossible to partition the array into two subsets with equal sums, so return `False`.
# 2. **Target Sum**: Calculate the target sum, which is half of the total sum.
# 3. **Dynamic Programming**:
#    - Use a set `dp` to keep track of all possible sums that can be achieved using the subset of numbers encountered so far.
#    - Initialize `dp` with `0`, indicating that a sum of 0 is always achievable.
#    - Iterate through each number in the input list `nums`.
#    - For each number, create a new set `nextDp` that includes all current sums in `dp` and the sums obtained by adding the current number to each of the existing sums in `dp`.
#    - Update `dp` with `nextDp`.
# 4. **Check Target**: After processing all numbers, check if the target sum is in `dp`. If it is, return `True`; otherwise, return `False`.

# ### Time Complexity
# - **Time**: \(O(n \cdot \text{sum})\), where \(n\) is the length of the input list `nums` and `sum` is the total sum of the elements. This complexity arises because, in the worst case, each number can be added to all elements in the `dp` set.
# - **Space**: \(O(\text{sum})\), for the `dp` set that can store up to `sum` different sums.

# ### Summary
# 1. Check if the total sum is odd; if so, return `False`.
# 2. Use a set to track achievable sums and update it as you iterate through the numbers.
# 3. After processing, check if the target sum (half of the total sum) is in the set of achievable sums and return the appropriate boolean value.