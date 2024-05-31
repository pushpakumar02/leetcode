# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, min, max):
            if not node:
                return True

            if node.val <= min or node.val >= max:
                return False

            return valid(node.left, min, node.val ) and  valid(node.right, node.val, max) 

        return valid(root, float('-inf'), float('inf'))


### Intuition and Approach for `isValidBST`

# #### Intuition

# A binary search tree (BST) is defined as a binary tree in which for every node:
# - All nodes in the left subtree have values less than the node's value.
# - All nodes in the right subtree have values greater than the node's value.

# To verify if a binary tree is a BST, we can utilize the properties of a BST and ensure that every node adheres to the constraints provided by its parent nodes.

# #### Approach

# 1. **Recursive Validation**:
#    - Use a helper function that takes a node and two boundaries (`min` and `max`).
#    - Initially, the boundaries are set to negative infinity (`-inf`) and positive infinity (`+inf`).

# 2. **Node Validation**:
#    - For each node, check if its value lies within the valid range (`min < node.val < max`).
#    - If the node value violates this range, return `False`.

# 3. **Update Boundaries**:
#    - Recursively check the left and right subtrees.
#    - For the left subtree, update the `max` boundary to the current node's value.
#    - For the right subtree, update the `min` boundary to the current node's value.

# 4. **Termination**:
#    - If a leaf node is reached (i.e., `node is None`), return `True` as a leaf node does not violate the BST properties.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. Each node is visited exactly once.

# #### Space Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the tree. This is due to the recursive call stack.

