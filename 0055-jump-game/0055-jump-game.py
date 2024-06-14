class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

# ### Intuition
# The problem is to determine if you can jump to the last index of the given list `nums`. This can be efficiently solved using a greedy approach by working backwards from the last index. The idea is to check if the current position can reach the "goal" position, which starts as the last index and updates as we iterate backwards.

# ### Approach
# 1. **Initialization**:
#    - Set `goal` to the last index of the array, `len(nums) - 1`.

# 2. **Iterate from the second last index to the first index**:
#    - For each index `i`, check if `i + nums[i]` (the maximum index we can reach from `i`) is greater than or equal to `goal`.
#    - If it is, update `goal` to `i` because now we need to see if we can reach this new `goal`.

# 3. **Result**:
#    - After iterating through the array, if `goal` is 0, it means we can jump to the last index from the first index, so return `True`.
#    - Otherwise, return `False`.

# ### Time and Space Complexities
# - **Time Complexity**: \(O(n)\), where \(n\) is the length of `nums`. We iterate through the array once.
# - **Space Complexity**: \(O(1)\). We use a constant amount of extra space.

# ### Explanation
# - **Initial Setup**: 
#   - `goal` is initially set to the last index of the array.
# - **Iteration**:
#   - Start from the second last index and move backwards to the first index.
#   - For each index `i`, if `i + nums[i]` (the farthest we can jump from index `i`) is greater than or equal to the current `goal`, update `goal` to `i`.
# - **Return**: After the loop, if `goal` is 0, return `True` indicating that we can jump to the last index from the first index. Otherwise, return `False`.