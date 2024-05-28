# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right) 

### Intuition and Approach for `maxDepth`

#### Intuition

# The depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. To find the maximum depth, we need to explore all paths from the root to the leaves and keep track of the longest one.

#### Approach

# 1. **Base Case**: If the current node is `None`, the depth is `0` because we've reached a leaf's child.
# 2. **Recursive Depth Calculation**:
#    - Recursively find the maximum depth of the left subtree.
#    - Recursively find the maximum depth of the right subtree.
# 3. **Combine Results**: The depth of the current node is `1` (for the current node itself) plus the maximum of the depths of its left and right subtrees.
# 4. **Return the Result**: This process continues recursively, ultimately returning the maximum depth of the entire tree.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. Each node is visited once.

# #### Space Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the tree. This accounts for the space used by the recursion stack. In the worst case (a completely unbalanced tree), \(h\) could be \(n\); in the best case (a completely balanced tree), \(h\) is \(\log n\).