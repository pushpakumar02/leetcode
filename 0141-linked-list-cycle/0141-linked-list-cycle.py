# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                return True
        return False

### Intuition and Approach for `hasCycle`

#### Intuition

# To determine if a linked list has a cycle, we can use Floyd's Tortoise and Hare algorithm, which uses two pointers moving at different speeds. The idea is that if there is a cycle in the list, the faster-moving pointer will eventually meet the slower-moving pointer.

#### Approach

# 1. **Initialize Pointers**:
#    - Use two pointers, `slow` and `fast`, both starting at the head of the linked list.
#    - `slow` moves one step at a time (`slow = slow.next`).
#    - `fast` moves two steps at a time (`fast = fast.next.next`).

# 2. **Traverse the List**:
#    - Iterate through the list with a `while` loop that continues as long as `fast` and `fast.next` are not null. This ensures that the `fast` pointer does not reach the end of the list and cause a null pointer exception.
#    - In each iteration, move `slow` one step and `fast` two steps forward.

# 3. **Cycle Detection**:
#    - If at any point `slow` and `fast` pointers meet (i.e., `slow == fast`), it indicates that there is a cycle in the linked list.
#    - If the loop ends without the pointers meeting, then there is no cycle in the list.

# 4. **Return Result**:
#    - Return `True` if a cycle is detected (pointers meet).
#    - Return `False` if no cycle is found (pointers do not meet).

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the number of nodes in the linked list. In the worst case, the `fast` pointer traverses the list twice as fast as the `slow` pointer, leading to a linear time complexity.

# #### Space Complexity
# - **Overall**: \(O(1)\), since only a constant amount of extra space is used for the two pointers.

# ### Summary

# - **Initialization**: Set two pointers (`slow` and `fast`) to the head of the list.
# - **Traversal**: Move `slow` by one step and `fast` by two steps in each iteration.
# - **Detection**: Check if the `slow` and `fast` pointers meet, indicating a cycle.
# - **Efficiency**: The algorithm operates in linear time with constant space, making it efficient for cycle detection in linked lists.