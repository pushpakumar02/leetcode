class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + ([float("inf")] * amount)
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]


### Intuition
# The goal is to find the minimum number of coins needed to make up a given amount using a given set of coin denominations. This problem can be solved efficiently using dynamic programming, where the solution to the problem is built up from solutions to smaller subproblems.

# ### Approach
# 1. **Dynamic Programming Table**: Use an array `dp` where `dp[i]` represents the minimum number of coins needed to make up the amount `i`.
# 2. **Initialization**: Set `dp[0]` to 0 because zero coins are needed to make the amount 0. Initialize all other entries in `dp` to infinity (`float("inf")`) to signify that those amounts are initially unreachable.
# 3. **Filling the DP Table**: Iterate through each amount from 1 to the target amount:
#    - For each coin in the given list of coins, if the coin can be used (i.e., the coin's value is less than or equal to the current amount `i`), update the DP table by considering the minimum coins required.
# 4. **Result**: If the entry `dp[amount]` is still infinity after processing, it means the amount cannot be formed with the given coins, so return -1. Otherwise, return the value at `dp[amount]`.

# ### Time Complexity
# - **Time**: \(O(n \times m)\), where \(n\) is the amount and \(m\) is the number of different coin denominations. Each amount is processed with each coin.
# - **Space**: \(O(n)\), for the DP table storing the minimum coins needed for each amount.

# ### Summary
# 1. Initialize a DP array with `dp[0]` as 0 and all other values as infinity.
# 2. Iterate through each amount and each coin to update the DP array with the minimum number of coins required.
# 3. Return the minimum number of coins for the target amount, or -1 if it's not possible.