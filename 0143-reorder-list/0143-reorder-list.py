# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque 
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next: return 

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second.next = None
        second = slow.next
        slow.next = prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 





### Intuition and Approach

# To reorder a linked list in the desired format, we can follow a three-step process:
# 1. **Find the middle of the linked list** using the slow and fast pointer technique.
# 2. **Reverse the second half** of the list.
# 3. **Merge the two halves** by alternating nodes from each half.

# ### Steps and Approach

# 1. **Find the middle of the linked list**:
#    - Use two pointers, `slow` and `fast`. Move `slow` one step at a time and `fast` two steps at a time. When `fast` reaches the end, `slow` will be at the middle.
   
# 2. **Reverse the second half**:
#    - Starting from the node after the `slow` pointer, reverse the second half of the list.
   
# 3. **Merge the two halves**:
#    - Interleave nodes from the first half and the reversed second half.

# ### Complexity

# - **Time Complexity**: \(O(n)\) because we traverse the list a constant number of times.
# - **Space Complexity**: \(O(1)\) because we only use a few pointers and do not require additional data structures.

# ### Implementation

# Here's the code for the approach described:

# ```python
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         if not head or not head.next:
#             return 
        
#         # Step 1: Find the middle of the linked list
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         # Step 2: Reverse the second half of the linked list
#         second = slow.next
#         slow.next = None  # Split the list into two halves
#         prev = None
#         while second:
#             tmp = second.next
#             second.next = prev
#             prev = second
#             second = tmp
        
#         # Step 3: Merge the two halves
#         first, second = head, prev
#         while second:
#             tmp1, tmp2 = first.next, second.next
#             first.next = second
#             second.next = tmp1
#             first, second = tmp1, tmp2
# ```

# ### Explanation

# 1. **Finding the middle**:
#    - Initialize `slow` to `head` and `fast` to `head.next`.
#    - Move `slow` one step and `fast` two steps until `fast` can't move twice.

# 2. **Reversing the second half**:
#    - Use a `prev` pointer to reverse the nodes starting from `slow.next`.
#    - Move each node to the front of the reversed list until all nodes are reversed.

# 3. **Merging the two halves**:
#    - Interleave nodes from `head` and the reversed second half.
#    - Use two pointers, `first` for the first half and `second` for the reversed second half.
#    - Alternate the nodes by updating the `next` pointers accordingly.
