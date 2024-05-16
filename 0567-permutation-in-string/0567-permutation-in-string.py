class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2 : return False

        countS1 = [0] * 26
        countS2 = [0] * 26  

        for i in range(n1):
            countS1[ord(s1[i]) - ord("a") ] += 1
            countS2[ord(s2[i]) - ord("a") ] += 1
        
        if countS1 == countS2 : return True

        for i in range(n1, n2):
            countS2[ord(s2[i]) - ord("a") ] += 1
            countS2[ord(s2[i - n1]) - ord("a") ] -= 1
            if countS1 == countS2 : return True
        return  False


### Intuition and Approach

# This problem asks if any permutation of string `s1` is a substring of string `s2`.

# 1. **Initialization**:
#    - Get the lengths of `s1` and `s2`, denoted as `n1` and `n2` respectively.
#    - If the length of `s1` is greater than `s2`, return `False` because `s1` cannot be a substring of `s2`.

# 2. **Frequency Count**:
#    - Initialize two arrays `countS1` and `countS2`, each of size 26 (to store counts of 26 lowercase English letters).
#    - Loop through the first `n1` characters of `s1` and `s2`:
#      - Increment the count of the corresponding character in `countS1` and `countS2`.
#    - If the count arrays of `s1` and `s2` are equal, return `True`, indicating that `s1` is a permutation of a substring of `s2`.

# 3. **Sliding Window**:
#    - Iterate over the remaining characters of `s2`, starting from index `n1`:
#      - Increment the count of the current character and decrement the count of the character `n1` steps back in `countS2`.
#      - If the count arrays of `s1` and `s2` are equal at any point, return `True`.

# 4. **Return**:
#    - If no permutation of `s1` is found in `s2`, return `False`.

# 5. **Time Complexity**:
#    - The time complexity is O(n2) where n2 is the length of string `s2`. We traverse `s2` once and perform constant-time operations for each character.

# 6. **Space Complexity**:
#    - The space complexity is O(1) because the size of `countS1` and `countS2` arrays is fixed (26 characters). We don't consider the input space (s1, s2) in space complexity analysis as it's given.