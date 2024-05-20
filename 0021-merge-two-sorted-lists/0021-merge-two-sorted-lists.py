# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        curr = d

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        curr.next = list1 if list1 else list2
        
        return d.next

### Intuition and Approach for `mergeTwoLists`

#### Intuition

# Merging two sorted linked lists involves creating a new sorted linked list by comparing the nodes of the two input lists one by one and linking them in sorted order. This can be efficiently done using a two-pointer approach, iterating through both lists simultaneously and picking the smaller node each time.

#### Approach

# 1. **Dummy Node**:
#    - Initialize a dummy node (`d`) to act as a starting point for the merged list. This helps to easily return the head of the merged list later.
#    - Initialize a current pointer (`curr`) starting at the dummy node, which will help in constructing the new list.

# 2. **Two Pointers**:
#    - Use two pointers, `list1` and `list2`, to traverse the two input lists.
#    - Compare the values at the current nodes of both lists:
#      - If `list1.val` is less than `list2.val`, set `curr.next` to `list1`, move `curr` to `list1`, and advance `list1`.
#      - Otherwise, set `curr.next` to `list2`, move `curr` to `list2`, and advance `list2`.

# 3. **Remaining Nodes**:
#    - Once one of the lists is fully traversed, link the remaining part of the other list to `curr.next`.
#    - This is because the remaining nodes are already sorted.

# 4. **Return the Result**:
#    - The merged list starts from `d.next` (since `d` is a dummy node).

# #### Time Complexity
# - **Overall**: \(O(n + m)\), where \(n\) is the number of nodes in `list1` and \(m\) is the number of nodes in `list2`. Each node is processed exactly once.

# #### Space Complexity
# - **Overall**: \(O(1)\), aside from the space required for the input lists. The solution uses a constant amount of additional space.

# ### Summary

# - **Initialization**: Create a dummy node to facilitate the merging process.
# - **Merging**: Use two pointers to iterate through the input lists and link nodes in sorted order.
# - **Completion**: Attach any remaining nodes from the non-empty list to the merged list.
# - **Efficiency**: This approach is efficient, with linear time complexity and constant space complexity.

# This method ensures that the two sorted lists are merged into a single sorted list efficiently.