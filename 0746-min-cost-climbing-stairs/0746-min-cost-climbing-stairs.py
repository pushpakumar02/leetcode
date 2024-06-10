class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1] , cost[i + 2])
        return min(cost[0], cost[1])

# ### Intuition
# To determine the minimum cost to reach the top of the staircase where you can either start from the 0th step or the 1st step, and you can either take one or two steps at a time, a dynamic programming approach can be used to find the optimal solution. 

# ### Approach
# - **Dynamic Programming**: We start from the end of the list and work our way to the beginning. We update each step with the minimum cost required to get to the top from that step.
#   - Append a `0` to the `cost` list to represent the cost of reaching the top.
#   - Traverse the list backwards starting from the third last element to the first.
#   - For each element, update it by adding the minimum of the costs of the next one or two steps ahead.
#   - Finally, the minimum cost to start from either of the first two steps is the answer.

# ### Time Complexity
# - **Time**: \(O(n)\). We iterate through the list once.

# ### Space Complexity
# - **Space**: \(O(1)\). We modify the list in place and use only a constant amount of extra space.

# ### Implementation
# - **Initialization**: Append a `0` to the `cost` list.
# - **Iteration**: Traverse the list from the third last element to the first, updating each element with the minimum of the costs of the next one or two steps.
# - **Result**: The minimum of the first two elements gives the minimum cost to reach the top.