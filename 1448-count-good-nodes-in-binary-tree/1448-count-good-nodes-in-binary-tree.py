# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node: return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)


### Intuition and Approach for `goodNodes`

#### Intuition

# In a binary tree, a node is considered "good" if in the path from the root to that node, there are no nodes with a value greater than the node's value. Essentially, each node must be the maximum value encountered along the path from the root.

# #### Approach

# 1. **Depth-First Search (DFS)**:
#    - We will use DFS to traverse the tree.
#    - At each node, keep track of the maximum value encountered on the path from the root to the current node.

# 2. **Counting Good Nodes**:
#    - If the current node's value is greater than or equal to the maximum value encountered so far, it is a "good" node.
#    - Update the maximum value to the current node's value if it is greater than the current maximum.

# 3. **Recursive DFS**:
#    - Recursively apply the same logic to the left and right children of the current node.
#    - Accumulate the count of "good" nodes from the left and right subtrees.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. Each node is visited exactly once.

# #### Space Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the tree. This is due to the recursive call stack.
