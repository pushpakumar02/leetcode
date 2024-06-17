"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True

"""
### Intuition

The problem of determining if a person can attend all meetings without any overlap can be solved using a simple greedy algorithm. The key idea is to sort the intervals based on their start times and then check for any overlaps between consecutive intervals.

### Approach

1. **Sort Intervals**: First, sort the intervals based on their start times. This allows us to easily check for overlaps by comparing each interval with the previous one.
2. **Check for Overlaps**: Iterate through the sorted list of intervals and compare the end time of the current interval with the start time of the next interval. If the end time of any interval is greater than the start time of the next interval, it indicates an overlap, and the person cannot attend all meetings.

### Time and Space Complexities

- **Time Complexity**: \(O(N \log N)\), where \(N\) is the number of intervals. This is due to the sorting step.
- **Space Complexity**: \(O(1)\), as we are using a constant amount of extra space.

### Implementation

```python
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals based on their start times
        intervals.sort(key=lambda i: i.start)

        # Check for any overlapping intervals
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            
            if i1.end > i2.start:
                return False
        
        return True
```

### Explanation

1. **Sorting**: We sort the list of intervals by their start times. This ensures that we can simply compare each interval with the next one to check for overlaps.
2. **Checking for Overlaps**: 
   - We iterate through the sorted list starting from the second interval.
   - For each interval `i2`, we compare it with the previous interval `i1`.
   - If `i1.end` is greater than `i2.start`, it means there is an overlap, and we return `False`.
3. **Return Result**: If no overlaps are found after checking all intervals, we return `True`, indicating that the person can attend all meetings.

This method efficiently determines whether all meetings can be attended without any overlap by leveraging sorting and a single pass comparison.
"""
