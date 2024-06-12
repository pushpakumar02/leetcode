class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# ### Intuition
# The problem is to find the length of the longest increasing subsequence (LIS) in a given list of integers. This is a classic dynamic programming problem where we maintain an array to track the length of the LIS ending at each position in the array.

# ### Approach
# 1. **Initialization**: Create an array `dp` of the same length as the input array `nums`, initialized with 1s. Each element in `dp` represents the length of the LIS ending at that position.
# 2. **Dynamic Programming Table Update**:
#    - Iterate through the array with index `i` from 1 to `n-1`.
#    - For each `i`, iterate through all indices `j` from 0 to `i-1`.
#    - If `nums[i]` is greater than `nums[j]`, update `dp[i]` to be the maximum of its current value and `dp[j] + 1`. This step ensures that we are extending the LIS ending at `j` to include `i`.
# 3. **Result**: The length of the longest increasing subsequence will be the maximum value in the `dp` array.

# ### Time Complexity
# - **Time**: \(O(n^2)\), where \(n\) is the length of the input list `nums`. We have a nested loop, where each element `i` is compared with all previous elements `j`.
# - **Space**: \(O(n)\), for the `dp` array of size `n`.

# ### Summary
# 1. Initialize a `dp` array with 1s, where each element represents the length of the LIS ending at that index.
# 2. Use a nested loop to update the `dp` array by comparing each element with all previous elements.
# 3. Return the maximum value in the `dp` array, which represents the length of the longest increasing subsequence.