class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l , r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
                
        return dfs(1, len(nums) - 2)



### Intuition and Approach

# The problem "Burst Balloons" can be approached using dynamic programming. The goal is to find the maximum number of coins you can collect by bursting balloons wisely. Each time a balloon `i` is burst, it contributes to the total number of coins based on the product of the balloon values on its left and right (i.e., `nums[left] * nums[i] * nums[right]`). To achieve this, we need to consider all possible ways to burst the balloons in the interval and select the one that maximizes the total coins.

# ### Detailed Steps

# 1. **Modify the Input Array**:
#    - Add `1` at the beginning and the end of the `nums` array to handle edge cases easily. This allows us to always have a left and right balloon when any balloon is burst.

# 2. **Dynamic Programming with Memoization**:
#    - Use a dictionary `dp` to store the maximum coins that can be collected in the subarray `nums[l:r+1]`.
#    - Define a recursive function `dfs(l, r)` that computes the maximum coins obtainable by bursting all balloons in the interval `[l, r]`.

# 3. **Recursive Function Logic**:
#    - Base Case: If `l > r`, return `0` as no balloons are left to burst.
#    - If the result for the interval `[l, r]` is already computed, return it from the `dp` dictionary.
#    - Initialize `dp[(l, r)]` to `0`.
#    - Iterate through all possible balloons to burst in the interval `[l, r]`. For each balloon `i`:
#      - Calculate the coins obtained by bursting balloon `i` (i.e., `nums[l-1] * nums[i] * nums[r+1]`).
#      - Add the coins obtained by recursively bursting the balloons in the left and right subintervals (`dfs(l, i-1)` and `dfs(i+1, r)`).
#      - Update `dp[(l, r)]` with the maximum coins obtained.
#    - Return the value of `dp[(l, r)]`.

# ### Time and Space Complexities

# - **Time Complexity**: \(O(n^3)\), where \(n\) is the length of the input array `nums`. This is because there are \(O(n^2)\) subproblems and each subproblem requires \(O(n)\) time to solve.
# - **Space Complexity**: \(O(n^2)\) for storing the results of subproblems in the `dp` dictionary.

# Here is the complete code:

# ```python
# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         nums = [1] + nums + [1]
#         dp = {}

#         def dfs(l, r):
#             if l > r:
#                 return 0
#             if (l, r) in dp:
#                 return dp[(l, r)]
            
#             dp[(l, r)] = 0
#             for i in range(l, r + 1):
#                 coins = nums[l - 1] * nums[i] * nums[r + 1]
#                 coins += dfs(l, i - 1) + dfs(i + 1, r)
#                 dp[(l, r)] = max(dp[(l, r)], coins)
#             return dp[(l, r)]
                
#         return dfs(1, len(nums) - 2)
# ```

# This code leverages dynamic programming with memoization to efficiently compute the maximum coins that can be collected by bursting balloons in an optimal order.
        
