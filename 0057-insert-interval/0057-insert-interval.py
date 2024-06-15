class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            
        res.append(newInterval)
        return res



### Intuition

# The problem involves inserting a new interval into a list of non-overlapping intervals sorted by their start time. The task is to merge this new interval with any overlapping intervals and return the modified list of intervals.

# ### Approach

# To solve this, we can iterate through the existing intervals and handle three cases:
# 1. **Non-overlapping to the left**: If the new interval ends before the current interval starts, append the new interval to the result and append all remaining intervals as they are. Return the result immediately since the new interval has been placed.
# 2. **Non-overlapping to the right**: If the new interval starts after the current interval ends, append the current interval to the result.
# 3. **Overlapping**: If the new interval overlaps with the current interval, merge them by updating the new interval's start to the minimum of both starts and the new interval's end to the maximum of both ends.

# Finally, if the new interval has not been added yet (e.g., it overlaps with the last interval or all intervals are non-overlapping to the right), append it to the result.

# ### Time and Space Complexities

# - **Time Complexity**: \(O(N)\), where \(N\) is the number of intervals. We iterate through the list once.
# - **Space Complexity**: \(O(N)\), where \(N\) is the number of intervals. In the worst case, we store all original intervals plus the new interval.

# ### Implementation

# ```python
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         res = []

#         for i in range(len(intervals)):
#             if newInterval[1] < intervals[i][0]:
#                 res.append(newInterval)
#                 return res + intervals[i:]
#             elif newInterval[0] > intervals[i][1]:
#                 res.append(intervals[i])
#             else:
#                 newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            
#         res.append(newInterval)
#         return res
# ```

# ### Explanation

# 1. **Initialization**: Start with an empty result list `res`.
# 2. **Iterate through intervals**:
#    - **Non-overlapping to the left**: If the new interval ends before the current interval starts, append the new interval and all remaining intervals, then return the result.
#    - **Non-overlapping to the right**: If the new interval starts after the current interval ends, append the current interval to the result.
#    - **Overlapping**: If the new interval overlaps with the current interval, merge them by updating the new interval's start to the minimum start and its end to the maximum end.
# 3. **Final Step**: If the new interval has not been added by the end of the loop, append it to the result.

# This method ensures that the new interval is correctly placed and merged with any overlapping intervals, maintaining the sorted order of the intervals.