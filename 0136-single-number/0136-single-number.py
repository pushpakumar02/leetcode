class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res



# ### Intuition and Approach

# The problem requires finding the single number in a list where every other number appears twice. Using the XOR (exclusive or) operation provides an elegant solution due to its properties:

# 1. **Properties of XOR**:
#    - \(a \oplus a = 0\): Any number XORed with itself results in 0.
#    - \(a \oplus 0 = a\): Any number XORed with 0 remains unchanged.
#    - XOR is both commutative and associative, meaning the order of operations does not matter.

# Given these properties, if we XOR all numbers in the list, pairs of identical numbers will cancel each other out (resulting in 0), and the single number will be left.

# ### Approach

# 1. Initialize a variable `res` to 0.
# 2. Iterate through each number in the input list.
# 3. XOR the current number with `res` and store the result back in `res`.
# 4. After processing all numbers, `res` will contain the single number that appears only once in the list.

# ### Time Complexity

# - **Time Complexity**: \(O(n)\)
#   - We iterate through the list of numbers once, performing a constant-time XOR operation for each element. Hence, the overall time complexity is linear with respect to the number of elements in the list.

# ### Space Complexity

# - **Space Complexity**: \(O(1)\)
#   - We use a single extra variable (`res`) regardless of the size of the input list, resulting in constant space usage.

# ### Implementation

# Here's the implementation of the described approach:

# ```python
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         res = 0
#         for n in nums:
#             res ^= n
#         return res
# ```

# ### Explanation

# 1. **Initialization**: `res` is set to 0.
# 2. **Iteration**:
#    - For each number `n` in the list `nums`, we perform `res ^= n`.
#    - This operation will cancel out all pairs of numbers and leave the single number alone in `res`.

# 3. **Result**:
#    - After completing the iteration, `res` holds the number that appears only once.

# This approach leverages the properties of the XOR operation to efficiently solve the problem in both time and space.