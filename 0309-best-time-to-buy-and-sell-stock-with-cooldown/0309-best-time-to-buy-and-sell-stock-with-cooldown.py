class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = dfs(i + 1, not buying) - prices[i] 
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
            
        return dfs(0, True)


### Intuition
# To maximize the profit from stock prices where you are allowed to buy and sell with a cooldown period of one day after selling, we can use dynamic programming to explore all possible actions at each day and choose the one that maximizes the profit. We will use a memoization technique to avoid recalculating results for the same states.

# ### Approach
# 1. **Define States**:
#    - `i`: the current day.
#    - `buying`: a boolean indicating whether we are in the state of buying (True) or selling (False).
   
# 2. **Base Case**:
#    - If `i` is beyond the last day, return 0 as no more transactions can be made.

# 3. **Recursive Case**:
#    - If `buying` is True:
#      - **Buy**: Consider buying the stock on day `i` and then recursively find the maximum profit from day `i+1` in the selling state.
#      - **Cooldown**: Skip buying on day `i` and recursively find the maximum profit from day `i+1` still in the buying state.
#      - The result for this state will be the maximum of the two actions.
   
#    - If `buying` is False:
#      - **Sell**: Consider selling the stock on day `i` and then recursively find the maximum profit from day `i+2` (due to the cooldown period) in the buying state.
#      - **Cooldown**: Skip selling on day `i` and recursively find the maximum profit from day `i+1` still in the selling state.
#      - The result for this state will be the maximum of the two actions.

# 4. **Memoization**:
#    - Use a dictionary `dp` to store the results of subproblems to avoid redundant calculations.

# ### Time Complexity
# - **Time**: \(O(n)\), where \(n\) is the number of days, because each state is computed only once due to memoization.
# - **Space**: \(O(n)\), for the memoization dictionary.

# ### Summary
# 1. Define the states and the base case.
# 2. Use recursion to explore all possible actions for each state and memoize the results.
# 3. Return the result for the initial state (day 0, buying).

# Here is the cleaned-up solution without the code:

# 1. **Define a recursive function** to compute the maximum profit starting from a given day in a given state (buying or selling).
# 2. **Base Case**: If the current day is beyond the last day, return 0.
# 3. **Memoization**: Use a dictionary to store the results of previously computed states.
# 4. **Recursive Cases**:
#    - If in the buying state, compute the profit for buying or skipping the current day.
#    - If in the selling state, compute the profit for selling or skipping the current day.
# 5. **Return the maximum profit** for the initial state (day 0, buying). 