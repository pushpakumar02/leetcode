class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+ 1) ]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[n]:
                par[p] = par[par[p]]
                p = par[p]
            return p
       
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p2 == p1:
                return False
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]

            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

    ### Intuition
# To find the redundant connection in an undirected graph, we can use the Union-Find data structure (also known as Disjoint Set Union, DSU). This structure helps efficiently manage and merge sets of elements, which is useful for detecting cycles in the graph.

# ### Approach
# 1. **Union-Find Initialization**:
#    - Initialize two arrays, `par` (parent) and `rank`:
#      - `par`: Represents the parent of each node. Initially, each node is its own parent.
#      - `rank`: Represents the rank (size) of each set. Initially, each set has a rank of 1.

# 2. **Find Function**:
#    - Implements path compression to flatten the structure of the tree, making future queries faster.
#    - Traverse up the tree until reaching the root. During traversal, make each node point directly to the root.

# 3. **Union Function**:
#    - Implements union by rank to attach the smaller tree under the root of the larger tree.
#    - If the nodes have the same root, they form a cycle, and the current edge is redundant.

# 4. **Processing Edges**:
#    - For each edge `(n1, n2)`, check if they can be unioned without forming a cycle.
#    - If union returns `False`, it means `n1` and `n2` are already connected, hence the edge `(n1, n2)` is redundant.

# ### Time Complexity
# - **Time**: \(O(E \cdot \alpha(V))\), where \(E\) is the number of edges and \(V\) is the number of vertices. \(\alpha\) is the Inverse Ackermann function, which grows very slowly and is almost constant for practical purposes.

# ### Space Complexity
# - **Space**: \(O(V)\), where \(V\) is the number of vertices, for storing the parent and rank arrays.

