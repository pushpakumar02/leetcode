# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root: return 0

            left_height = height(root.left)
            if balanced[0] is False:
                return 0

            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0

            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0] 


### Intuition and Approach for `isBalanced`

#### Intuition

# A binary tree is considered balanced if the heights of the two child subtrees of any node differ by no more than one. To determine if the tree is balanced, we need to ensure this condition holds for every node in the tree.

# #### Approach

# 1. **Height Calculation with Balance Check**:
#    - Use a helper function `height` to calculate the height of each node.
#    - While calculating the height, also check if the subtree rooted at the node is balanced.

# 2. **Early Stopping**:
#    - If any subtree is found to be unbalanced, propagate this information up the recursive calls and terminate further unnecessary computations.

# 3. **Global Variable**:
#    - Use a list with one element, `balanced`, to keep track of whether the tree is balanced. This allows the helper function to update the balance status.

# 4. **Recursive Function**:
#    - Calculate the height of the left and right subtrees.
#    - If the difference in height is greater than 1, mark the tree as unbalanced.
#    - Return the height of the subtree.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. Each node is visited exactly once.

# #### Space Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the tree. This accounts for the space used by the recursion stack. In the worst case (a completely unbalanced tree), \(h\) could be \(n\); in the best case (a completely balanced tree), \(h\) is \(\log n\).