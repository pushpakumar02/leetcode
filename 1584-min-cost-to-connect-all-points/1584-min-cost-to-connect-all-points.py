class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        minH = [[0, 0]]

        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost    
            visit.add(i)
            
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei]) 
        return res

# ### Intuition
# To find the minimum cost to connect all points in a 2D plane, we can model this problem as finding the Minimum Spanning Tree (MST) of a graph where each point is a node and each edge is the Manhattan distance between two points.

# ### Approach
# 1. **Graph Representation**:
#    - Create an adjacency list where each node points to a list of tuples representing its neighbors and the corresponding Manhattan distances.

# 2. **Prim's Algorithm**:
#    - Initialize a min-heap with a starting point (cost of 0 for the first node).
#    - Use a set to keep track of visited nodes.
#    - While there are still nodes to visit:
#      - Pop the smallest cost edge from the heap.
#      - If the node has already been visited, continue.
#      - Add the cost to the result and mark the node as visited.
#      - For each neighbor of the current node, if the neighbor hasn't been visited, add the edge to the heap.
#    - Continue until all nodes are visited.

# ### Time Complexity
# - **Time**: \(O(N^2 \log N)\), where \(N\) is the number of points. Constructing the adjacency list takes \(O(N^2)\) and each insertion/deletion operation in the min-heap takes \(O(\log N)\).

# ### Space Complexity
# - **Space**: \(O(N^2)\) for the adjacency list and the min-heap can have up to \(N^2\) entries in the worst case.