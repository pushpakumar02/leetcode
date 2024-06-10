class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        visit = set()
        t = 0
        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap) 
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
                
        return t if  len(visit) == n else -1


# ### Intuition
# The goal is to determine the time it takes for all nodes in a network to receive a signal sent from a starting node `k`. This can be modeled as a shortest path problem on a weighted graph.

# ### Approach
# 1. **Graph Representation**:
#    - Use a dictionary to represent the graph, where each key is a node and the value is a list of tuples representing the neighboring nodes and the travel time to them.

# 2. **Priority Queue (Min-Heap)**:
#    - Utilize a min-heap to always expand the node with the smallest known distance first, similar to Dijkstra's algorithm.

# 3. **Visited Set**:
#    - Maintain a set to track visited nodes to avoid processing the same node multiple times.

# 4. **Algorithm**:
#    - Initialize the min-heap with the starting node `k` at time 0.
#    - While the heap is not empty:
#      - Extract the node with the smallest distance.
#      - If this node has already been visited, skip it.
#      - Mark the node as visited and update the maximum time taken (`t`).
#      - For each neighbor of the current node, if the neighbor has not been visited, add it to the heap with the updated travel time.
#    - If all nodes are visited, return the maximum time; otherwise, return -1 indicating not all nodes can be reached.

# ### Time Complexity
# - **Time**: \(O(E \log N)\), where \(E\) is the number of edges and \(N\) is the number of nodes. Each edge is processed once, and each operation on the heap (insertions and deletions) takes logarithmic time.

# ### Space Complexity
# - **Space**: \(O(N + E)\), where \(N\) is the number of nodes for the visited set and the heap, and \(E\) is the number of edges for the graph representation.

