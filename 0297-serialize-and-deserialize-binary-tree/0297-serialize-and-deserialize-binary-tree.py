# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        val = data.split(",")
        self.i = 0

        def dfs():
            if val[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(val[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()            
            return node
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))





### Intuition and Approach

# To serialize and deserialize a binary tree, we can use Depth-First Search (DFS). The idea is to perform a pre-order traversal (node, left, right) and convert the tree into a string where each value is separated by a delimiter (e.g., comma). For `None` nodes, we use a placeholder (e.g., "N").

# ### Serialization:
# - Traverse the tree in a pre-order manner.
# - Append each node's value to a result list.
# - For `None` nodes, append "N".
# - Join the list into a single string with commas separating the values.

# ### Deserialization:
# - Split the serialized string by the delimiter to get a list of values.
# - Use a recursive function to reconstruct the tree using the list:
#   - Start from the beginning of the list.
#   - For each value, create a new TreeNode.
#   - If the value is "N", return `None`.
#   - Recurse for left and right children.

# ### Complexity:
# - **Time Complexity**: \(O(N)\) for both serialization and deserialization, where \(N\) is the number of nodes in the tree.
# - **Space Complexity**: \(O(N)\) for storing the serialized string and during recursion stack in deserialization.

# ### Implementation:

# ```python
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string."""
#         res = []

#         def dfs(node):
#             if not node:
#                 res.append("N")
#                 return
#             res.append(str(node.val))
#             dfs(node.left)
#             dfs(node.right)
        
#         dfs(root)
#         return ",".join(res)
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree."""
#         values = data.split(",")
#         self.i = 0

#         def dfs():
#             if values[self.i] == "N":
#                 self.i += 1
#                 return None
#             node = TreeNode(int(values[self.i]))
#             self.i += 1
#             node.left = dfs()
#             node.right = dfs()
#             return node
        
#         return dfs()

# # Your Codec object will be instantiated and called as such:
# # ser = Codec()
# # deser = Codec()
# # ans = deser.deserialize(ser.serialize(root))
# ```

# ### Explanation:

# 1. **Serialization**:
#    - `res` is a list to collect the serialized values.
#    - `dfs(node)` is a helper function to traverse the tree in pre-order.
#      - If `node` is `None`, append "N" to `res`.
#      - Otherwise, append the node's value, then recurse for left and right children.
#    - After the traversal, join `res` with commas to form a single string.

# 2. **Deserialization**:
#    - `values` is a list of values obtained by splitting the serialized string.
#    - `self.i` is an index to keep track of the current position in `values`.
#    - `dfs()` is a helper function to reconstruct the tree:
#      - If the current value is "N", increment `self.i` and return `None`.
#      - Otherwise, create a new TreeNode with the current value, then recurse for left and right children.
#      - Finally, return the reconstructed node.

# This approach ensures the correct reconstruction of the original tree structure from the serialized string.