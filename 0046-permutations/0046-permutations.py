class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return res


# **Intuition:**

# Permutations involve arranging elements in all possible orders. This code utilizes a backtracking approach to systematically explore these arrangements.

# **Approach:**

# 1. **Initialization:**
#    - An empty result list `res` stores the final permutations.
#    - A temporary solution list `sol` keeps track of the current arrangement being constructed.
#    - `n` holds the length of the input list `nums`.

# 2. **Backtracking Function:**
#    - **Base Case:** If the solution list (`sol`) reaches the length of the input array (`n`), it means a complete permutation has been formed. Append a copy of this solution to the result list (`res`) using slicing (`sol[:])` to avoid modifications in later recursive calls.
#    - **Iterate Through Numbers:** Loop through each element (`x`) in the input list (`nums`).
#      - **Check for Uniqueness:** If the current element (`x`) is not already present in the solution list (`sol`), it's a valid candidate for the current permutation.
#        - Add `x` to the solution list (`sol.append(x)`).
#        - Recursively call `backtrack()` to explore further possibilities with the remaining elements. This deepens the recursion tree.
#        - After the recursive call returns, backtrack by removing `x` from the solution list (`sol.pop()`) to consider other arrangements.

# 3. **Main Function Call:**
#    - Call the `backtrack()` function to initiate the exploration process.

# **Time Complexity:**

# - In the worst case, for each element `x`, we might include it (`sol.append(x)`) and backtrack (`sol.pop()`), leading to a branching factor of 2.
# - The recursion tree can have a depth of `n` (number of elements in the input list).
# - The total number of permutations grows exponentially, resulting in a time complexity of O(n!).

# **Space Complexity:**

# - The recursion stack, in the worst case, can have a depth of `n`.
# - The `sol` list also scales linearly with `n`.
# - Therefore, the space complexity is O(n) for the recursion stack and O(n) for `sol`, totaling O(n). However, due to the space overhead of function calls, the practical space complexity might be slightly higher.

# **Key Points:**

# - Backtracking allows for systematic exploration of all possible permutations.
# - Checking for uniqueness in `sol` ensures no element is included multiple times within a permutation.
# - Slicing (`sol[:])` when appending to the result list (`res`) prevents modifications to the current solution during recursive calls.

# **Additional Considerations:**

# - For large `n`, the exponential time complexity can make this solution impractical. In such cases, consider using alternative approaches like iteratively generating permutations or leveraging libraries like `itertools.permutations`.
# - The space complexity might be a factor for very large input lists. If memory is a concern, explore alternative algorithms that might have lower space requirements.

# I hope this explanation provides a comprehensive understanding of the `permute` function and its complexities.
