class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f)-1):
            if f[i - 1] == 0 and f[i] == 0 and f[i +1 ] ==0 :
                f[i] = 1
                n -= 1
        return n <= 0


# Intuition and Approach:

# - We're given a flowerbed represented by a list `flowerbed` of 0s and 1s, where 0 represents an empty plot and 1 represents a planted flower.
# - We're also given an integer `n`, representing the number of new flowers to plant.
# - To determine if we can plant `n` flowers in the flowerbed without violating the condition that flowers can't be adjacent, we add a 0 at the beginning and end of the flowerbed (to handle edge cases).
# - We iterate through the flowerbed and check each position:
#   - If the current plot and its adjacent plots are all empty (i.e., equal to 0), we plant a flower in the current plot.
#   - We decrement `n` after planting a flower.
# - After iterating through the flowerbed, if `n` is less than or equal to 0, it means we can plant all `n` flowers without violating the adjacency condition, so we return True.
# - Otherwise, we return False.

# Time Complexity: O(n), where n is the length of the flowerbed. We iterate through the flowerbed once.

# Space Complexity: O(n), where n is the length of the flowerbed. We create a new list `f` of size `len(flowerbed) + 2`.
