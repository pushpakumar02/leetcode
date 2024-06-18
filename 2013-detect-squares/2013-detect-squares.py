class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(px - x ) != abs(py - y)) or px == x or py == y :
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)] 
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)






# The `DetectSquares` class allows for adding points to a collection and then counting the number of squares that can be formed using a given point as one of the vertices. The class utilizes a combination of a list to store points and a dictionary to keep track of the frequency of each point. Let's break down the approach and the implementation:

# ### Key Points of the Implementation

# 1. **Data Structures**:
#    - `self.ptsCount`: A dictionary (using `defaultdict(int)`) to count the occurrences of each point.
#    - `self.pts`: A list to store all added points.

# 2. **Methods**:
#    - `add(point: List[int]) -> None`: Adds a point to both the dictionary and the list.
#    - `count(point: List[int]) -> int`: Counts the number of valid squares using the given point as one of the vertices.

# ### Steps in `count` Method

# 1. **Extract Coordinates**:
#    - Get the x and y coordinates of the given point `point`.

# 2. **Iterate Through Points**:
#    - For each point in `self.pts`, check if the point can form a diagonal with the given point.
#    - Check if the absolute differences in x and y coordinates are the same (ensuring a square).
#    - Ensure the points are not aligned vertically or horizontally.

# 3. **Count Squares**:
#    - If the conditions are met, calculate the potential squares by looking at points that could form the other two corners of the square.
#    - Use the counts from `self.ptsCount` to find how many such squares can be formed.

# ### Time Complexity

# - **`add` Method**: \(O(1)\) for updating the count and appending to the list.
# - **`count` Method**: \(O(N)\), where \(N\) is the number of points added so far, as it involves iterating through all points and performing constant time operations for each point.

# ### Code Implementation

# ```python
# from collections import defaultdict
# from typing import List

# class DetectSquares:

#     def __init__(self):
#         self.ptsCount = defaultdict(int)
#         self.pts = []

#     def add(self, point: List[int]) -> None:
#         self.ptsCount[tuple(point)] += 1
#         self.pts.append(point)

#     def count(self, point: List[int]) -> int:
#         res = 0
#         px, py = point
#         for x, y in self.pts:
#             # Check if we have a valid diagonal candidate
#             if (abs(px - x) != abs(py - y)) or px == x or py == y:
#                 continue
#             # Count the possible squares
#             res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
#         return res

# # Example usage:
# # obj = DetectSquares()
# # obj.add([3, 10])
# # obj.add([11, 2])
# # obj.add([3, 2])
# # print(obj.count([11, 10]))  # Output should be 1
# ```

# ### Explanation of the Example

# - Points are added to the structure.
# - When `count([11, 10])` is called, it checks possible squares that can be formed with the given point `[11, 10]` and the added points.
# - It finds that with the points `[3, 10]`, `[11, 2]`, and `[3, 2]`, a square can be formed.

# This implementation is efficient for the operations described and correctly handles the addition and counting of points to detect squares.