class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1

            for a in range(1, amount + 1):
                nextDp[a] = dp[a]
                if a - coins[i] >= 0:
                     nextDp[a] += nextDp[a - coins[i]]
            dp = nextDp
        return dp[amount] 


### Intuition
# To find the number of ways to make a given amount using a list of coins, we can use dynamic programming. The idea is to build up the solution using the subproblems, where we calculate the number of ways to make every smaller amount using the available coins.

# ### Approach
# 1. **Initialize the DP Table**:
#    - Create a list `dp` where `dp[i]` represents the number of ways to make the amount `i`.
#    - Initialize `dp[0]` to 1 because there is one way to make the amount 0, which is to use no coins.

# 2. **Iterate Over Coins**:
#    - For each coin, update the `dp` table for all amounts from the coin value up to the target amount.
#    - For each amount, add the number of ways to make the current amount minus the coin value to the current number of ways to make the current amount.

# ### Detailed Steps
# 1. **Initialization**:
#    - Create a `dp` list of size `amount + 1` and initialize it with zeros.
#    - Set `dp[0]` to 1.

# 2. **Update the DP Table**:
#    - For each coin, iterate through all amounts from 1 to `amount`.
#    - For each amount, update the number of ways to make that amount by adding the number of ways to make `amount - coin`.

# ### Summary
# 1. Initialize the `dp` list where `dp[0]` is 1.
# 2. For each coin, update the `dp` list for all amounts.
# 3. Return the value in `dp[amount]` which represents the number of ways to make the target amount.

# ### Algorithm Without Code
# 1. **Initialize `dp` array** of size `amount + 1` with zeros and set `dp[0]` to 1.
# 2. **For each coin**:
#    - For each amount from 1 to `amount`:
#      - Update `dp[amount]` by adding `dp[amount - coin]` to it.
# 3. **Return `dp[amount]`** as the result, which is the number of ways to make the target amount using the given coins.