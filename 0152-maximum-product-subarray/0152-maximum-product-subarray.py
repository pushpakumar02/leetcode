class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            tmp = n * currMax
            currMax = max(n * currMax, currMin * n , n)
            currMin = min(tmp, currMin * n , n)
            res = max(res, currMax)
        return res

### Intuition
# The problem requires finding the maximum product subarray within a given list of integers. This can be challenging due to the presence of negative numbers, which can turn a large positive product into a large negative one (and vice versa). Hence, it is useful to track both the maximum and minimum products up to the current position.

# ### Approach
# 1. **Initialization**: Start by setting the result `res` to the maximum value in the input list to handle the case of single-element arrays and zeros.
# 2. **Tracking Products**: Use two variables, `currMax` and `currMin`, to track the maximum and minimum product up to the current element, respectively.
# 3. **Iteration**: Iterate through each number in the list:
#    - If the number is zero, reset `currMax` and `currMin` to 1 because the product of any subarray ending at zero would be zero.
#    - Calculate a temporary product of the current number and `currMax`.
#    - Update `currMax` to be the maximum of:
#      - The product of the current number and `currMax`
#      - The product of the current number and `currMin`
#      - The current number itself
#    - Update `currMin` similarly to handle the potential flip due to negative numbers.
#    - Update the result `res` to be the maximum of itself and `currMax`.
# 4. **Result**: The result is the highest value of `currMax` encountered during the iteration.

# ### Time Complexity
# - **Time**: \(O(n)\), where \(n\) is the number of elements in the input list. Each element is processed once.
# - **Space**: \(O(1)\), as only a constant amount of extra space is used regardless of the input size.

# ### Summary
# 1. Initialize the result to the maximum element of the list to handle edge cases.
# 2. Use `currMax` and `currMin` to keep track of the maximum and minimum products up to the current position.
# 3. Iterate through the list, updating `currMax`, `currMin`, and the result as needed.
# 4. Return the maximum product found.