class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            if rightSum == leftSum :
                return i
            leftSum += nums[i]
        return -1                  ## Time complexity: O(n)| Space complexity: O(1)