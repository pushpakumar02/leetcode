class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res



### Intuition and Approach

# To solve the problem of finding the maximum value in each sliding window of size `k` in the array `nums`, we can use a deque (double-ended queue) to maintain the indices of useful elements within the current window.

# ### Approach

# 1. **Initialization**:
#    - Create an empty deque `q` to store indices.
#    - Create an empty list `res` to store the result.
#    - Initialize pointers `l` and `r` to 0. `l` marks the left end of the window, and `r` marks the right end.

# 2. **Iterate through `nums` with `r`**:
#    - Remove elements from the back of `q` while they are less than the current element `nums[r]`. This ensures that `q` contains indices of elements in decreasing order.
#    - Add the current index `r` to `q`.
#    - If the left pointer `l` is greater than the index at the front of `q`, remove the front element. This ensures that the indices in `q` are always within the bounds of the current window.
#    - If the window size is at least `k` (i.e., `r - l + 1 >= k`), append the maximum element in the current window (i.e., `nums[q[0]]`) to `res` and increment `l` to slide the window to the right.

# 3. **Return Result**:
#    - Return the list `res` containing the maximum values for each sliding window.

# ### Time Complexity

# - **Time Complexity**: \(O(n)\), where \(n\) is the length of the array `nums`. Each element is processed at most twice (once when added to the deque and once when removed), resulting in linear time complexity.
# - **Space Complexity**: \(O(k)\), due to the deque storing at most `k` elements.

# ### Implementation

# Here's the implementation of the described approach:

# ```python
# import collections
# from typing import List

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         q = collections.deque()
#         l = r = 0

#         while r < len(nums):
#             while q and nums[q[-1]] < nums[r]:
#                 q.pop()
#             q.append(r)

#             if l > q[0]:
#                 q.popleft()

#             if (r + 1) >= k:
#                 res.append(nums[q[0]])
#                 l += 1
#             r += 1
#         return res
# ```

# ### Explanation

# 1. **Initialization**:
#    - `q` is used to store the indices of elements in `nums` in decreasing order.
#    - `res` will store the maximum values for each sliding window.

# 2. **Iterate through `nums` with `r`**:
#    - For each `r`, remove elements from the back of `q` while they are less than `nums[r]` to maintain the decreasing order.
#    - Add `r` to `q`.
#    - If the index at the front of `q` is out of the current window, remove it.
#    - If the window has at least `k` elements, append the maximum value (i.e., `nums[q[0]]`) to `res` and increment `l`.

# 3. **Return Result**:
#    - The list `res` contains the maximum values for each sliding window.

# This approach ensures that we efficiently track the maximum values in each sliding window using a deque to maintain the necessary indices.