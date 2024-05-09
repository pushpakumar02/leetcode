# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev


# Intuition:
# - To reverse a linked list, we need to change the direction of the pointers such that each node's next pointer points to its previous node.

# Approach:
# - We initialize two pointers: `prev` and `curr`.
#   - `prev` initially points to `None`.
#   - `curr` initially points to the `head` of the linked list.
# - We iterate through the linked list:
#   - We store the next node of `curr` in a temporary variable `nxt`.
#   - We update the `next` pointer of `curr` to point to its previous node, which is `prev`.
#   - We move `prev` to `curr`.
#   - We move `curr` to `nxt`.
# - We continue this process until we reach the end of the linked list (i.e., `curr` becomes `None`).
# - Finally, we return `prev`, which now points to the new head of the reversed linked list.

# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse each node once.

# Space Complexity: O(1). We use a constant amount of extra space regardless of the input size.

