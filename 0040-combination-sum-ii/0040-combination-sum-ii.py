class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(curr, pos, target):
            if target == 0:
                res.append(curr[:])
                return 
            if target <= 0:
                return 
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(curr, i + 1, target - candidates[i])
                curr.pop()
                prev = candidates[i]
        backtrack([], 0, target)
        return res


# **Intuition:**

# The problem seeks all unique combinations of elements from `candidates` that add up to the target `target`. However, each element can only be used once. To handle this constraint and avoid duplicates, we leverage sorting and backtracking.

# **Approach:**

# 1. **Initialization:**
#    - An empty result list `res` stores the final valid combinations.
#    - `candidates` is sorted to group identical elements together, aiding in duplicate handling.

# 2. **Backtracking Function:**
#    - **Base Cases:**
#      - If `target` reaches 0, it means a valid combination has been found. Append a copy of the current combination (`curr[:]`) to `res`.
#      - If `target` becomes less than 0 (meaning exceeding the target sum), it's an invalid path. Terminate the current exploration.
#    - **Iterate Through Candidates:**
#      - Loop through `candidates` starting from index `pos` (to avoid considering previously included elements).
#      - **Skip Duplicates:** Use a variable `prev` to track the previously considered element. If the current candidate (`candidates[i]`) is the same as `prev`, it signifies a duplicate combination within a group of identical elements. Skip this candidate using `continue`.
#      - **Include Candidate:** Add the current candidate (`candidates[i]`) to the temporary combination list (`curr.append(candidates[i])`).
#      - **Recursive Call:** Make a recursive call to `backtrack` with the following arguments:
#        - Updated `curr` list containing the current combination.
#        - Incremented `i + 1` to explore remaining candidates (skipping duplicates).
#        - Reduced `target - candidates[i]` to reflect the remaining target sum after including the current candidate.
#      - **Backtrack:** After the recursive call returns, remove the added candidate (`curr.pop()`) to consider other possibilities and prevent modifications in later recursive calls.
#      - Update `prev` to the current candidate for duplicate tracking in the next iteration.

# 3. **Main Function Call:**
#    - Call `backtrack([], 0, target)` to initiate the exploration process with an empty initial combination and the target sum.

# **Time Complexity:**

# - In the worst case, for each element `candidates[i]`, we might include it (`curr.append(x)`) and backtrack (`curr.pop()`), leading to a branching factor of 2.
# - However, skipping duplicates using `prev` reduces redundant exploration within groups of identical elements.
# - The recursion tree can have a depth of `n` (number of elements) in the worst case, but the branching factor is reduced due to duplicate handling.
# - The overall time complexity becomes approximately O(2^(n/k)), where `n` is the number of elements and `k` is the average number of distinct elements (assuming a moderate to high level of duplicates).

# **Space Complexity:**

# - The recursion stack, in the worst case, can have a depth of `n`.
# - The `curr` list also scales linearly with `n`.
# - Therefore, the space complexity is O(n) for the recursion stack and O(n) for `sol`, totaling O(n). However, due to the space overhead of function calls, the practical space complexity might be slightly higher.

# **Key Points:**

# - Sorting allows for efficient duplicate handling within groups of identical elements.
# - The `prev` variable effectively skips duplicate combinations and reduces the branching factor.
# - Slicing (`curr[:]`) when appending to the result list (`res`) prevents modifications to the current combination during recursive calls.

# **Additional Considerations:**

# - For large `n`, the time complexity can still be significant. If efficiency is a critical concern, consider alternative approaches like dynamic programming for this specific problem.
# - The space complexity might be a factor for very large input lists. If memory is a concern, explore alternative algorithms that might have lower space requirements.

