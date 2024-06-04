class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        n = len(nums)
        res, sol = [], []

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return 

            if curr_sum > target or i == n:
                return
            
            backtrack(i+1, curr_sum)

            sol.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            sol.pop()
            
        backtrack(0, 0)
        return res

### Intuition and Approach for `combinationSum`

# #### Intuition
# The goal is to find all unique combinations of numbers in `candidates` that sum up to the `target`. We can use a backtracking approach to explore all potential combinations. At each step, we decide whether to include a candidate in the current combination and recursively explore further.

# #### Approach
# 1. **Initialization**:
#    - Create a result list `res` to store all valid combinations.
#    - Create a temporary list `sol` to build each combination during the recursion.

# 2. **Backtracking Function**:
#    - Use a recursive function `backtrack(i, curr_sum)` where `i` is the current index in the `candidates` array, and `curr_sum` is the sum of the current combination.
#    - **Base Case**:
#      - If `curr_sum` equals `target`, add a copy of `sol` to `res` and return.
#      - If `curr_sum` exceeds `target` or `i` reaches the length of `candidates`, return as no valid combination can be formed from here.
#    - **Recursive Case**:
#      - **Exclude the current candidate**: Call `backtrack(i+1, curr_sum)` to skip the current candidate.
#      - **Include the current candidate**: Add `candidates[i]` to `sol`, call `backtrack(i, curr_sum + candidates[i])` to continue including the same candidate (as each candidate can be used unlimited times), and then backtrack by removing the last added candidate from `sol`.

# 3. **Final Result**:
#    - Start the backtracking process from the first index and return the result list `res` which contains all valid combinations.

# #### Time Complexity
# - **Exponential Time**: \(O(2^{\text{target}/\min(\text{candidates})})\).
#   - The time complexity is exponential due to the nature of the problem, where each number can be chosen multiple times, leading to a large number of potential combinations.

# #### Space Complexity
# - **Exponential Space**: \(O(\text{target}/\min(\text{candidates}))\) for the recursion stack in the worst case.
# - **Auxiliary Space**: \(O(\text{target}/\min(\text{candidates}))\) for storing the current combination.

# This method ensures that all possible combinations are explored by making decisions at each step whether to include a candidate or not, and recursively finding all valid combinations that sum up to the target.

