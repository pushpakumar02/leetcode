class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]= nums2
        nums1.sort()

   
# Intuition and Approach:

# - Given two sorted arrays `nums1` and `nums2`, and `m` and `n` representing the number of elements in `nums1` and `nums2` respectively.
# - We want to merge `nums2` into `nums1` in-place such that the merged array is also sorted.
# - We can achieve this by appending elements of `nums2` to `nums1` starting from index `m`, effectively merging the two arrays.
# - After merging, we sort the entire `nums1` array to ensure it's in ascending order.

# Time Complexity: O((m + n) log(m + n)) - where m is the size of `nums1` and n is the size of `nums2`. The dominating factor is the sorting operation.

# Space Complexity: O(1) - No additional space is used apart from the inputs and a constant amount of space for variables. The operation is done in-place.
