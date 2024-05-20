class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 
                else:
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


### Intuition and Approach

# The task is to locate a target value within a rotated sorted array using binary search. 

# 1. **Binary Search Adaptation**:
#    - Leverage the binary search technique, but adapt it to handle the rotation in the array.

# 2. **Identify Sorted Halves**:
#    - Determine whether the left or right half of the array is sorted by comparing the middle element to the boundary elements.
#    - Use this information to decide which half to discard.

# 3. **Binary Search Steps**:
#    - Initialize pointers `l` (left) and `r` (right) to the start and end of the array.
#    - Iterate while `l` is less than or equal to `r`:
#      - Calculate the middle index `mid`.
#      - If the middle element matches the target, return its index.
#      - If the left half is sorted:
#        - Check if the target lies within this half.
#        - If it does, adjust `r` to `mid - 1` to focus on the left half.
#        - If not, adjust `l` to `mid + 1` to search the right half.
#      - If the right half is sorted:
#        - Check if the target lies within this half.
#        - If it does, adjust `l` to `mid + 1` to focus on the right half.
#        - If not, adjust `r` to `mid - 1` to search the left half.

# 4. **Conclusion**:
#    - The loop ends when `l` exceeds `r`, meaning the target is not found, and return -1.

# ### Complexity
# - **Time Complexity**: \(O(\log n)\), due to the binary search approach that divides the search space in half each iteration.
# - **Space Complexity**: \(O(1)\), as only a constant amount of extra space is used for variables.