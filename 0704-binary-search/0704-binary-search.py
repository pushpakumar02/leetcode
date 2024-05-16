class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums ) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1 
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1
        

### Intuition and Approach

# The problem is asking to find the index of a target element in a sorted array. If the element is not present, return -1.

# 1. **Binary Search**:
#    - Initialize two pointers `l` and `r` pointing to the start and end of the array respectively.
#    - While `l` is less than or equal to `r` (indicating there is still a search space):
#      - Calculate the middle index `m` as the average of `l` and `r`.
#      - If `nums[m]` is less than `target`, the target must be in the right half of the array, so update `l = m + 1`.
#      - If `nums[m]` is greater than `target`, the target must be in the left half of the array, so update `r = m - 1`.
#      - If `nums[m]` is equal to `target`, we found the target, so return `m`.
#    - If the target is not found after the loop, return -1.

# 2. **Time Complexity**:
#    - The time complexity of binary search is O(log n), where n is the number of elements in the array. Each step of the binary search reduces the search space by half.

# 3. **Space Complexity**:
#    - The space complexity is O(1) because we are using constant extra space, regardless of the size of the input.
