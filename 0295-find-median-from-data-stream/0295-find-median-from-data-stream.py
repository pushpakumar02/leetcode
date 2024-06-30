class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large) and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val =  heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return  self.large[0] 
        return (-1 * self.small[0] + self.large[0]) / 2
            



### MedianFinder: Intuition and Approach

# The `MedianFinder` class uses two heaps (priority queues) to efficiently find the median of a stream of numbers. The heaps are used to keep track of the smaller half and the larger half of the numbers seen so far. 

# ### Heaps:
# 1. **Max-Heap (`small`)**: To keep track of the smaller half of the numbers. Since Python's `heapq` module only provides a min-heap, we simulate a max-heap by pushing the negative of the numbers.
# 2. **Min-Heap (`large`)**: To keep track of the larger half of the numbers.

# ### Invariant:
# - The largest number in the max-heap (`small`) should be less than or equal to the smallest number in the min-heap (`large`).
# - The size difference between the two heaps should not exceed 1 to maintain a balanced division of numbers for median calculation.

# ### Operations:

# 1. **`addNum(num)`**:
#    - Insert the new number into the max-heap (`small`).
#    - Balance the heaps if necessary to maintain the invariant.
#    - Ensure neither heap is more than one element larger than the other.

# 2. **`findMedian()`**:
#    - If one heap has more elements than the other, the median is the root of that heap.
#    - If both heaps have the same number of elements, the median is the average of the roots of the two heaps.

# ### Complexity:
# - **Time Complexity**:
#   - `addNum(num)`: \(O(\log n)\) due to heap operations.
#   - `findMedian()`: \(O(1)\) as it only involves checking the roots of the heaps.
# - **Space Complexity**: \(O(n)\) where \(n\) is the number of elements added, as we store all elements in the heaps.

# ### Implementation:

# ```python
# import heapq

# class MedianFinder:

#     def __init__(self):
#         self.small = []  # Max-Heap (inverted)
#         self.large = []  # Min-Heap

#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.small, -1 * num)

#         # Ensure the smallest of large is greater than the largest of small
#         if (self.small and self.large) and (-1 * self.small[0] > self.large[0]):
#             val = -1 * heapq.heappop(self.small)
#             heapq.heappush(self.large, val)

#         # Balance the size of the heaps
#         if len(self.small) > len(self.large) + 1:
#             val = -1 * heapq.heappop(self.small)
#             heapq.heappush(self.large, val)
        
#         if len(self.large) > len(self.small) + 1:
#             val = heapq.heappop(self.large)
#             heapq.heappush(self.small, -1 * val)

#     def findMedian(self) -> float:
#         if len(self.small) > len(self.large):
#             return -1 * self.small[0]
#         if len(self.large) > len(self.small):
#             return self.large[0]
#         return (-1 * self.small[0] + self.large[0]) / 2

# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()
# ```

# ### Explanation:
# - **`__init__`**: Initializes two heaps.
# - **`addNum(num)`**:
#   - Adds the number to `small` as a negative to simulate max-heap behavior.
#   - Ensures the heaps are balanced and the invariants are maintained.
# - **`findMedian()`**:
#   - Determines the median based on the sizes and the roots of the heaps.

# This approach ensures efficient median calculation in a streaming context, with optimal time complexity for both adding numbers and finding the median.
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()