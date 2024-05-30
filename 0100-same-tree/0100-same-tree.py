# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def same(p, q):
            if not p and not q:
                return True

            if (not p and q) or (p and not q):
                return False

            if p.val != q.val:
                return False

            return same(p.left, q.left) and same(p.right,  q.right)

        return same(p, q)  

### Intuition and Approach for `isSameTree`

#### Intuition

# To determine if two binary trees are identical, we need to compare their structures and the values of their nodes. Two trees are considered the same if they have the same structure and corresponding nodes have the same values.

# #### Approach

# 1. **Recursive Comparison**:
#    - Use a helper function `same` that takes two nodes, one from each tree.
#    - Check if both nodes are `None`. If they are, the trees are identical up to this point.
#    - If one node is `None` and the other is not, the trees are not identical.
#    - If the values of the nodes are different, the trees are not identical.
#    - Recursively check the left and right subtrees of both nodes.

# 2. **Base Cases**:
#    - Both nodes being `None` indicates identical subtrees up to this point.
#    - One node being `None` while the other is not indicates a structural difference.
#    - Different values at corresponding nodes indicate the trees are not identical.

# 3. **Recursive Checks**:
#    - For each pair of nodes, recursively check their left children and right children.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the smaller of the two trees. This is because each node is visited once.

# #### Space Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the trees. This accounts for the space used by the recursion stack. In the worst case (a completely unbalanced tree), \(h\) could be \(n\); in the best case (a completely balanced tree), \(h\) is \(\log n\).
