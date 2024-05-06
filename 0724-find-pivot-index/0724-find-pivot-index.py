class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            if rightSum == leftSum :
                return i
            leftSum += nums[i]
        return -1                 



# Intuition and Approach:

# - We're given a list of integers `nums`.
# - The pivot index is an index such that the sum of all elements to the left of it is equal to the sum of all elements to its right.
# - To find the pivot index efficiently, we first calculate the total sum of all elements in the list.
# - We initialize a variable `leftSum` to keep track of the sum of elements to the left of the current index.
# - Then, we iterate through the list:
#   - At each index `i`, we calculate the sum of elements to the right of `i` using the formula `total - leftSum - nums[i]`.
#   - If the sum of elements to the right is equal to the sum of elements to the left (`rightSum == leftSum`), we have found the pivot index, so we return `i`.
#   - Otherwise, we update `leftSum` by adding `nums[i]`.
# - If we finish iterating through the list without finding a pivot index, we return -1.

# Time Complexity: O(n), where n is the length of the input list `nums`. We iterate through the list once.

# Space Complexity: O(1), as we use only a constant amount of extra space regardless of the size of the input. We do not use any additional data structures that grow with the size of `nums`.
