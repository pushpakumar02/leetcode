# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)

            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr





### Intuition and Approach

# The goal is to reverse nodes of the linked list in groups of size \( k \) and return the modified list. To achieve this, we can follow these steps:

# 1. **Dummy Node**: 
#    - Use a dummy node to simplify edge cases, especially handling the head of the list.
   
# 2. **Identify Group of k Nodes**:
#    - Use a helper function to find the \( k \)-th node from the current position.
#    - If a group of size \( k \) exists, proceed to reverse it; otherwise, exit the loop.

# 3. **Reverse the k Nodes**:
#    - Reverse the nodes within the group while maintaining pointers to the previous and next nodes to reconnect the reversed segment correctly.

# 4. **Reattach Reversed Groups**:
#    - After reversing the group, adjust the pointers to connect the reversed group with the rest of the list.

# 5. **Repeat Until End**:
#    - Continue the process until no more complete groups of \( k \) nodes are found.

# ### Complexity

# - **Time Complexity**: \( O(N) \), where \( N \) is the number of nodes in the list. Each node is visited a constant number of times.
# - **Space Complexity**: \( O(1) \), since we are only using a few extra pointers.

# ### Implementation

# Here is the Python implementation of the approach:

# ```python
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         dummy = ListNode(0, head)
#         groupPrev = dummy

#         while True:
#             kth = self.getKth(groupPrev, k)
#             if not kth:
#                 break
#             groupNext = kth.next

#             # Reverse the group
#             prev, curr = groupNext, groupPrev.next
#             while curr != groupNext:
#                 tmp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = tmp
            
#             tmp = groupPrev.next
#             groupPrev.next = kth
#             groupPrev = tmp

#         return dummy.next

#     def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
#         while curr and k > 0:
#             curr = curr.next
#             k -= 1
#         return curr
# ```

# ### Explanation

# 1. **reverseKGroup**:
#    - A dummy node is used to simplify handling of the head.
#    - `groupPrev` is initialized to the dummy node.
#    - In a loop, find the \( k \)-th node from `groupPrev`.
#    - If \( k \)-th node exists (`kth` is not `None`), reverse the nodes in the group.
#    - Adjust pointers to reconnect the reversed group.
#    - Update `groupPrev` to the end of the newly reversed group.
#    - Repeat until no more complete groups of \( k \) nodes are found.

# 2. **getKth**:
#    - A helper function to find the \( k \)-th node starting from `curr`.
#    - It returns `None` if fewer than \( k \) nodes are left.

# This solution ensures that the nodes in the linked list are reversed in groups of \( k \), and the remaining nodes (if fewer than \( k \)) are left unchanged.