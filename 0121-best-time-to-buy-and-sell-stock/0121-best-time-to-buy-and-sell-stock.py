class Solution:
    def maxProfit(self,prices):
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit


# Intuition and Approach:

# - We're given an array `prices` where `prices[i]` represents the price of a stock on the ith day.
# - To find the maximum profit, we iterate through the array, keeping track of the minimum price (`buy`) seen so far and the maximum profit (`profit`) that can be obtained.
# - We start iterating from the second day because we need at least two days to make a profit.
# - For each day, if the current price (`sell`) is greater than the buy price, we calculate the profit by subtracting the buy price from the sell price and update `profit` if the calculated profit is greater than the current profit.
# - If the current price is less than or equal to the buy price, we update the buy price to the current price.
# - Finally, we return the maximum profit.

# Time Complexity: O(n), where n is the number of elements in the `prices` array. We iterate through the array once.

# Space Complexity: O(1), as we use only a constant amount of extra space regardless of the size of the input. We use variables to store `profit` and `buy`.
