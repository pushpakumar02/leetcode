class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1] 
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res 

### Intuition

# The problem of erasing the minimum number of intervals to make the rest non-overlapping can be approached using a greedy algorithm. The key idea is to always keep the interval with the earliest end time to maximize the chances of accommodating more intervals without overlap.

# ### Approach

# 1. **Sort Intervals**: Sort the intervals based on their start times. This helps to consider each interval in the order they appear on the timeline.
# 2. **Initialize Variables**: Use a variable `prevEnd` to track the end time of the last added interval in the non-overlapping set. Initialize it to the end of the first interval. Also, use a counter `res` to count the number of intervals that need to be removed.
# 3. **Iterate Through Intervals**:
#    - For each interval, check if it overlaps with the last interval in the non-overlapping set (`prevEnd`).
#    - If it does not overlap, update `prevEnd` to the end of the current interval.
#    - If it overlaps, increment the counter `res` and update `prevEnd` to the minimum of the current `prevEnd` and the end of the current interval to ensure the interval with the earliest end time is chosen.

# ### Time and Space Complexities

# - **Time Complexity**: \(O(N \log N)\), where \(N\) is the number of intervals. This is due to the sorting step.
# - **Space Complexity**: \(O(1)\) if we disregard the input storage, as we are using a constant amount of extra space.

# ### Implementation

# ```python
# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         # Sort intervals based on their start times
#         intervals.sort()
        
#         res = 0  # To count the number of intervals to be removed
#         prevEnd = intervals[0][1]  # End time of the last interval in the non-overlapping set
        
#         for start, end in intervals[1:]:
#             if start >= prevEnd:
#                 # No overlap, update prevEnd to the end of the current interval
#                 prevEnd = end
#             else:
#                 # Overlap, increment the counter and choose the interval with the smallest end time
#                 res += 1
#                 prevEnd = min(prevEnd, end)
        
#         return res
# ```

# ### Explanation

# 1. **Sorting**: The intervals are sorted based on their start times. This simplifies the process of checking overlaps.
# 2. **Initialization**: Start by assuming the first interval is part of the non-overlapping set. Initialize `prevEnd` to its end time.
# 3. **Iterate and Compare**:
#    - For each subsequent interval, check if its start time is greater than or equal to `prevEnd`.
#      - If true, it means there is no overlap, so update `prevEnd` to the end of this interval.
#      - If false, it means there is an overlap, so increment the counter `res` and update `prevEnd` to the minimum of the current `prevEnd` and the end of this interval to keep the interval with the earliest end time.

# This approach ensures that we always have the maximum number of non-overlapping intervals by greedily choosing intervals with the smallest possible end times in case of overlaps.