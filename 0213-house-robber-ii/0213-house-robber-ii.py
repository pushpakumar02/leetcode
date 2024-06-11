class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

      
    def helper(self, nums):
        rob1, rob2 = 0, 0 
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

### Intuition
# This problem is a variant of the "House Robber" problem, with the added complexity that the houses are arranged in a circle. This means the first and last houses are adjacent and cannot be robbed together.

# ### Approach
# To solve this problem, we can break it down into two simpler "House Robber" problems:
# 1. Rob houses from the second house to the last house.
# 2. Rob houses from the first house to the second-to-last house.

# The solution to the original problem will be the maximum value obtained from the above two scenarios.

# ### Detailed Steps
# 1. **Base Case**: If there is only one house, return its value.
# 2. **Helper Function**: Implement a helper function to calculate the maximum amount of money that can be robbed from a linear list of houses.
# 3. **Divide and Conquer**:
#    - Use the helper function to find the maximum amount of money that can be robbed from the subarray excluding the first house.
#    - Use the helper function to find the maximum amount of money that can be robbed from the subarray excluding the last house.
# 4. **Result**: The final answer is the maximum value between the two scenarios.

# ### Time Complexity
# - **Time**: \(O(n)\), where \(n\) is the number of houses. We iterate through the list of houses twice, once for each scenario.
  
# ### Space Complexity
# - **Space**: \(O(1)\). Only a constant amount of extra space is used for the variables.

