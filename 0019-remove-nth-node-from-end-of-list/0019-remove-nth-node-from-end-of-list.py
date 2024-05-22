# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head
        ahead = behind = dummy

        for _ in range(n+1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next
        return dummy.next



### Intuition and Approach for `removeNthFromEnd`

#### Intuition

# To remove the nth node from the end of a linked list, we can use a two-pointer technique with a dummy node to handle edge cases (such as removing the first node). The idea is to position two pointers such that they maintain a gap of \(n\) nodes between them, allowing the first pointer to reach the end of the list while the second pointer reaches the node just before the one to be removed.

#### Approach

# 1. **Initialize Dummy Node**:
#    - Create a dummy node and point its `next` to the head of the list. This helps handle edge cases seamlessly.

# 2. **Set Up Pointers**:
#    - Initialize two pointers, `ahead` and `behind`, both pointing to the dummy node.

# 3. **Advance Ahead Pointer**:
#    - Move the `ahead` pointer \(n+1\) steps forward to ensure a gap of \(n\) nodes between the `ahead` and `behind` pointers.

# 4. **Traverse the List**:
#    - Move both pointers one step at a time until the `ahead` pointer reaches the end of the list. At this point, the `behind` pointer will be at the node just before the one to be removed.

# 5. **Remove the Node**:
#    - Adjust the `next` pointer of the `behind` pointer to skip the node to be removed.

# 6. **Return the Result**:
#    - Return the `next` of the dummy node, which points to the head of the modified list.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the linked list. Each pointer traverses the list at most once.

# #### Space Complexity
# - **Overall**: \(O(1)\), as only a constant amount of extra space is used for the pointers and dummy node.

# ### Summary

# - **Dummy Node**: Use a dummy node to simplify handling edge cases.
# - **Two-Pointer Technique**: Maintain a gap of \(n\) nodes between the `ahead` and `behind` pointers.
# - **Single Pass**: Achieve the result in a single traversal of the list.
# - **Efficiency**: The approach is linear in time and constant in space, making it efficient for the given problem.

# This method effectively removes the nth node from the end of the linked list using the two-pointer technique.