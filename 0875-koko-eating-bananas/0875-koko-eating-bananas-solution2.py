class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            return hours <= h
        
        l = 1
        r = max(piles)

        while l < r:
            k = (l + r) // 2

            if k_works(k):
                r = k
            else:
                l = k + 1
        return l


# video solution : https://www.youtube.com/watch?v=ceYZ5RgwQwQ
### Intuition and Approach

# This problem involves finding the minimum eating speed `k` that allows Koko to eat all the bananas in `h` hours:

# 1. **Binary Search on Speed**:
#    - We need to determine the minimum value of `k` (bananas per hour) such that Koko can finish all piles within `h` hours.
#    - Initialize the search range for `k` between `1` (minimum speed) and the maximum value in `piles` (maximum speed).

# 2. **Helper Function**:
#    - Define a helper function `k_works(k)` to check if a given speed `k` allows Koko to finish within `h` hours.
#    - For each pile, compute the hours needed by dividing the pile size by `k` and summing the results, using `ceil` to handle partial hours.

# 3. **Binary Search**:
#    - Perform binary search within the range `[l, r]`.
#    - Calculate the mid-point `k`.
#    - Use `k_works(k)` to determine if `k` is feasible.
#    - If `k` works, search the left half (lower speeds), otherwise search the right half (higher speeds).
#    - Continue until `l` equals `r`, which gives the minimum feasible speed.

# ### Complexity
# - **Time Complexity**: \(O(n \log m)\), where \(n\) is the number of piles and \(m\) is the maximum pile size.
# - **Space Complexity**: \(O(1)\).