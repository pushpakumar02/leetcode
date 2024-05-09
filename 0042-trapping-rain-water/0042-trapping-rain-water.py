class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l]) 
                res += leftMax -  height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r]) 
                res += rightMax -  height[r]
        return res




# Intuition:
# - To find the amount of water that can be trapped between the bars, we need to determine the maximum height of bars on the left and right of each position.
# - We can then calculate the amount of water at each position by taking the minimum of the maximum heights on the left and right, and subtracting the height of the current bar.

# Approach:
# 1. Initialize two pointers, `l` and `r`, at the beginning and end of the list respectively.
# 2. Initialize variables `leftMax` and `rightMax` to store the maximum height of bars encountered from the left and right sides.
# 3. Initialize a variable `res` to store the total trapped water.
# 4. Iterate while `l` is less than `r`:
#    - If `leftMax` is less than `rightMax`:
#      - Move `l` to the right (`l += 1`).
#      - Update `leftMax` as the maximum of `leftMax` and the height at index `l`.
#      - Add the amount of trapped water at position `l` to `res` (`res += leftMax - height[l]`).
#    - Otherwise:
#      - Move `r` to the left (`r -= 1`).
#      - Update `rightMax` as the maximum of `rightMax` and the height at index `r`.
#      - Add the amount of trapped water at position `r` to `res` (`res += rightMax - height[r]`).
# 5. Finally, return `res`, which holds the total amount of trapped water.

# Time Complexity: O(n), where n is the length of the input list. Both pointers traverse the list only once.

# Space Complexity: O(1), because we use only a constant amount of extra space regardless of the input size. We store variables `l`, `r`, `leftMax`, `rightMax`, and `res`.