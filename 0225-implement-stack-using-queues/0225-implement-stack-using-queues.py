class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Intuition and Approach:

# - We're implementing a stack using a queue.
# - We use a deque (double-ended queue) to mimic the behavior of a stack.
# - For `push`, we simply append elements to the queue.
# - For `pop`, since a queue is a FIFO (first-in-first-out) structure, we want to simulate the LIFO (last-in-first-out) behavior of a stack.
#   - To achieve this, when we pop an element, we move all the elements from the front of the queue to the rear, except for the last element.
#   - Then we return and remove this last element, effectively mimicking the behavior of a stack.
# - For `top`, we simply return the last element of the queue.
# - For `empty`, we check if the queue is empty.

# Time Complexity:
# - `push`: O(1) - Appending to a deque is O(1).
# - `pop`: O(n) - In the worst case, we have to move all elements except the last one to mimic the stack behavior, which takes O(n).
# - `top`: O(1) - Accessing the last element of a deque is O(1).
# - `empty`: O(1) - Checking if a deque is empty is O(1).

# Space Complexity: O(n) - where n is the number of elements in the queue. In the worst case, the queue contains all elements of the stack.