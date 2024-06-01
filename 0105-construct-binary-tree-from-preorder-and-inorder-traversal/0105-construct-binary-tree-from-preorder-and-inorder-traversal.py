# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder and not inorder: return None

        root = TreeNode(preorder[0])  
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1: ])

        return root

### Intuition and Approach for `buildTree`

#### Intuition

# To construct a binary tree from its preorder and inorder traversals:
# - **Preorder Traversal**: The first element is always the root of the tree/subtree.
# - **Inorder Traversal**: The elements to the left of the root element in the inorder list are the nodes of the left subtree, and the elements to the right are the nodes of the right subtree.

# By recursively finding the root from the preorder list and partitioning the inorder list into left and right subtrees, we can construct the entire tree.

#### Approach

# 1. **Base Case**:
#    - If either `preorder` or `inorder` list is empty, return `None`.

# 2. **Root Identification**:
#    - The first element of the `preorder` list is the root of the current subtree.

# 3. **Partitioning**:
#    - Find the index of the root element in the `inorder` list. This index divides the list into the left and right subtrees.

# 4. **Recursive Construction**:
#    - Recursively construct the left subtree using the next `mid` elements from the `preorder` list and the left part of the `inorder` list.
#    - Recursively construct the right subtree using the remaining elements from the `preorder` list and the right part of the `inorder` list.

# 5. **Return the Tree**:
#    - Attach the constructed left and right subtrees to the root node.

# #### Time Complexity
# - **Overall**: \(O(n^2)\) in the worst case, as each call to find the root index in the inorder list takes \(O(n)\) time, and this is done for each of the \(n\) nodes.

# #### Space Complexity
# - **Overall**: \(O(n)\) due to the recursion stack and the space needed to store the tree nodes.
