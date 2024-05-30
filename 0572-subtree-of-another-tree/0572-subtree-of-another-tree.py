# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            if not p and not q: return True

            if (not p and q) or ( p and not q):
                return False

            if p.val != q.val:
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def subTree(root):

            if not root: return False

            if sameTree(root, subRoot):
                return True

            return subTree(root.left) or subTree(root.right)

        return subTree(root)



### Intuition and Approach for `isSubtree`

#### Intuition

# To determine if `subRoot` is a subtree of `root`, we need to verify that `subRoot` is identical to some subtree within `root`. A subtree of a binary tree `T` is a tree `S` consisting of a node in `T` and all of that node's descendants. The subtree `S` must have exactly the same structure and node values as `subRoot`.

# #### Approach

# 1. **Helper Function for Identical Trees**:
#    - Define a helper function `sameTree` that checks if two trees are identical.
#    - Trees are identical if:
#      - Both are `None`.
#      - Both are not `None` and their root values are the same, and their left and right subtrees are also identical.

# 2. **Recursive Traversal**:
#    - Traverse the main tree `root` using another helper function `subTree`.
#    - At each node in `root`, check if the subtree starting from this node is identical to `subRoot` using `sameTree`.
#    - If not, recursively check the left and right subtrees of the current node.

# 3. **Base Cases**:
#    - If `root` becomes `None`, it means we have traversed a branch without finding `subRoot`, so return `False`.
#    - If `sameTree` returns `True`, it means the current subtree is identical to `subRoot`, so return `True`.

# #### Time Complexity
# - **Overall**: \(O(m \times n)\), where \(m\) is the number of nodes in `root` and \(n\) is the number of nodes in `subRoot`. This is because in the worst case, for each node in `root`, we might check all nodes in `subRoot`.

# #### Space Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the main tree `root`. This accounts for the space used by the recursion stack.


# This implementation defines two helper functions: `sameTree` to check if two trees are identical and `subTree` to recursively check each subtree of `root` to see if it matches `subRoot`. This ensures that we correctly identify if `subRoot` is a subtree of `root`.