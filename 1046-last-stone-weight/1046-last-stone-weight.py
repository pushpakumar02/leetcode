class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

# ### Intuition and Approach for `lastStoneWeight`

# #### Intuition

# To simulate the process of smashing the two heaviest stones, we can use a max-heap to efficiently access and remove the two largest stones. However, Python's `heapq` module only provides a min-heap by default, so we can invert the values of the stones to simulate a max-heap.

# #### Approach

# 1. **Convert to Max-Heap**:
#    - Invert the values of the stones (multiply by -1) and heapify the list. This converts the problem to a max-heap scenario using Python's min-heap implementation.

# 2. **Simulate Stone Smashing**:
#    - Continuously remove the two largest stones (smallest in the min-heap of negative values).
#    - If they are not equal, push the difference back into the heap.
#    - Continue until one or zero stones remain.

# 3. **Return Result**:
#    - If one stone remains, return its absolute value.
#    - If no stones remain, return 0.

# #### Time Complexity
# - **Heapify**: \(O(n)\), where \(n\) is the number of stones.
# - **Simulate Stone Smashing**: Each pop and push operation on the heap is \(O(\log n)\), and there are at most \(n-1\) such operations, leading to a total of \(O(n \log n)\).

# #### Space Complexity
# - **Overall**: \(O(n)\), due to the storage of the heap.
