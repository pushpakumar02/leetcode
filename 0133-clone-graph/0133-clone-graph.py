"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        oldTonew = {}
        def dfs(node):            
            if node  in oldTonew:
                return oldTonew[node]

            copy = Node(node.val)
            oldTonew[node] = copy 
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) 


### Intuition
# To clone a graph, we need to create a deep copy where every node and its connections are duplicated. This involves visiting each node, creating a copy of it, and then recursively copying all its neighbors. A hashmap (dictionary) is used to keep track of the original node and its corresponding copy to avoid redundant work and infinite loops.

# ### Approach
# 1. **Edge Case**:
#    - If the input node is `None`, return `None`.

# 2. **HashMap Initialization**:
#    - Use a hashmap (`oldToNew`) to store the mapping from the original nodes to their copies.

# 3. **DFS Helper Function**:
#    - If the node is already copied (exists in `oldToNew`), return its copy.
#    - Otherwise, create a new copy of the node and add it to the hashmap.
#    - Recursively copy all neighbors and append them to the neighbor list of the copied node.

# 4. **DFS Invocation**:
#    - Start the DFS from the input node.

# ### Time Complexity
# - **Time**: \(O(N + E)\), where \(N\) is the number of nodes and \(E\) is the number of edges. Each node and edge is visited once.

# ### Space Complexity
# - **Space**: \(O(N)\), where \(N\) is the number of nodes. The space is used by the recursion stack and the hashmap.

# This approach ensures that each node and its connections are copied exactly once, making the algorithm efficient and avoiding unnecessary computations.

          


