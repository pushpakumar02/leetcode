class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tempPrices[d]:
                     tempPrices[d] = prices[s] + p
            prices = tempPrices

        return -1 if prices[dst] == float("inf") else prices[dst]


### Intuition
# To find the cheapest price from a source to a destination with at most `k` stops, we can use a modified version of the Bellman-Ford algorithm. This algorithm is suitable because it can handle the constraint of a limited number of stops.

# ### Approach
# 1. **Initialization**:
#    - Create an array `prices` to keep track of the minimum cost to reach each node, initializing all values to infinity except the source, which is set to 0.

# 2. **Relaxation**:
#    - For `k + 1` iterations (to account for up to `k` stops):
#      - Create a temporary copy of the `prices` array.
#      - For each flight (represented by its start, destination, and price):
#        - If the current price to the start node is not infinity and the cost to reach the destination via this flight is cheaper than the recorded cost in the temporary array, update the temporary array.
#      - Update the main `prices` array with values from the temporary array.

# 3. **Result**:
#    - After the iterations, check the cost to reach the destination. If it is still infinity, return -1 indicating it's not possible within the given constraints. Otherwise, return the computed cost.

# ### Time Complexity
# - **Time**: \(O(k \cdot E)\), where \(k\) is the maximum number of stops, and \(E\) is the number of flights. Each iteration processes all edges.

# ### Space Complexity
# - **Space**: \(O(n)\) for storing the prices array, where \(n\) is the number of nodes.