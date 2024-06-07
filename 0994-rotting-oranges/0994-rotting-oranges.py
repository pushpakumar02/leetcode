class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append((i, j))
                elif grid[i][j] == FRESH:
                    fresh += 1
        
        if fresh == 0:
            return 0

        minutes = -1
        while q:
            size_q = len(q)
            minutes += 1
            for _ in range(size_q):
                i, j = q.popleft()
                for r, c in [(i+1, j), (i, j+1), (i-1, j), (i,j-1)]:
                    if (0 <= r < m and 0 <= c < n and grid[r][c] == FRESH):
                        grid[r][c] = ROTTEN
                        fresh -= 1
                        q.append((r, c))

        if fresh == 0:
            return minutes
        return -1 

### Intuition
# To determine the minimum time required for all fresh oranges to rot, we can use a Breadth-First Search (BFS) approach. The BFS is ideal because it explores nodes (or oranges in this case) level by level, ensuring that we capture the spread of rot in the shortest possible time from multiple sources simultaneously.

# ### Approach
# 1. **Initialization**:
#    - Define constants for empty cells (0), fresh oranges (1), and rotten oranges (2).
#    - Get the dimensions of the grid.
#    - Initialize a queue (`q`) to keep track of the rotten oranges and their positions.
#    - Count the number of fresh oranges.

# 2. **Add Initial Rotten Oranges to Queue**:
#    - Iterate through the grid to find all rotten oranges and add their positions to the queue.
#    - Also, count the total number of fresh oranges.

# 3. **BFS to Spread Rot**:
#    - If there are no fresh oranges initially, return 0 immediately as no time is needed.
#    - Initialize a minutes counter to track the time.
#    - While there are positions in the queue:
#      - For each position in the queue, spread the rot to its adjacent cells (up, down, left, right) if they contain fresh oranges.
#      - Add these newly rotten oranges to the queue.
#      - Decrease the fresh orange count accordingly.
#      - Increment the minutes counter after processing all current rotten oranges in the queue.

# 4. **Check Remaining Fresh Oranges**:
#    - If no fresh oranges are left, return the time taken in minutes.
#    - If there are still fresh oranges left after the BFS completes, return -1 indicating that not all fresh oranges can rot.

# ### Time Complexity
# - **Time**: \(O(m \times n)\), where \(m\) is the number of rows and \(n\) is the number of columns in the grid. This is because each cell is processed at most once.

# ### Space Complexity
# - **Space**: \(O(m \times n)\), for the queue and the space needed to store the grid state.

