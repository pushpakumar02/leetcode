class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if len(word) == i: return True
            
            if( r < 0 or c < 0 or
                r >= ROWS or c >= COLS or word[i] != board[r][c] or 
                (r, c) in path ): 
                return False

            path.add((r, c))
            res = ( dfs(r+1, c , i + 1) or 
                    dfs(r-1, c , i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1 , i + 1))
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False




# **Intuition:**

# The problem asks if a given word `word` can be formed by connecting characters in a 2D character grid `board`, where characters can be used only once. This function employs a Depth-First Search (DFS) approach to explore all possible paths in the grid.

# **Approach:**

# 1. **Initialization:**
#    - `ROWS` and `COLS` store the dimensions of the `board`.
#    - `path` is a set to keep track of visited cells, preventing revisiting and forming invalid paths (using the same character multiple times).

# 2. **DFS Function:**
#    - **Base Case:** If the current index `i` reaches the length of the word (`len(word)`), it means the entire word has been found on the board. Return `True`.
#    - **Out-of-Bounds or Mismatch:** Check if the current row (`r`), column (`c`), or the character at `board[r][c]` doesn't match the target word's character at index `i`. Also, check if the current cell is already in the `path` set (visited). If any of these conditions hold, return `False`, indicating an invalid path.
#    - **Mark Visited:** Add the current cell coordinates (`(r, c)`) to the `path` set to mark it as visited.
#    - **Recursive Calls:** Explore four possible directions (up, down, left, right) using recursive calls to `dfs`. For each direction, increment `i` by 1 to check the next character in the word. The return value is a combination of results from these recursive calls using the `or` operator (`|`).
#    - **Backtrack:** After exploring all directions, remove the current cell from the `path` set using `path.remove((r, c))` to allow revisiting in other paths during backtracking.
#    - **Return Result:** Return the final result (`res`), which is either `True` if the word is found or `False` if not.

# 3. **Outer Loop for Starting Points:**
#    - Iterate through each row (`r`) and column (`c`) of the `board`.
#    - For each cell, initiate a DFS exploration by calling `dfs(r, c, 0)`. If any of these calls return `True`, it signifies the word was found. Return `True`.

# 4. **Overall Result:**
#    - If no successful path is found starting from any cell, the function returns `False`.

# **Time Complexity:**

# - In the worst case, for each cell, the DFS might explore all four directions recursively, leading to a branching factor of 4.
# - The recursion tree can have a depth of `ROWS * COLS` (number of cells) in the worst case, where the entire grid is traversed.
# - However, if the word is not present in the board, exploration stops earlier.
# - The overall time complexity can be considered O(4^(ROWS*COLS)) in the worst case, but the actual complexity depends on the presence of the word and the grid size.

# **Space Complexity:**

# - The recursion stack, in the worst case, can have a depth of `ROWS * COLS`.
# - The `path` set scales linearly with the number of visited cells, which could be up to `ROWS * COLS` in the worst case.
# - Therefore, the space complexity is dominated by the recursion stack, which is O(ROWS * COLS).

# **Key Points:**

# - DFS systematically explores all possible paths in the grid.
# - The `path` set ensures that cells are visited only once, preventing invalid paths.
# - The function returns `True` as soon as the word is found, avoiding unnecessary exploration.

# **Additional Considerations:**

# - The worst-case time complexity can be high for large grids. If you need a more efficient solution for specific use cases, consider techniques like backtracking with memoization or trie-based approaches.
# - For very large grids or long words, the space complexity might be a factor. If memory is a concern, explore alternative algorithms that might have lower space requirements.

