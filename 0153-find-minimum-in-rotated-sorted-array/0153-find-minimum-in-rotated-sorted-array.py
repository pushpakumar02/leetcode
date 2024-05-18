class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                res = min(res, nums[l])
                l = m + 1               
            else:
                r = m - 1
        return res



### Intuition and Approach

# 1. **Problem Understanding**:
#    - The array is sorted but rotated, and we need to find the minimum element.
#    - A binary search approach is suitable due to the sorted nature of the array segments.

# 2. **Binary Search Logic**:
#    - Initialize two pointers, `l` (left) and `r` (right), representing the start and end of the array.
#    - Use a binary search to repeatedly divide the array into halves.

# 3. **Key Insight**:
#    - If the middle element `nums[m]` is greater than or equal to the left element `nums[l]`, the left part is sorted.
#      - In this case, update the result with the minimum of the current result and `nums[l]`.
#      - Move the left pointer `l` to `m + 1` to search in the right half.
#    - If the middle element `nums[m]` is less than the left element `nums[l]`, the rotation point is in the left part.
#      - Update the right pointer `r` to `m - 1` to search in the left half.

# 4. **Termination**:
#    - The search continues until the left pointer surpasses the right pointer.
#    - The minimum element is tracked and updated during the search process.

# ### Complexity
# - **Time Complexity**: \(O(\log n)\), where \(n\) is the length of the array due to the binary search approach.
# - **Space Complexity**: \(O(1)\), as only a fixed amount of extra space is used for the pointers and result variable.


