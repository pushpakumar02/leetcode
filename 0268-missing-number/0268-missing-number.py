class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(res):
            res += (i - nums[i])
        return res




### Intuition and Approach

# To find the missing number in an array of integers ranging from 0 to `n` (with one number missing), we can utilize a mathematical approach that leverages the properties of sums.

# #### Approach:

# 1. **Initial Result Setup**:
#    - Start with `res` initialized to the length of the input list `nums`. This step accounts for the inclusion of the missing number in the range calculation.

# 2. **Sum Difference Calculation**:
#    - Iterate through the indices and the corresponding values in `nums`.
#    - For each index `i` and value `nums[i]`, add the difference `(i - nums[i])` to `res`. This approach effectively balances out the excess or deficit caused by the missing number.

# 3. **Final Result**:
#    - After completing the loop, `res` will hold the missing number due to the cumulative effect of the sum differences.

# ### Time Complexity

# - **Time Complexity**: \(O(n)\)
#   - The algorithm iterates through the list exactly once, making the time complexity linear.

# ### Space Complexity

# - **Space Complexity**: \(O(1)\)
#   - The algorithm uses a constant amount of extra space.

# ### Implementation

# Here's the implementation of the described approach:

# ```python
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = len(nums)
#         for i in range(res):
#             res += (i - nums[i])
#         return res
# ```

# ### Explanation

# 1. **Initialize `res`**:
#    - Set `res` to the length of `nums`. This accounts for the fact that the numbers range from 0 to `n` (inclusive).

# 2. **Iterate Through the List**:
#    - For each index `i` in `nums`:
#      - Adjust `res` by adding the difference between the index `i` and the value `nums[i]`. This helps in neutralizing the effect of the missing number.

# 3. **Return `res`**:
#    - After processing all elements, `res` will contain the value of the missing number.

# ### Example

# Let's walk through an example to illustrate this:

# Consider `nums = [3, 0, 1]`:

# - Initial `res = len(nums) = 3`.
# - Iterating through `nums`:
#   - For `i = 0`, `nums[i] = 3`, so `res += (0 - 3)`, resulting in `res = 0`.
#   - For `i = 1`, `nums[i] = 0`, so `res += (1 - 0)`, resulting in `res = 1`.
#   - For `i = 2`, `nums[i] = 1`, so `res += (2 - 1)`, resulting in `res = 2`.

# The final value of `res` is `2`, which is the missing number in the list.