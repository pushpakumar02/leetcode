# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

### Intuition and Approach for `invertTree`

#### Intuition

# Inverting a binary tree means swapping the left and right children of every node in the tree. This can be done recursively by processing each node, swapping its children, and then recursively inverting its left and right subtrees.

#### Approach

# 1. **Base Case**: If the current node is `None`, return `None` (this handles the leaf node case and stops further recursion).
# 2. **Swap Children**: Swap the left and right children of the current node.
# 3. **Recursive Inversion**:
#    - Recursively invert the left subtree.
#    - Recursively invert the right subtree.
# 4. **Return the Root**: After inverting the entire tree, return the root node.

# This approach ensures that every node in the tree is processed and its children are swapped, resulting in the entire tree being inverted.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. Each node is visited once.

# #### Space Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the tree. This accounts for the space used by the recursion stack. In the worst case (a completely unbalanced tree), \(h\) could be \(n\); in the best case (a completely balanced tree), \(h\) is \(\log n\).