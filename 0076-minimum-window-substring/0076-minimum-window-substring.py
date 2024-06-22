class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == " ": return " "

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resL = [-1, -1], float("inf")
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resL:
                    res = [l, r]
                    resL = (r - l + 1)

                window[s[l]] -= 1    
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res 
        return s[l : r + 1] if resL != float(inf) else ""





### Intuition and Approach

# To solve the problem of finding the minimum window substring in `s` which contains all the characters in `t`, we can use a sliding window approach with two pointers.

# ### Approach

# 1. **Initialization**:
#    - Create dictionaries `countT` and `window` to keep track of the character counts in `t` and the current window in `s`, respectively.
#    - Initialize variables `have` and `need` to track the number of characters in `t` that are satisfied in the current window.
#    - Use `res` to store the best window found so far, and `resL` to store its length.

# 2. **Expand the Window**:
#    - Iterate over `s` with the right pointer `r`.
#    - Add the current character `s[r]` to the `window` dictionary.
#    - If `s[r]` is a character needed (i.e., in `countT`) and its count in `window` matches its count in `countT`, increment `have`.

# 3. **Contract the Window**:
#    - While the current window satisfies all characters in `t` (`have == need`), try to contract it from the left.
#    - If the current window is smaller than the previous best (`resL`), update `res` and `resL`.
#    - Move the left pointer `l` to the right, decrementing the count of `s[l]` in `window`.
#    - If `s[l]` is a character needed and its count in `window` falls below its count in `countT`, decrement `have`.

# 4. **Return Result**:
#    - Extract the substring corresponding to the best window from `res`.
#    - If no valid window was found, return an empty string.

# ### Time Complexity

# - **Time Complexity**: \(O(|s| + |t|)\), where \(|s|\) is the length of the string `s` and \(|t|\) is the length of the string `t`. This is because each character in `s` is processed at most twice (once by the right pointer and once by the left pointer), and constructing the `countT` dictionary takes \(O(|t|)\).
# - **Space Complexity**: \(O(|s| + |t|)\), due to the dictionaries `countT` and `window`.

# ### Implementation

# Here's the implementation of the described approach:

# ```python
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if t == " ":
#             return " "

#         countT, window = {}, {}

#         for c in t:
#             countT[c] = 1 + countT.get(c, 0)
        
#         have, need = 0, len(countT)
#         res, resL = [-1, -1], float("inf")
        
#         l = 0
#         for r in range(len(s)):
#             c = s[r]
#             window[c] = 1 + window.get(c, 0)

#             if c in countT and window[c] == countT[c]:
#                 have += 1
            
#             while have == need:
#                 if (r - l + 1) < resL:
#                     res = [l, r]
#                     resL = (r - l + 1)

#                 window[s[l]] -= 1    
#                 if s[l] in countT and window[s[l]] < countT[s[l]]:
#                     have -= 1
#                 l += 1
        
#         l, r = res 
#         return s[l : r + 1] if resL != float("inf") else ""
# ```

# ### Explanation

# 1. **Initialization**:
#    - `countT` stores the count of each character in `t`.
#    - `window` stores the count of each character in the current window of `s`.
#    - `have` keeps track of how many characters from `t` are currently satisfied in the window.
#    - `need` is the total number of unique characters in `t` that need to be satisfied.

# 2. **Expand the Window**:
#    - Iterate through `s` with `r` and add `s[r]` to `window`.
#    - If `s[r]` is in `countT` and its count in `window` matches its count in `countT`, increment `have`.

# 3. **Contract the Window**:
#    - While `have` equals `need`, update the best window if the current window is smaller.
#    - Decrease the count of `s[l]` in `window`.
#    - If `s[l]` is in `countT` and its count in `window` falls below its count in `countT`, decrement `have`.
#    - Move `l` to the right to try and find a smaller window.

# 4. **Return Result**:
#    - Extract the substring using the indices in `res`.
#    - If no valid window was found (`resL` is still `inf`), return an empty string.
 