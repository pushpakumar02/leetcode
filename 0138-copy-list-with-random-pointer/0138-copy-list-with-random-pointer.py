"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: return None

        curr = head
        old_to_new = {}

        while curr:
            node = Node(curr.val) 
            old_to_new[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            new_node = old_to_new[curr] 
            new_node.next = old_to_new[curr.next] if curr.next else None
            new_node.random = old_to_new[curr.random] if curr.random else None
            curr = curr.next
            
        return old_to_new[head]

### Intuition and Approach for `copyRandomList`

#### Intuition

# To create a deep copy of a linked list where each node has an additional `random` pointer, we need to ensure that both the `next` and `random` pointers in the new list point to the correct new nodes. A straightforward way to achieve this is by using a hash map to keep track of the mapping between the original nodes and their corresponding new nodes.

#### Approach

# 1. **Edge Case**:
#    - If the head of the original list is `None`, return `None` immediately.

# 2. **Create a Hash Map**:
#    - Use a hash map `old_to_new` to map each original node to its corresponding new node.

# 3. **First Pass (Clone Nodes)**:
#    - Traverse the original list and create a new node for each original node. Store the mapping from the original node to the new node in the hash map.

# 4. **Second Pass (Set Pointers)**:
#    - Traverse the original list again. For each original node, set the `next` and `random` pointers of the corresponding new node using the hash map.

# 5. **Return the New List**:
#    - Return the new head, which is the mapped node of the original head.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the linked list. We traverse the list twice, once for cloning nodes and once for setting pointers.

# #### Space Complexity
# - **Overall**: \(O(n)\), due to the hash map used to store the mapping between original and new nodes.

# ### Summary

# - **Edge Case Handling**: Return `None` if the input list is empty.
# - **Hash Map Usage**: Use a hash map to store the mapping between original nodes and their corresponding new nodes.
# - **Two Pass Traversal**: First pass to clone nodes and store mappings, and second pass to set `next` and `random` pointers.
# - **Efficiency**: Linear time complexity and linear space complexity due to the hash map.

# This approach ensures a deep copy of the list, correctly setting both `next` and `random` pointers in the new list.



# In this code:
# - **First Pass**: Creates new nodes and stores the mapping in `old_to_new`.
# - **Second Pass**: Sets `next` and `random` pointers for the new nodes using the mappings.