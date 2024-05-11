class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1 ):
            res[i] *= postfix
            postfix *= nums[i]
        return res


# Intuition:
# - To find the product of all elements except self, we can compute the prefix products and postfix products of each element.

# Approach:
# 1. Initialize an array `res` of the same length as `nums`, where each element is initially set to 1.
# 2. Compute the prefix products:
#    - Initialize a variable `prefix` to 1.
#    - Iterate through the elements of `nums`:
#      - Set `res[i]` to `prefix`.
#      - Update `prefix` by multiplying it with `nums[i]`.
# 3. Compute the postfix products:
#    - Initialize a variable `postfix` to 1.
#    - Iterate through the elements of `nums` in reverse order:
#      - Multiply `res[i]` with `postfix` and update `res[i]`.
#      - Update `postfix` by multiplying it with `nums[i]`.
# 4. Return the `res` array.

# Time Complexity: O(n), where n is the length of the input list `nums`. We traverse the list twice, once to compute prefix products and once to compute postfix products.

# Space Complexity: O(1), excluding the output array. We use a constant amount of extra space for storing variables, and the output array `res`, which is allowed by the problem statement.