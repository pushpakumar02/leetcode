class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea , height * (i - index)) 
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h *(len(heights) - i)) 
        return maxArea



# Intuition:
# - We are given a list of heights representing the heights of bars in a histogram, and we need to find the largest rectangle area that can be formed.

# Approach:
# - We use a stack to keep track of the indices of bars in ascending order of heights.
# - We iterate through the heights and maintain a stack of tuples `(index, height)`.
# - For each bar at index `i`, we check:
#   - If the stack is not empty and the height of the current bar is less than the height of the bar at the top of the stack:
#     - We pop the top of the stack and calculate the area of the rectangle with the popped bar as the height and the width as `(i - index)`.
#     - We update the `maxArea` with the maximum of the current `maxArea` and the calculated area.
#     - We update the `start` index with the index of the popped bar.
#   - We push the current bar's index and height onto the stack.
# - After iterating through all bars, if there are still bars left in the stack, it means they can form rectangles extending to the end of the histogram.
#   - We iterate through the remaining bars in the stack and calculate their areas, updating `maxArea`.
# - Finally, we return `maxArea`.

# Time Complexity: O(n), where n is the number of bars in the histogram. We iterate through each bar once.

# Space Complexity: O(n), where n is the number of bars in the histogram. The stack can potentially store all bars in the histogram. In the worst case, all bars are in increasing order of heights, so the space complexity is O(n).