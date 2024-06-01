# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

### Intuition and Approach for `kthSmallest`

#### Intuition

# To find the \(k\)th smallest element in a Binary Search Tree (BST), we can take advantage of the properties of the BST:
# - The in-order traversal of a BST yields the nodes in ascending order.

# Thus, by performing an in-order traversal and counting the nodes as we visit them, we can directly obtain the \(k\)th smallest element.

#### Approach

# 1. **In-order Traversal**:
#    - Use a stack to simulate the in-order traversal iteratively.
#    - Traverse to the leftmost node while pushing nodes onto the stack.
#    - Once the leftmost node is reached, start popping from the stack, which represents visiting nodes in ascending order.

# 2. **Count Nodes**:
#    - Maintain a counter to keep track of the number of nodes visited during the in-order traversal.
#    - When the counter reaches \(k\), the current node is the \(k\)th smallest element.

# 3. **Termination**:
#    - The traversal and counting continue until the \(k\)th smallest element is found, at which point the value is returned.

# #### Time Complexity
# - **Overall**: \(O(k)\). In the worst case, we might need to traverse \(k\) nodes to find the \(k\)th smallest element.

# #### Space Complexity
# - **Overall**: \(O(h)\), where \(h\) is the height of the tree. This is due to the stack that stores the nodes during traversal, which at most will be the height of the tree.

