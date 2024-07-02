class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        
        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1 

        return [res[q] for q in queries]





# The problem is to find the minimum interval length that contains each query from a list of queries. To solve this problem efficiently, we can use a combination of sorting and a min-heap (priority queue).

# ### Detailed Steps:

# 1. **Sort Intervals and Queries**:
#    - Sort the intervals based on their starting point.
#    - Sort the queries in ascending order to process them in increasing order.

# 2. **Using a Min-Heap**:
#    - Use a min-heap to keep track of the intervals that can potentially cover the current query. The heap will store tuples of `(interval_length, end_point)`.

# 3. **Processing Queries**:
#    - For each query, add all intervals that start before or at the query to the heap.
#    - Remove intervals from the heap that end before the query since they cannot cover the query.
#    - The smallest element in the heap (if the heap is not empty) represents the smallest interval covering the current query.

# 4. **Result Collection**:
#    - Store the result for each query in a dictionary.
#    - After processing all queries, retrieve the results in the original order of the queries.

# Here is the complete implementation:

# ```python
# import heapq
# from typing import List

# class Solution:
#     def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
#         # Sort intervals based on their starting point
#         intervals.sort()
        
#         minHeap = []
#         res, i = {}, 0
#         for q in sorted(queries):
#             # Add all intervals that start before or at q to the heap
#             while i < len(intervals) and intervals[i][0] <= q:
#                 l, r = intervals[i]
#                 heapq.heappush(minHeap, (r - l + 1, r))
#                 i += 1

#             # Remove all intervals from the heap that end before q
#             while minHeap and minHeap[0][1] < q:
#                 heapq.heappop(minHeap)
            
#             # If the heap is not empty, the smallest interval is at the top
#             res[q] = minHeap[0][0] if minHeap else -1 

#         # Return results in the order of the original queries
#         return [res[q] for q in queries]
# ```

# ### Explanation:

# 1. **Sorting**:
#    - `intervals.sort()`: Sort intervals by their starting points.
#    - `for q in sorted(queries)`: Process queries in sorted order.

# 2. **Heap Operations**:
#    - `heapq.heappush(minHeap, (r - l + 1, r))`: Push intervals into the heap with their lengths and end points.
#    - `while minHeap and minHeap[0][1] < q`: Remove intervals from the heap that cannot cover the current query.

# 3. **Result Storage**:
#    - Use a dictionary `res` to store the minimum interval length for each query.
#    - Construct the final result by fetching the answers for each query in their original order.

# This approach ensures that each query is processed efficiently by leveraging the heap to maintain the smallest possible interval at any given time. The overall complexity is dominated by the sorting steps, making it `O((n + m) log n)`, where `n` is the number of intervals and `m` is the number of queries.