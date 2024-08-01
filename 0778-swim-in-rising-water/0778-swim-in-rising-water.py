class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]] 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] 

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or 
                    neiR == N or neiC == N or 
                    (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])




### Intuition and Approach

# The problem is to determine the minimum time required to swim from the top-left to the bottom-right corner of a grid, where each cell contains an elevation, and you can only move up, down, left, or right.

# This problem can be modeled as a graph traversal problem, where each cell in the grid is a node, and edges between nodes have weights corresponding to the maximum elevation encountered so far on the path. The goal is to minimize this maximum elevation, which can be efficiently solved using a priority queue with Dijkstra's algorithm or a similar approach.

# ### Approach

# 1. **Priority Queue Initialization**:
#    - Initialize a priority queue (`minH`) starting with the top-left corner of the grid.
#    - The priority queue will store tuples of the form (elevation, row, column), where `elevation` is the maximum elevation encountered to reach the cell at `(row, column)`.

# 2. **Traversal with Priority Queue**:
#    - Use a set (`visit`) to keep track of visited cells to avoid processing them multiple times.
#    - While the priority queue is not empty:
#      - Pop the cell with the minimum elevation from the priority queue.
#      - If this cell is the bottom-right corner, return the current elevation as the result.
#      - For each of the four possible directions (up, down, left, right), compute the coordinates of the neighboring cell.
#      - If the neighboring cell is within the grid bounds and has not been visited, add it to the priority queue with the updated maximum elevation and mark it as visited.

# ### Time and Space Complexities

# - **Time Complexity**:
#   - The priority queue operations (insertion and extraction) take \(O(\log N^2)\), where \(N\) is the grid size.
#   - Each cell is processed once, leading to \(O(N^2 \log N^2)\) time complexity.

# - **Space Complexity**:
#   - The priority queue can contain up to \(N^2\) cells, requiring \(O(N^2)\) space.
#   - The visited set also requires \(O(N^2)\) space.
#   - Thus, the overall space complexity is \(O(N^2)\).



# ```python
# import heapq

# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         N = len(grid)
#         visit = set()
#         minH = [[grid[0][0], 0, 0]] 
#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] 

#         visit.add((0, 0))
#         while minH:
#             t, r, c = heapq.heappop(minH)

#             if r == N - 1 and c == N - 1:
#                 return t
            
#             for dr, dc in directions:
#                 neiR, neiC = r + dr, c + dc
#                 if (neiR < 0 or neiC < 0 or 
#                     neiR >= N or neiC >= N or 
#                     (neiR, neiC) in visit):
#                     continue
#                 visit.add((neiR, neiC))
#                 heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
# ```

# This solution uses a priority queue to ensure that we always explore the least elevated path available, effectively simulating a flood fill where we prioritize cells by their elevation, ensuring we find the minimum possible "time" to swim from the top-left to the bottom-right of the grid.