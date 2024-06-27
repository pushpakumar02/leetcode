class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
             A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright) 
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1






### Intuition and Approach

# To find the median of two sorted arrays, the goal is to find a position where both arrays can be divided such that the left half contains the same number of elements as the right half (or one more if the total number of elements is odd), and all elements in the left half are less than or equal to all elements in the right half.

# ### Steps and Approach

# 1. **Ensure the first array is the smaller one**:
#    - Swap `A` and `B` if `B` is smaller than `A`. This simplifies the logic since we always binary search on the smaller array.

# 2. **Binary Search**:
#    - Perform binary search on the smaller array (`A`). Initialize `l` and `r` as the start and end indices of `A`.
#    - Calculate the current partition indices for `A` and `B`:
#      - `i` for `A` is the midpoint of `l` and `r`.
#      - `j` for `B` is calculated as `half - i - 2` to ensure that the total number of elements in the left partitions of both arrays equals the total number of elements in the right partitions (or is one less if the total number is odd).

# 3. **Partition and Compare**:
#    - Compare the elements around the partition:
#      - `Aleft` is the maximum element on the left side of `A`.
#      - `Aright` is the minimum element on the right side of `A`.
#      - `Bleft` is the maximum element on the left side of `B`.
#      - `Bright` is the minimum element on the right side of `B`.
#    - If the partition is correct (`Aleft <= Bright` and `Bleft <= Aright`):
#      - If the total number of elements is odd, return the minimum of the right-side elements.
#      - If the total number is even, return the average of the maximum of the left-side elements and the minimum of the right-side elements.
#    - Adjust the binary search range based on the comparisons.

# ### Complexity

# - **Time Complexity**: \(O(\log \min(m, n))\) due to the binary search on the smaller array.
# - **Space Complexity**: \(O(1)\) since we only use a few extra variables.

# ### Implementation

# Here is the code for the approach described:

# ```python
# from typing import List

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         A, B = nums1, nums2
#         total = len(nums1) + len(nums2)
#         half = total // 2

#         if len(B) < len(A):
#             A, B = B, A

#         l, r = 0, len(A) - 1
#         while True:
#             i = (l + r) // 2
#             j = half - i - 2

#             Aleft = A[i] if i >= 0 else float("-inf")
#             Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
#             Bleft = B[j] if j >= 0 else float("-inf")
#             Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

#             if Aleft <= Bright and Bleft <= Aright:
#                 if total % 2:
#                     return min(Aright, Bright)
#                 return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
#             elif Aleft > Bright:
#                 r = i - 1
#             else:
#                 l = i + 1
# ```

# ### Explanation

# 1. **Initialization**:
#    - `A` and `B` are assigned to `nums1` and `nums2` respectively.
#    - Ensure `A` is the smaller array.
#    - `total` is the combined length of both arrays.
#    - `half` is half of the total length (integer division).

# 2. **Binary Search**:
#    - Calculate `i` and `j` as partition indices.
#    - Determine `Aleft`, `Aright`, `Bleft`, and `Bright`.

# 3. **Partition Check**:
#    - Check if the partition is correct.
#    - Adjust the binary search range based on the comparison.

# 4. **Return Result**:
#    - Calculate and return the median based on the partition results.