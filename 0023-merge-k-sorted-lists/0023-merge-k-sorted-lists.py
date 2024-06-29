# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: return None
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeLists(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeLists(self, l1, l2):

            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next   




### Intuition and Approach

# To merge \( k \) sorted linked lists into one sorted linked list, we can use a divide-and-conquer approach. This involves repeatedly merging pairs of lists until only one list remains. This is efficient because it reduces the problem size by half in each iteration, similar to the merge step in merge sort.

# ### Steps

# 1. **Divide and Conquer**:
#    - Start with the list of \( k \) linked lists.
#    - Merge pairs of lists and reduce the list of lists by half in each iteration.
#    - Repeat until only one list remains.

# 2. **Merge Two Lists**:
#    - Use a helper function to merge two sorted linked lists into one sorted list.
#    - This helper function is similar to the merge step in the merge sort algorithm for arrays.

# ### Complexity

# - **Time Complexity**: \( O(N \log k) \)
#   - \( N \) is the total number of nodes in all lists.
#   - Merging two lists takes \( O(N) \) time and we perform the merge operation \( \log k \) times.
  
# - **Space Complexity**: \( O(1) \)
#   - We are only using a few extra pointers.

# ### Implementation

# Here's the code for the approach described:

# ```python
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists or len(lists) == 0:
#             return None
        
#         while len(lists) > 1:
#             mergedList = []
#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 l2 = lists[i + 1] if (i + 1) < len(lists) else None
#                 mergedList.append(self.mergeLists(l1, l2))
#             lists = mergedList
#         return lists[0]

#     def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next
        
#         if l1:
#             tail.next = l1
#         if l2:
#             tail.next = l2
        
#         return dummy.next
# ```

# ### Explanation

# 1. **mergeKLists**:
#    - If the input list is empty or contains no lists, return `None`.
#    - While there is more than one list in `lists`, merge pairs of lists using the `mergeLists` helper function.
#    - After each round of merging, update `lists` to the list of merged lists.
#    - Finally, return the single merged list.

# 2. **mergeLists**:
#    - Initialize a dummy node to help with the merge process.
#    - Use a `tail` pointer to build the new merged list.
#    - Compare the current nodes of `l1` and `l2`, appending the smaller node to the `tail`.
#    - Move the pointer of the list from which the node was taken.
#    - Once one of the lists is exhausted, append the remaining nodes of the other list.
#    - Return the merged list starting from the node after the dummy node.