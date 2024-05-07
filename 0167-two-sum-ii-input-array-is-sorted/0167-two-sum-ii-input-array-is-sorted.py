class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        for i in range(len(numbers)):
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return



# Intuition and Approach:

# - We're given a sorted list of integers `numbers` and a target integer `target`.
# - To find the two numbers that sum up to `target`, we use a two-pointer approach.
# - We initialize two pointers, `l` and `r`, pointing to the start and end of the list, respectively.
# - We iterate through the list:
#   - At each iteration, we calculate the sum of the numbers at `l` and `r`.
#   - If the sum is greater than `target`, we decrement `r` to reduce the sum.
#   - If the sum is less than `target`, we increment `l` to increase the sum.
#   - If the sum is equal to `target`, we return the indices (1-based) of the two numbers.
# - If we finish iterating through the list without finding a pair that sums up to `target`, we return an empty list.

# Time Complexity: O(n), where n is the number of elements in the `numbers` list. Both pointers `l` and `r` traverse the list at most once.

# Space Complexity: O(1), as we use only a constant amount of extra space regardless of the size of the input. We use variables `l` and `r` to store the positions of the pointers.