# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]

        def height(root):
            if root is None: return 0

            left_height = height(root.left)
            right_height = height(root.right)
            diameter = (left_height + right_height)

            largest_diameter[0] = max(largest_diameter[0], diameter)

            return 1 + max(left_height, right_height)

        height(root)
        return largest_diameter[0]

### Intuition and Approach for `diameterOfBinaryTree`

#### Intuition

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. To determine the diameter, we need to consider the path that spans the longest distance in terms of the number of nodes from one leaf node to another.

#### Approach

# 1. **Height Calculation**:
#    - The height of a node is the number of edges on the longest path from the node to a leaf.
#    - The diameter at a given node is the sum of the heights of its left and right subtrees.
# 2. **Recursive Function**:
#    - Create a helper function `height` that calculates the height of the tree rooted at the given node.
#    - While calculating the height, update the largest diameter encountered.
# 3. **Updating Diameter**:
#    - For each node, calculate the potential diameter by adding the heights of its left and right subtrees.
#    - Keep track of the maximum diameter encountered during the traversal.
# 4. **Global Variable**:
#    - Use a mutable container (like a list) to keep track of the largest diameter found so far, as this value needs to be updated within the recursive calls.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. Each node is visited once.

# #### Space Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the tree. This accounts for the space used by the recursion stack. In the worst case (a completely unbalanced tree), \(h\) could be \(n\); in the best case (a completely balanced tree), \(h\) is \(\log n\).
            