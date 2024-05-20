class TimeMap:

    def __init__(self):
        self.map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp]) 

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res  


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)





### Intuition and Approach for `TimeMap`

#### Intuition

# The `TimeMap` class is designed to efficiently handle key-value pairs where each key can have multiple values with associated timestamps. This structure allows for retrieving the value corresponding to a specific timestamp, or the closest timestamp less than or equal to the specified one.

#### Approach

# 1. **Initialization**:
#    - Use a dictionary to store the key-value pairs. Each key maps to a list of `[value, timestamp]` pairs.
   
# 2. **Setting Values**:
#    - For the `set` method, check if the key is already in the dictionary.
#    - If not, initialize an empty list for the key.
#    - Append the `[value, timestamp]` pair to the list associated with the key.
   
# 3. **Getting Values**:
#    - For the `get` method, retrieve the list of `[value, timestamp]` pairs for the given key.
#    - Use binary search to find the largest timestamp that is less than or equal to the specified timestamp:
#      - Initialize two pointers (`l` and `r`) for binary search.
#      - Calculate the mid-point (`m`).
#      - If the timestamp at mid-point is less than or equal to the specified timestamp, update the result to the value at the mid-point and move the left pointer to `m + 1`.
#      - If the timestamp at mid-point is greater than the specified timestamp, move the right pointer to `m - 1`.
#    - After the loop, return the result which contains the value for the largest timestamp less than or equal to the specified timestamp.

# #### Time Complexity
# - **set**: \(O(1)\) for appending to the list.
# - **get**: \(O(\log n)\) for binary search in the list, where \(n\) is the number of entries for a specific key.

# #### Space Complexity
# - **Overall**: \(O(n)\), where \(n\) is the total number of key-value pairs stored. This accounts for the space taken by the dictionary and the lists of pairs.

# ### Summary

# - **Set Operation**: Efficiently appends new `[value, timestamp]` pairs to the list for a key.
# - **Get Operation**: Efficiently retrieves the appropriate value using binary search to handle the timestamp constraint.

# This approach ensures that both operations are efficient and scalable with respect to the number of stored key-value pairs and their timestamps.