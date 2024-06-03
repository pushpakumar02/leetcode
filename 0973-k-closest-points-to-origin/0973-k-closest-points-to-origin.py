class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x, y):
            return x**2 + y**2

        heap = []

        for x, y in points:
            d = distance(x, y)
            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y))
            else:
                heapq.heappushpop(heap, (-d, x, y))

        return [[x, y] for d, x, y in heap]

### Intuition and Approach for `kClosest`

#### Intuition
# We need to find the k points closest to the origin. Using a max-heap allows us to efficiently keep track of the k smallest distances encountered so far.

# #### Approach
# 1. **Define a Distance Function**:
#    - Calculate the squared distance from the origin to avoid computing square roots.

# 2. **Use a Max-Heap**:
#    - Iterate through each point and compute its distance.
#    - Maintain a max-heap of size k:
#      - Push the negative distance and point coordinates into the heap.
#      - If the heap exceeds size k, remove the largest distance.
   
# 3. **Return the Result**:
#    - Extract the points from the heap and return them.

# #### Time Complexity
# - **Building the Heap**: \(O(n \log k)\), where \(n\) is the number of points and \(k\) is the number of closest points needed.

# #### Space Complexity
# - **Heap Storage**: \(O(k)\), for storing the k closest points.

# This approach ensures we efficiently find the k closest points using a max-heap.