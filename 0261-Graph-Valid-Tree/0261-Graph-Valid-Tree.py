class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True

        adj = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n


### Intuition
# To determine if a graph is a valid tree, it must satisfy two conditions:
# 1. **Connected**: All nodes must be reachable from any starting node.
# 2. **Acyclic**: There must be no cycles in the graph.

### Approach
# 1. **Adjacency List Representation**:
#    - Create an adjacency list `adj` to represent the graph where each key is a node and the value is a list of its neighbors.

# 2. **DFS for Connectivity and Cycle Detection**:
#    - Use a set `visit` to keep track of visited nodes.
#    - Define a helper function `dfs(i, prev)`:
#      - If the current node `i` is already visited, a cycle is detected, return `False`.
#      - Add the current node `i` to `visit`.
#      - Recursively visit all its neighbors. If a neighbor is the node we came from (`prev`), skip it. If a recursive call detects a cycle, return `False`.
#      - If no cycle is detected for all neighbors, return `True`.

# 3. **Check All Conditions**:
#    - Start the DFS from node `0` with an initial `prev` value of `-1` (indicating no previous node).
#    - After the DFS, ensure that all nodes are visited (`len(visit) == n`). This ensures the graph is connected.
#    - Return `True` if both conditions (no cycles and all nodes visited) are met.

# ### Time Complexity
# - **Time**: \(O(V + E)\), where \(V\) is the number of nodes and \(E\) is the number of edges. Each node and edge is processed once.

# ### Space Complexity
# - **Space**: \(O(V + E)\), for the adjacency list and the recursion stack during DFS.
         
