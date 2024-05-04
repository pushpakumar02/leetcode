class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]= nums2
        nums1.sort()

   
# Time Complexity: O((m + n) log(m + n)) - where m is the size of `nums1` and n is the size of `nums2`. The dominating factor is the sorting operation.

# Space Complexity: O(1) - No extra space is used apart from the input arrays, as the modification is done in-place.