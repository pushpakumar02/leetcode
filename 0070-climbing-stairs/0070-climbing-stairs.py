class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

### Intuition
# To solve the problem of finding the number of distinct ways to climb a staircase with `n` steps, where you can take either 1 or 2 steps at a time, we can recognize that this is essentially a Fibonacci sequence problem. 

# ### Approach
# - **Dynamic Programming**: We can use two variables to keep track of the number of ways to reach the current step and the previous step. The idea is to use these two variables to iteratively calculate the number of ways to reach the top.
#   - Initialize two variables, `one` and `two`, both set to 1. `one` represents the number of ways to reach the current step, and `two` represents the number of ways to reach the previous step.
#   - For each step from 2 to `n`, update `one` and `two` by summing the two previous values.
#   - Return `one`, which will hold the number of ways to reach the nth step.

# ### Time Complexity
# - **Time**: \(O(n)\). We iterate from 2 to `n`, performing a constant amount of work each iteration.

# ### Space Complexity
# - **Space**: \(O(1)\). We use a fixed amount of extra space regardless of the input size.

