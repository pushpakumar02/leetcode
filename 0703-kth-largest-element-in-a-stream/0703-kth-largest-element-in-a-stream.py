class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) 
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)



### Intuition and Approach for `KthLargest`

#### Intuition

# To efficiently find the k-th largest element in a stream of numbers, we can use a min-heap. The min-heap will maintain the k largest elements seen so far, with the smallest of these k elements at the root of the heap. This way, the root of the heap always contains the k-th largest element.

#### Approach

# 1. **Initialization**:
#    - Store the value of `k` and the initial numbers in the object.
#    - Convert the list of numbers into a min-heap using `heapq.heapify`.
#    - Ensure the heap only contains the k largest elements by removing the smallest elements until the heap size is k.

# 2. **Add Method**:
#    - Insert the new value into the heap using `heapq.heappush`.
#    - If the heap exceeds size k, remove the smallest element using `heapq.heappop`.
#    - Return the root of the heap, which is the k-th largest element.

#### Time Complexity
# - **Initialization**: \(O(n \log n)\), where \(n\) is the length of the initial `nums` list, due to the heapify operation and potential pops to maintain the heap size.
# - **Add Method**: \(O(\log k)\) for each insertion since heap operations (push and pop) take logarithmic time relative to the size of the heap, which is constrained to k.

#### Space Complexity
# - **Overall**: \(O(k)\), as the heap maintains at most k elements.