class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = (backtrack(i + 1,total + nums[i] ) + 
                             backtrack(i + 1,total - nums[i]))
            return dp[(i, total)]
        return backtrack(0, 0)

### Intuition
# The problem is to find the number of ways to assign '+' and '-' symbols to a list of numbers such that they sum up to a given target. This is a variation of the subset sum problem which can be solved using dynamic programming.

# ### Approach
# We use a recursive approach with memoization to keep track of the number of ways to achieve a particular sum at each step. The recursion explores all possible combinations by adding and subtracting each number in the list.

# 1. **Recursive Function with Memoization**:
#    - Define a recursive function `backtrack(i, total)` that returns the number of ways to achieve `total` using the numbers from index `i` to the end.
#    - If we reach the end of the list (`i == len(nums)`), check if the `total` equals the target. If it does, return 1; otherwise, return 0.
#    - Use a dictionary `dp` to store the results of subproblems to avoid redundant calculations.
#    - For each number at index `i`, recursively calculate the number of ways by adding and subtracting the current number to the `total`.
#    - Store the result in the `dp` dictionary and return it.

# 2. **Initialize and Start the Recursion**:
#    - Start the recursion with the first index (`0`) and an initial sum (`0`).
#    - Return the result of the initial call.

# ### Time and Space Complexities
# - **Time Complexity**: 
#   - The time complexity is \(O(n \cdot \text{sum(nums)})\) because there are \(n\) indices and each index can have up to \(2 \cdot \text{sum(nums)}\) possible values for the total (considering both positive and negative sums).
# - **Space Complexity**: 
#   - The space complexity is \(O(n \cdot \text{sum(nums)})\) for storing the memoization table plus the recursion stack space, which is also \(O(n)\).

# ### Detailed Steps
# 1. **Initialization**:
#    - Create a dictionary `dp` to store memoization results.
# 2. **Define the Recursive Function**:
#    - `backtrack(i, total)`: 
#      - If `i` is the length of `nums`, return 1 if `total` equals `target`, else return 0.
#      - If `(i, total)` is in `dp`, return `dp[(i, total)]`.
#      - Recursively calculate the number of ways by adding and subtracting the current number to/from the total.
#      - Store the result in `dp[(i, total)]` and return it.
# 3. **Start Recursion**:
#    - Call `backtrack(0, 0)` and return the result.

# ### Algorithm Without Code
# 1. **Create a memoization dictionary `dp`** to store results of subproblems.
# 2. **Define a recursive function `backtrack(i, total)`**:
#    - If `i` equals the length of `nums`, check if `total` equals `target` and return 1 if true, otherwise return 0.
#    - If `(i, total)` is already in `dp`, return `dp[(i, total)]`.
#    - Recursively calculate the number of ways to achieve the target by considering both adding and subtracting the current number:
#      - Add the current number to `total` and call `backtrack(i + 1, total + nums[i])`.
#      - Subtract the current number from `total` and call `backtrack(i + 1, total - nums[i])`.
#    - Store the result in `dp[(i, total)]`.
# 3. **Initialize the recursion**:
#    - Call `backtrack(0, 0)` to start the recursion.
#    - Return the result of `backtrack(0, 0)`.