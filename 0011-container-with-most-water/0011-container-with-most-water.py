class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area =   (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
              


# Intuition:
# - The area of a rectangle formed by two lines from the histogram is determined by the width (the distance between the lines) and the height (the minimum height of the two lines).

# Approach:
# - We use a two-pointer approach to explore all possible combinations of lines.
# - We initialize two pointers, `l` and `r`, at the beginning and end of the list respectively.
# - While `l` is less than `r`, we calculate the area formed by the lines at indices `l` and `r`.
#   - The width of the rectangle is `(r - l)`.
#   - The height of the rectangle is the minimum height of the two lines, `min(height[l], height[r])`.
#   - So, the area is `(r - l) * min(height[l], height[r])`.
# - We update the maximum area seen so far.
# - We move the pointers inward:
#   - If `height[l]` is less than `height[r]`, we move `l` to the right.
#   - Otherwise, we move `r` to the left.
# - We continue this process until `l` becomes greater than or equal to `r`.
# - Finally, we return the maximum area.

# Time Complexity: O(n), where n is the number of elements in the list. We traverse the list once using two pointers.

# Space Complexity: O(1), as we use only a constant amount of extra space regardless of the input size. 

             