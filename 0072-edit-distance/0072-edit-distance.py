class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2)+1) for i in range(len(word1) +1)]

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) +1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] =1 + min(cache[i][j+1], cache[i+1][j], cache[i+1][j+1])
        return cache[0][0]

# ### Intuition
# To find the minimum number of operations required to convert `word1` to `word2`, we can use dynamic programming. The three operations allowed are insertion, deletion, and substitution. The key is to determine the minimum number of these operations needed for each substring of `word1` and `word2`.

# ### Approach
# 1. **Initialization**:
#    - Create a 2D DP table `cache` where `cache[i][j]` represents the minimum number of operations required to convert `word1[i:]` to `word2[j:]`.

# 2. **Base Cases**:
#    - If one of the words is empty, the minimum number of operations needed is the length of the other word.
#    - Initialize the bottom row and rightmost column of the DP table accordingly.

# 3. **DP Table Update**:
#    - Iterate through the DP table from the bottom-right to the top-left.
#    - If the characters `word1[i]` and `word2[j]` are the same, no new operation is needed; thus, `cache[i][j]` is set to `cache[i+1][j+1]`.
#    - If the characters are different, consider the three operations (insertion, deletion, and substitution) and take the minimum of these operations plus one.

# 4. **Result**:
#    - The value at `cache[0][0]` will give the minimum number of operations required to convert the entire `word1` to `word2`.

# ### Time and Space Complexities
# - **Time Complexity**: \(O(n \cdot m)\), where \(n\) and \(m\) are the lengths of `word1` and `word2` respectively.
# - **Space Complexity**: \(O(n \cdot m)\) due to the DP table.
