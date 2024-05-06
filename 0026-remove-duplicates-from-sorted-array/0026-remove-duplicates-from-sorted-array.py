class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r -1]:
                nums[l] = nums[r]
                l +=1
        return l


# Intuition and Approach:

# - We are given a sorted array `nums` with duplicate elements. 
# - The goal is to modify `nums` in-place to remove duplicates and return the length of the resulting array.
# - We maintain two pointers: `l` (left) and `r` (right).
# - `l` starts from 1, indicating the index to place the next unique element.
# - `r` starts from 1 as well, and it iterates through the array to find unique elements.
# - If `nums[r]` is not equal to `nums[r - 1]`, it means we've encountered a new unique element.
#   - We assign this unique element to `nums[l]`.
#   - Increment `l` to indicate the next position where the next unique element should be placed.
# - This process continues until `r` reaches the end of the array.
# - Finally, we return `l`, which represents the length of the array with duplicates removed.

# Time Complexity: O(n) - where n is the size of the input array `nums`. We iterate through the array once.

# Space Complexity: O(1) - No additional space is used apart from a constant amount of space for the pointers and temporary variables. The operation is done in-place.
