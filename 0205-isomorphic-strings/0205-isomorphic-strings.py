class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in mapST and mapST[c1] != c2) or
                 (c2 in mapTS and mapTS[c2] != c1)):
                 return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True




# Intuition and Approach:

# - The problem is to determine if two strings `s` and `t` are isomorphic, meaning that each character in `s` can be replaced by a character in `t`, and vice versa, while preserving the order.
# - We use two maps, `mapST` to map characters from `s` to `t`, and `mapTS` to map characters from `t` to `s`.
# - We iterate through each character in `s` (or equivalently, `t`) simultaneously.
# - For each character pair `(c1, c2)` at index `i`, we check if `c1` already exists in `mapST` and if its corresponding character in `t` is not equal to `c2`, or if `c2` already exists in `mapTS` and its corresponding character in `s` is not equal to `c1`. If either of these conditions is true, the mapping is invalid, and we return `False`.
# - If both characters `c1` and `c2` are new, we add them to the respective maps.
# - If we complete the loop without finding any invalid mappings, we return `True`.

# Time Complexity: O(n) - where n is the length of either `s` or `t`. We iterate through both strings simultaneously once.

# Space Complexity: O(n) - We use two maps, `mapST` and `mapTS`, each containing at most `n` unique characters. Therefore, the space complexity is linear.
