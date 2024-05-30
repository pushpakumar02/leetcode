# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur

### Intuition and Approach for `lowestCommonAncestor`

#### Intuition

# To find the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST), we can leverage the properties of BST. The key property is that for any node, all nodes in its left subtree have smaller values, and all nodes in its right subtree have larger values. The LCA of two nodes `p` and `q` is the deepest node that is an ancestor of both `p` and `q`.

#### Approach

# 1. **Start from the Root**:
#    - Begin the search from the root of the BST.

# 2. **Binary Search**:
#    - If both `p` and `q` are smaller than the current node, then the LCA must be in the left subtree.
#    - If both `p` and `q` are larger than the current node, then the LCA must be in the right subtree.
#    - If one node is on one side and the other node is on the other side (or if one of them is the current node), then the current node is the LCA.

# 3. **Loop until Found**:
#    - Continue traversing the tree until you find the split point where one node is in the left subtree and the other is in the right subtree, or one of the nodes is the current node.

# #### Time Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the tree. This is because in the worst case, we might have to traverse from the root to a leaf node.

# #### Space Complexity
# - **Overall**: \(O(1)\), as we are using only a few extra variables and no recursion stack is involved.