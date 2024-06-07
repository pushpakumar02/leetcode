class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid, len(grid[0]))
        visited = set()
        q = deque()

        def addNode(i, j):
            if (i < 0 or i == ROWS or j < 0 or j == COLS or (i,j) in visited or grid[i][j] == -1):
                return 
            
            visited.add((i, j))
            q.append([i, j])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        distance = 0
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = distance
                visited.add((i,j))

                addNode(i + 1, j)
                addNode(i - 1, j)
                addNode(i, j + 1)
                addNode(i, j - 1)
            distance += 1


'''### Intuition
The goal is to find the shortest distance from each cell to the nearest cell containing water (0). This can be efficiently achieved using a breadth-first search (BFS), which explores nodes layer by layer, ensuring that the shortest path is found first.

### Approach
1. **Initialization**:
   - Get the dimensions of the grid (ROWS, COLS).
   - Initialize a set (`visited`) to keep track of visited cells.
   - Initialize a queue (`q`) using deque to manage the BFS process.

2. **Add Water Cells to Queue**:
   - Iterate through the grid and add all cells containing water (0) to the queue.
   - Mark these cells as visited.

3. **BFS to Calculate Distances**:
   - Initialize a distance counter to zero.
   - Perform BFS:
     - For each cell in the queue, set its value in the grid to the current distance.
     - Add all valid neighboring cells (cells that are not out of bounds, not visited, and not blocked) to the queue and mark them as visited.
     - Increment the distance after processing all cells at the current distance level.

### Time Complexity
- **Time**: \(O(ROWS \times COLS)\), because each cell is processed at most once.

### Space Complexity
- **Space**: \(O(ROWS \times COLS)\), for the queue and visited set.

This ensures that each cell is visited in the shortest possible way from any water cell.

'''
