class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

### Intuition
# The problem of determining the maximum amount of money you can rob from a series of houses without robbing two consecutive houses can be efficiently solved using a dynamic programming approach.

# ### Approach
# - **Dynamic Programming**: Utilize two variables to keep track of the maximum amount of money robbed up to the current house, without using extra space for an array.
#   - `rob1`: Represents the maximum amount robbed up to the house two steps before the current house.
#   - `rob2`: Represents the maximum amount robbed up to the previous house.
#   - For each house, calculate the maximum amount of money that can be robbed by either choosing to rob the current house (adding the current house's money to `rob1`) or not robbing it (taking `rob2`).

# ### Time Complexity
# - **Time**: \(O(n)\). We iterate through the list of houses once.

# ### Space Complexity
# - **Space**: \(O(1)\). Only a constant amount of extra space is used to store intermediate results (`rob1` and `rob2`).

# ### Implementation
# - **Initialization**: Set `rob1` and `rob2` to 0.
# - **Iteration**: For each house, update `rob1` and `rob2` based on the maximum money that can be robbed considering the current house.
# - **Result**: The value in `rob2` after processing all houses will be the maximum money that can be robbed.