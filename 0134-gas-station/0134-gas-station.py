class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        res = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            
            if total < 0:
                total = 0
                res = i + 1
        return res


# ### Intuition
# The problem is to determine the starting gas station index from which we can complete a circular tour of all gas stations. We need to decide the starting point such that the car never runs out of gas.

# ### Approach
# 1. **Initial Check**: 
#    - If the total amount of gas available (`sum(gas)`) is less than the total cost required to travel (`sum(cost)`), it is impossible to complete the circuit. Hence, return `-1` immediately.

# 2. **Greedy Approach**:
#    - Traverse through the gas stations while keeping track of the cumulative gas balance (`total`).
#    - If at any point, the cumulative gas balance becomes negative, it means starting from the previous starting point up to the current point is not feasible. Hence, update the starting point to the next station and reset the cumulative balance.
#    - Finally, the starting point where the cumulative balance never falls below zero by the end of the loop is the desired starting point.

# ### Time and Space Complexities
# - **Time Complexity**: \(O(n)\), where \(n\) is the number of gas stations. We make a single pass through the gas stations.
# - **Space Complexity**: \(O(1)\). We use a constant amount of extra space.



# ### Explanation
# - **Initial Check**:
#   - `if sum(cost) > sum(gas)`: Check if the total gas is less than the total cost. If true, return `-1` as it is not possible to complete the circuit.

# - **Main Loop**:
#   - Initialize `res` to `0`, representing the starting index.
#   - Initialize `total` to `0`, representing the cumulative gas balance.
#   - Iterate through each gas station:
#     - Update the cumulative gas balance with `total += (gas[i] - cost[i])`.
#     - If at any point `total` becomes negative, it means starting from the previous start point to the current point is not feasible:
#       - Reset `total` to `0`.
#       - Update the starting index `res` to `i + 1`.

# - **Return**:
#   - Return `res` as the starting index from which the car can complete the circuit.

# This approach efficiently finds the starting gas station index by ensuring that any negative balance encountered is corrected by resetting the starting point, thus guaranteeing a feasible solution.