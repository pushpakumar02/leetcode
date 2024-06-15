class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nlogn)
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for first, end in intervals[1:]:
            lastEnd = output[-1][1]

            if first <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([first, end])

        return output


### Intuition

# The problem involves merging a list of overlapping intervals. The goal is to combine all overlapping intervals into a single interval and return the modified list of intervals.

# ### Approach

# To solve this, we can follow these steps:
# 1. **Sort the Intervals**: First, sort the intervals based on their start times. This helps in simplifying the merge process as we can merge intervals in a single pass.
# 2. **Iterate and Merge**: Iterate through the sorted intervals and merge them as follows:
#    - If the current interval overlaps with the last interval in the result list (i.e., the start of the current interval is less than or equal to the end of the last interval in the result list), merge them by updating the end of the last interval in the result list.
#    - If the current interval does not overlap, simply append it to the result list.

# ### Time and Space Complexities

# - **Time Complexity**: \(O(N \log N)\), where \(N\) is the number of intervals. The sorting step dominates the time complexity.
# - **Space Complexity**: \(O(N)\), where \(N\) is the number of intervals. In the worst case, we store all intervals in the output list.

# ### Implementation

# ```python
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # Sort intervals based on the start times
#         intervals.sort(key=lambda i: i[0])
        
#         output = [intervals[0]]  # Initialize output with the first interval
        
#         for start, end in intervals[1:]:
#             lastEnd = output[-1][1]  # Get the end of the last interval in the output list

#             if start <= lastEnd:
#                 # If the current interval overlaps with the last one in the output, merge them
#                 output[-1][1] = max(lastEnd, end)
#             else:
#                 # If there is no overlap, add the current interval to the output list
#                 output.append([start, end])
        
#         return output
# ```

# ### Explanation

# 1. **Sorting**: The intervals are first sorted based on their start times. This ensures that any overlapping intervals are adjacent in the sorted list.
# 2. **Initialize Output**: Start with the first interval in the output list.
# 3. **Iterate and Merge**:
#    - For each interval in the sorted list (starting from the second interval):
#      - Check if it overlaps with the last interval in the output list.
#      - If it does, merge by updating the end of the last interval in the output list.
#      - If it does not, append the interval to the output list.

# By following this approach, we ensure that all overlapping intervals are merged correctly, and the resulting list of intervals is returned in the correct order.
