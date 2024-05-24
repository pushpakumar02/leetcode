# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            current.next = ListNode(total % 10)
            carry = total // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return head.next

### Intuition and Approach for `addTwoNumbers`

#### Intuition

# Adding two numbers represented by linked lists involves handling each digit's sum, managing carries, and moving to the next nodes. This is similar to the process of adding numbers manually from right to left, digit by digit, while keeping track of the carry.

#### Approach

# 1. **Initialize a Dummy Node**:
#    - Start with a dummy node to simplify the process of building the result linked list.
#    - Use a `current` pointer initialized to the dummy node.

# 2. **Initialize a Carry**:
#    - Initialize a variable `carry` to keep track of any carry-over during the addition of digits.

# 3. **Traverse Both Lists**:
#    - Iterate through both linked lists until both are exhausted and no carry is left.
#    - For each node, add the corresponding digits from both lists along with any carry from the previous addition.

# 4. **Handle Digits and Carry**:
#    - Calculate the new digit to be added to the result list (`total % 10`).
#    - Update the carry for the next iteration (`total // 10`).

# 5. **Move Pointers**:
#    - Advance the pointers for `l1`, `l2`, and `current` to their respective next nodes.
#    - If any list is shorter, treat the missing value as 0.

# 6. **Return the Result**:
#    - The result is stored starting from the next node of the dummy node, which helps in handling edge cases cleanly.

# #### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the maximum length of the two linked lists. Each node is processed exactly once.

# #### Space Complexity
# - **Overall**: \(O(n)\), for storing the result linked list, which requires a new node for each digit.

# ### Summary

# - **Dummy Node**: Simplifies list construction.
# - **Carry Handling**: Ensures proper addition with carry-over.
# - **Pointer Management**: Advances through the lists and constructs the result.
# - **Edge Cases**: Handles different lengths and final carry efficiently.

