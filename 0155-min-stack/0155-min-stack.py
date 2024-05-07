class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




# Intuition:

# - We need to design a stack that supports push, pop, top, and retrieving the minimum element in constant time, all in O(1) complexity.

# Approach:
# - We can achieve this by using two stacks:
#   1. **Main Stack:** This stack stores all elements pushed into the stack.
#   2. **Min Stack:** This stack stores the minimum element encountered up to the current position in the main stack.
# - When pushing a new element:
#   - We push the element into the main stack as usual.
#   - We also maintain the minimum element by comparing the new element with the top element of the min stack. If it's smaller, we push the new element into the min stack; otherwise, we duplicate the top element of the min stack.
# - When popping an element:
#   - We pop an element from both the main stack and the min stack, ensuring both stacks remain in sync.
# - When retrieving the top element:
#   - We simply return the top element of the main stack.
# - When retrieving the minimum element:
#   - We return the top element of the min stack.
  
# Time Complexity:
# - **Push, Pop, Top, GetMin:** O(1) for each operation. These operations involve only stack manipulations, which are O(1) operations.

# Space Complexity:
# - O(n), where n is the number of elements in the main stack. Both the main stack and the min stack can potentially store all elements pushed into the stack. However, the space complexity for both stacks is essentially the same because they grow together.
