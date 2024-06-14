class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

### Intuition
# The problem of finding the maximum subarray sum can be efficiently solved using Kadane's algorithm. This algorithm keeps track of the current subarray sum and updates the maximum subarray sum seen so far.

# ### Approach
# 1. **Initialization**:
#    - Initialize `maxSub` with the first element of `nums` since the maximum subarray sum must start with at least one element.
#    - Initialize `curSum` to 0, which will be used to keep track of the current subarray sum.

# 2. **Iterate through the array**:
#    - For each element in `nums`, if `curSum` is less than 0, reset `curSum` to 0. This is because a negative sum would reduce the potential maximum sum of any new subarray starting from the current element.
#    - Add the current element to `curSum`.
#    - Update `maxSub` with the maximum value between `maxSub` and `curSum`.

# 3. **Result**:
#    - After iterating through the entire array, `maxSub` will contain the maximum subarray sum.

# ### Time and Space Complexities
# - **Time Complexity**: \(O(n)\), where \(n\) is the length of `nums`. We iterate through the array once.
# - **Space Complexity**: \(O(1)\). We use a constant amount of extra space.

# ### Explanation
# - **Initial Setup**: 
#   - `maxSub` is set to `nums[0]` to handle cases where the array contains all negative numbers.
#   - `curSum` starts at 0.
# - **Iteration**:
#   - If `curSum` is negative, reset it to 0 before adding the current element `n`.
#   - Update `curSum` by adding `n`.
#   - Update `maxSub` if `curSum` is greater than the current `maxSub`.
# - **Return**: Finally, return `maxSub` which holds the maximum subarray sum.