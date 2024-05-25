class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

### Intuition and Approach for `findDuplicate`

#### Intuition

# The problem of finding the duplicate number in an array where the numbers range from 1 to \( n \) and there is exactly one duplicate can be effectively solved using Floyd's Tortoise and Hare algorithm (cycle detection). This method leverages the properties of the array to detect a cycle, where the duplicate number forms the cycle.

#### Approach

# 1. **Initialize Pointers**:
#    - Start with two pointers, `fast` and `slow`, both initialized to the first element of the array (`index 0`).

# 2. **Detect Cycle**:
#    - Move the `slow` pointer one step at a time (`slow = nums[slow]`).
#    - Move the `fast` pointer two steps at a time (`fast = nums[nums[fast]]`).
#    - Continue this process until the `slow` and `fast` pointers meet, indicating the presence of a cycle.

# 3. **Find Entry Point of Cycle**:
#    - Once a cycle is detected, initialize a new pointer `slow2` to the beginning of the array (`index 0`).
#    - Move both `slow` and `slow2` pointers one step at a time until they meet. The meeting point is the duplicate number.

#### Time Complexity
# - **Overall**: \(O(n)\), where \(n\) is the length of the array. The pointers traverse the array linearly.

#### Space Complexity
# - **Overall**: \(O(1)\), as the algorithm uses a constant amount of extra space.

### Summary

# - **Cycle Detection**: Uses the properties of the array to detect a cycle.
# - **Floyd's Algorithm**: Effective in finding the duplicate number by treating the problem as a linked list cycle detection.
# - **Pointer Movement**: First phase detects the cycle, and the second phase finds the entry point of the cycle, which is the duplicate number.

# This method ensures that the duplicate number is found efficiently with minimal space usage.