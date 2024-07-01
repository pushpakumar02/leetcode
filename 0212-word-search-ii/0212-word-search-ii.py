class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                 (r, c) in visit or 
                 board[r][c] not in node.children):
                return 
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                 dfs(r, c, root, "")
        return list(res)





### Intuition and Approach

# The `findWords` function in the `Solution` class is designed to find all words from a given list that can be formed by tracing a path in a given board of letters. The approach uses a Trie (prefix tree) to store the list of words and then performs Depth-First Search (DFS) on the board to find all possible words.

# ### Steps:

# 1. **Trie Construction**:
#    - A Trie is constructed where each node represents a character in the word.
#    - The `TrieNode` class supports the addition of words to the Trie.

# 2. **DFS Search on Board**:
#    - For each cell in the board, initiate a DFS to explore all possible paths that can form words.
#    - Use a `visit` set to keep track of visited cells during the DFS to avoid revisiting and forming invalid paths.
#    - If a path forms a valid word (i.e., exists in the Trie), add it to the result set.

# ### Detailed Implementation:

# #### TrieNode Class:
# - The `TrieNode` class has a dictionary `children` to store the children nodes and a boolean `isWord` to mark the end of a word.
# - The `addWord` method inserts words into the Trie.

# #### Solution Class:
# - The `findWords` method initializes the Trie with the list of words and prepares the board dimensions.
# - The `dfs` method is a recursive function to explore all possible paths from a given cell.
# - The main loop iterates over each cell in the board to start a DFS from there.

# ### Time Complexity:
# - Building the Trie: \(O(W \cdot L)\), where \(W\) is the number of words and \(L\) is the average length of a word.
# - DFS Search: \(O(M \cdot N \cdot 4^L)\), where \(M\) and \(N\) are the dimensions of the board, and \(L\) is the length of the longest word. The factor \(4^L\) accounts for the potential paths taken in the worst-case scenario.

# ### Space Complexity:
# - Trie Storage: \(O(W \cdot L)\) for storing the words.
# - DFS Stack and `visit` Set: \(O(M \cdot N)\) for keeping track of visited cells.

# Here's the complete code:

# ```python
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False
    
#     def addWord(self, word):
#         cur = self
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
#             cur = cur.children[c]
#         cur.isWord = True

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         root = TrieNode()
#         for w in words:
#             root.addWord(w)
        
#         ROWS, COLS = len(board), len(board[0])
#         res, visit = set(), set()

#         def dfs(r, c, node, word):
#             if (r < 0 or c < 0 or 
#                 r >= ROWS or c >= COLS or
#                  (r, c) in visit or 
#                  board[r][c] not in node.children):
#                 return 
            
#             visit.add((r, c))
#             node = node.children[board[r][c]]
#             word += board[r][c]
#             if node.isWord:
#                 res.add(word)

#             dfs(r + 1, c, node, word)
#             dfs(r, c + 1, node, word)
#             dfs(r - 1, c, node, word)
#             dfs(r, c - 1, node, word)
#             visit.remove((r, c))

#         for r in range(ROWS):
#             for c in range(COLS):
#                  dfs(r, c, root, "")
#         return list(res)
# ```

# ### Explanation:
# - The `findWords` function builds the Trie and sets up the board dimensions.
# - The `dfs` function recursively explores all possible directions (up, down, left, right) from a given cell, adding valid words to the result set.
# - The main loop starts DFS from every cell in the board to ensure all potential words are found.

# This solution efficiently combines Trie and DFS to solve the problem of finding words in a board, leveraging the Trie to optimize word lookups and the DFS to explore possible paths on the board.