# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return 

        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            level = [] 
            n = len(queue)

            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            ans.append(level)

        return ans

# ### Intuition and Approach for `levelOrder`

# #### Intuition

# Level order traversal of a binary tree involves visiting each node level by level, from left to right. This can be efficiently achieved using a breadth-first search (BFS) strategy with the help of a queue.

# #### Approach

# 1. **Initialization**:
#    - If the tree is empty, return an empty list.
#    - Initialize a queue with the root node.

# 2. **Breadth-First Search (BFS)**:
#    - Use a queue to keep track of nodes at each level.
#    - For each level, determine the number of nodes at that level (using the length of the queue).
#    - Dequeue each node, record its value, and enqueue its left and right children (if they exist).

# 3. **Collect Results**:
#    - For each level, collect the values of the nodes and append this list to the final result list.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. Each node is processed exactly once.

# #### Space Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the tree. In the worst case, the queue can hold up to \(n\) nodes (if the tree is completely unbalanced).

