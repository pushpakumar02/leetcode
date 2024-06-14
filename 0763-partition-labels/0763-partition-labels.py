class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res


### Intuition

# The problem is about partitioning a string into as many parts as possible such that no letter appears in more than one part. The idea is to determine the last occurrence of each character and use this information to decide the partitions. Each partition should stretch from the current position to the furthest last occurrence of any character in that segment.

# ### Approach

# 1. **Calculate Last Occurrences**: First, create a dictionary to store the last occurrence index of each character in the string.
   
# 2. **Traverse and Partition**: Traverse the string while keeping track of the current partition size and the furthest last occurrence index (`end`) for characters encountered so far. When the current index matches the furthest last occurrence index, a partition is completed.

# 3. **Reset for New Partition**: Append the size of the completed partition to the result list and reset the size counter for the next partition.

# ### Time and Space Complexities

# - **Time Complexity**: \(O(N)\), where \(N\) is the length of the string. This is because we traverse the string twice: once to compute the last occurrences and once to determine the partitions.
# - **Space Complexity**: \(O(1)\) extra space, not counting the input and output since the dictionary of last occurrences has at most 26 entries (for each letter of the alphabet).

# ### Implementation

# ```python
# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         # Create a dictionary to store the last occurrence of each character
#         lastIndex = {}
#         for i, c in enumerate(s):
#             lastIndex[c] = i
        
#         res = []
#         size, end = 0, 0
        
#         # Traverse the string to determine partitions
#         for i, c in enumerate(s):
#             size += 1
#             end = max(end, lastIndex[c])
            
#             # If the current index is the end of the partition
#             if i == end:
#                 res.append(size)
#                 size = 0
                
#         return res
# ```

# ### Explanation

# 1. **Calculate Last Occurrences**: As we traverse the string, we update `lastIndex` to record the last occurrence of each character.
# 2. **Traverse and Partition**: During the second traversal, we increment the `size` for each character. For each character, we also update `end` to be the furthest last occurrence of any character seen so far.
# 3. **Complete Partition**: When the current index matches `end`, it indicates the end of a partition. We append the current size to `res` and reset `size` to start counting the next partition.

# This method ensures that each character in a partition does not appear in any subsequent partition, thus meeting the problem's requirements.