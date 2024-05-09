class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res



# Intuition:
# - To find all unique triplets with zero sum, we can use a two-pointer approach along with sorting the array.
# - After sorting, we fix one element (let's call it `a`) and use two pointers (`l` and `r`) to search for the remaining two elements.

# Approach:
# 1. Sort the given list of numbers.
# 2. Initialize an empty list `res` to store the result.
# 3. Iterate through the sorted list using index `i`.
#    - Skip duplicates: If `i > 0` and `nums[i] == nums[i-1]`, continue to the next iteration to avoid duplicates.
#    - Set pointers `l = i + 1` and `r = len(nums) - 1`.
#    - While `l < r`, check the sum of elements at indices `i`, `l`, and `r`:
#      - If the sum is less than zero, increment `l`.
#      - If the sum is greater than zero, decrement `r`.
#      - If the sum is zero, add `[nums[i], nums[l], nums[r]]` to the result, increment `l`, and skip duplicate elements by incrementing `l` until a different element is found.
# 4. Return the result list `res`.

# Time Complexity: O(n^2), where n is the length of the input list. The main part of the algorithm is the two-pointer loop, which has a linear time complexity O(n). Sorting the array initially takes O(n log n), but it's dominated by the O(n^2) part.

# Space Complexity: O(1), the extra space used is only for storing variables and the output list, which doesn't depend on the input size.