class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])           
            l = r + 1
            r = farthest
            res += 1
        return res


### Intuition
# The problem is to determine the minimum number of jumps required to reach the last index in the array `nums`. The greedy approach works well for this problem by making sure that at each step, you jump to the farthest possible position.

# ### Approach
# 1. **Initialize Variables**:
#    - `l` and `r` represent the current range of indices that can be reached with the current number of jumps.
#    - `res` counts the number of jumps taken.

# 2. **Iterate Until the Right Boundary `r` Reaches the Last Index**:
#    - While `r` is less than the last index, we perform the following:
#      - Calculate the farthest index that can be reached from the current range `[l, r]`.
#      - Update `l` to `r + 1` to start the next range from the position right after the current range.
#      - Update `r` to `farthest` to extend the range to the farthest reachable index.
#      - Increment the jump counter `res`.

# 3. **Return Result**:
#    - The number of jumps (`res`) will be the minimum number of jumps needed to reach the last index.

# ### Time and Space Complexities
# - **Time Complexity**: \(O(n)\), where \(n\) is the length of `nums`. We iterate through the array once in a while loop and in the inner for loop, we process each element at most once.
# - **Space Complexity**: \(O(1)\). We use a constant amount of extra space.



# ### Explanation
# - **Initial Setup**:
#   - `l` and `r` are set to 0, meaning we start from the first index.
#   - `res` is initialized to 0 to count the jumps.

# - **While Loop**:
#   - Continue the loop until `r` (the right boundary of the current range) reaches or exceeds the last index.
#   - Calculate the farthest index that can be reached from the current range `[l, r]`.
#   - Update `l` to `r + 1` to start the next range from the next index.
#   - Update `r` to `farthest` to extend the range to the farthest reachable index.
#   - Increment the jump counter `res`.

# - **Return**:
#   - Return the jump count `res` which represents the minimum number of jumps required to reach the last index.