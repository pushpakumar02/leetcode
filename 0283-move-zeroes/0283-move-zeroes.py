class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r], nums[l]
                l +=1
        return nums


# Intuition and Approach:

# - The goal is to move all the zeros in the list `nums` to the end, while maintaining the relative order of the non-zero elements.
# - We maintain a left pointer `l` which indicates the position where the next non-zero element should be placed.
# - We iterate through the list with a right pointer `r`, starting from the beginning.
# - If `nums[r]` is non-zero, we swap it with `nums[l]`, effectively moving it to the position indicated by `l`, and then increment `l`.
# - This approach ensures that all non-zero elements are moved to the beginning of the list, while maintaining their relative order, and all zeros are moved to the end.
# - Finally, we return the modified `nums`.

# Time Complexity: O(n) - where n is the size of the list `nums`. We iterate through the list once.

# Space Complexity: O(1) - No additional space is used apart from a constant amount of space for the pointers and temporary variables. The operation is done in-place.
