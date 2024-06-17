"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        res, count = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)
        return res

"""
### Intuition

To determine the minimum number of meeting rooms required, we can track the start and end times of the meetings separately. By doing this, we can simulate the process of meetings starting and ending over time. The key idea is to sort the start times and end times, and then use two pointers to traverse through these lists, incrementing the count of rooms when a meeting starts and decrementing when a meeting ends. The maximum count during this process will give us the minimum number of rooms required.

### Approach

1. **Separate and Sort**: Extract and sort the start times and end times of all meetings.
2. **Two-Pointer Technique**: Use two pointers to traverse the start and end times.
   - If the current start time is less than the current end time, it means a new meeting is starting before the previous one ends, so increment the room count.
   - If the current end time is less than or equal to the start time, it means a meeting has ended, so decrement the room count.
3. **Track Maximum Rooms**: Keep track of the maximum room count encountered during the traversal, which will be the result.

### Time and Space Complexities

- **Time Complexity**: \(O(N \log N)\), where \(N\) is the number of intervals. This is primarily due to the sorting step.
- **Space Complexity**: \(O(N)\) for storing the start and end times.

### Implementation

```python
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Extract and sort start and end times
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        # Initialize pointers and counters
        s, e = 0, 0
        res, count = 0, 0

        # Traverse through all the start times
        while s < len(intervals):
            # If a meeting is starting before the previous one ends, increment the room count
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                # If a meeting has ended, decrement the room count
                e += 1
                count -= 1
            
            # Track the maximum room count
            res = max(res, count)
        
        return res
```

### Explanation

1. **Extract and Sort**:
   - We extract the start and end times from the intervals and sort them separately.
   
2. **Two-Pointer Technique**:
   - We initialize two pointers `s` and `e` to traverse the start and end times respectively.
   - We also initialize `res` to keep track of the maximum number of rooms needed at any point in time and `count` to track the current number of rooms in use.
   - We iterate through all the start times:
     - If the current meeting starts before the previous one ends (`start[s] < end[e]`), increment `count` and move to the next start time.
     - If a meeting ends before the next one starts (`end[e] <= start[s]`), decrement `count` and move to the next end time.
   - Update `res` to the maximum value of `count` during each iteration.

3. **Result**:
   - The value of `res` after the iteration completes gives us the minimum number of meeting rooms required to accommodate all the meetings without any overlap.

This approach ensures that we efficiently determine the number of meeting rooms needed using sorting and a linear scan.
