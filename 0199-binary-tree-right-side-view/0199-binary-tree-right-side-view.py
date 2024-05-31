# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        queue = [root]
        res = []
        level = []

        while queue != []:
            for node in queue: 
                    if node.left:   
                        level.append(node.left)
                    if node.right:
                        level.append(node.right)
            res.append(node.val)
            queue = level
            level = []

        return res

### Intuition and Approach for `rightSideView`

#### Intuition

# The problem requires us to return the values of the nodes that are visible when the binary tree is viewed from the right side. This means for each level of the tree, we need to capture the rightmost node.

# #### Approach

# 1. **Initialization**:
#    - If the tree is empty, return an empty list.
#    - Initialize a queue with the root node to start the level order traversal.

# 2. **Breadth-First Search (BFS)**:
#    - Use a queue to perform BFS, keeping track of nodes at each level.
#    - For each level, keep track of the last node encountered.
#    - At the end of each level, add the value of the last node encountered to the result list.

# 3. **Collect Results**:
#    - For each level, collect the rightmost node's value and append it to the result list.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. Each node is processed exactly once.

# #### Space Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. In the worst case, the queue can hold up to \(n\) nodes (if the tree is completely unbalanced).