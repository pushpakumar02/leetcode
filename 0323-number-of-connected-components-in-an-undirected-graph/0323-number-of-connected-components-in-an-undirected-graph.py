class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1 
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2 
                rank[p2] += rank[p1]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res





'''
### Intuition and Approach

The problem requires finding the number of connected components in an undirected graph. This can be efficiently solved using the Union-Find (Disjoint Set Union, DSU) data structure. Union-Find helps manage a partition of a set into disjoint subsets and supports two operations efficiently:
1. **Find**: Determine the subset a particular element is in.
2. **Union**: Join two subsets into a single subset.

### Steps:

1. **Initialization**:
   - Create an array `par` where `par[i]` is the parent of node `i`. Initially, each node is its own parent.
   - Create an array `rank` to keep track of the tree's rank (or depth). Initially, all ranks are 1.

2. **Find Operation with Path Compression**:
   - The `find` function returns the root parent of a node. During the process, it compresses the path, making future queries faster.

3. **Union Operation with Union by Rank**:
   - The `union` function connects two nodes. It ensures the smaller tree is always attached under the larger tree to keep the structure balanced.

4. **Count Components**:
   - Iterate over all edges. For each edge, use the `union` function to connect nodes. If the nodes are already connected, `union` returns 0. If they are not, `union` connects them and returns 1, decrementing the count of components.

### Time Complexity:
- **Find** and **Union** operations: \(O(\alpha(n))\) where \(\alpha\) is the inverse Ackermann function, which is very slow-growing, making it almost constant for practical purposes.
- Total complexity is \(O(E \cdot \alpha(n))\) where \(E\) is the number of edges.

### Space Complexity:
- \(O(n)\) for storing the parent and rank arrays.

Here's the complete code with the described approach:

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize parent and rank arrays
        par = [i for i in range(n)]
        rank = [1] * n

        # Find function with path compression
        def find(n1):
            res = n1 
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        # Union function with union by rank
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2 
                rank[p2] += rank[p1]
            return 1

        # Initialize result with number of nodes
        res = n
        # Iterate through each edge and union the nodes
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res
```

### Explanation:
- **Initialization**: Each node is its own parent. All ranks are 1.
- **Find with Path Compression**: Ensures that each node points directly to the root, flattening the structure and speeding up future operations.
- **Union with Rank**: Ensures the smaller tree is always attached under the larger tree, keeping the structure balanced.
- **Counting Components**: Each successful union decreases the count of components by 1. The final count represents the number of connected components in the graph.
