class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                temp, tempind = stack.pop()
                res[tempind] = (i - tempind)
            stack.append([t, i])
        return res



# Intuition:
# - We want to find the number of days we need to wait until a warmer temperature. This can be solved using a stack to store the temperatures and their indices.

# Approach:
# - We iterate through the temperatures along with their indices.
# - We maintain a stack where we store temperatures and their corresponding indices.
# - While iterating, for each temperature `t`:
#   - We check if the stack is not empty and the current temperature is greater than the temperature at the top of the stack.
#   - If yes, it means the current temperature is warmer than the temperatures stored in the stack. So, we pop the temperatures from the stack and calculate the number of days by subtracting their indices from the current index. We update the result accordingly.
#   - We continue this process until the stack is empty or the current temperature is not warmer than the top of the stack.
# - Finally, we push the current temperature and its index onto the stack.
# - We return the result list which stores the number of days you would have to wait until a warmer temperature for each day.

# Time Complexity: O(n), where n is the number of temperatures. We traverse the list of temperatures only once.

# Space Complexity: O(n), where n is the number of temperatures. In the worst-case scenario, the stack can store all the temperatures.