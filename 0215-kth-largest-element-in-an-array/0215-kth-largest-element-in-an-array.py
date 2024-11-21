class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)



# Complexity
# - **Time Complexity**: \(O(n + k \log n)\)
# - **Space Complexity**: \(O(1)\)