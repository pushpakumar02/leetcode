# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            maxLeft = dfs(root.left)
            maxRight =  dfs(root.right)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            res[0] = max(res[0] , root.val + maxLeft + maxRight)
            return root.val + max(maxLeft , maxRight)

        dfs(root)
        return res[0]



### Intuition and Approach

# To find the maximum path sum in a binary tree, we need to consider different cases for paths:

# 1. **Root-to-Leaf Path**:
#    - The path can end at any node, not necessarily a leaf.

# 2. **Path Through Any Node**:
#    - The path can include any subtree of a node.

# To handle this, we perform a Depth-First Search (DFS) on the tree. For each node, we calculate:
# - The maximum path sum that includes the node itself and possibly extends to one of its subtrees.
# - The potential maximum path sum that passes through the node and includes both left and right subtrees (for updating the global maximum).

# ### Steps:
# 1. **DFS Traversal**:
#    - Traverse the tree using DFS.
#    - For each node, compute the maximum path sum of its left and right subtrees.
#    - If a subtree's maximum path sum is negative, consider it as 0 (since we can choose not to include it).

# 2. **Update Global Maximum**:
#    - For each node, calculate the sum of the node's value and the maximum path sums of its left and right subtrees.
#    - Update the global maximum path sum if this value is higher.

# 3. **Return Value for Recursion**:
#    - For the recursion, return the maximum path sum of the current node extended to one of its subtrees.

# ### Complexity:
# - **Time Complexity**: \(O(N)\), where \(N\) is the number of nodes in the tree, since we traverse each node once.
# - **Space Complexity**: \(O(H)\), where \(H\) is the height of the tree, which accounts for the recursion stack.

# ### Implementation:

# ```python
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         res = [root.val]

#         def dfs(node):
#             if not node:
#                 return 0
            
#             # Recursively find the maximum path sum for left and right subtrees
#             maxLeft = dfs(node.left)
#             maxRight = dfs(node.right)
            
#             # Ignore paths with negative sums, since we are looking for maximum sum
#             maxLeft = max(maxLeft, 0)
#             maxRight = max(maxRight, 0)

#             # Update the global maximum path sum including the current node
#             res[0] = max(res[0], node.val + maxLeft + maxRight)
            
#             # Return the maximum path sum extending to one of the subtrees
#             return node.val + max(maxLeft, maxRight)

#         dfs(root)
#         return res[0]
# ```

# ### Explanation:
# 1. **Initialization**:
#    - `res` is initialized to contain the value of the root node. This will keep track of the global maximum path sum.

# 2. **DFS Function**:
#    - `dfs` is a recursive helper function that calculates the maximum path sum for each subtree.
#    - If the current node is `None`, return 0 (base case).
#    - Calculate the maximum path sum for the left and right subtrees.
#    - Update the global maximum path sum if the current node's path sum (including both subtrees) is greater than the current global maximum.
#    - Return the maximum path sum for the current node extended to one of its subtrees.

# 3. **Final Result**:
#    - The `maxPathSum` function calls `dfs` and returns the global maximum path sum stored in `res[0]`.