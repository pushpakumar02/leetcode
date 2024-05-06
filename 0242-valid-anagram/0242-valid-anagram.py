class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        return Counter(s) == Counter(t)

        if len(s)!= len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

# Intuition and Approach:

# 1. **Using Sorted Strings**:
#    - We can directly sort both strings `s` and `t` and then compare them. If they are equal, it means `t` is an anagram of `s`.
#    - This approach works because anagrams have the same characters, but their order can be different.
#    - Time Complexity: O(n log n), where n is the length of the longer string between `s` and `t`, due to sorting.
#    - Space Complexity: O(n), where n is the length of the longer string between `s` and `t`, due to the space used by the sorted strings.

# 2. **Using Counter**:
#    - We can use the Counter class from the collections module to count the occurrences of characters in both strings.
#    - We return True if the counters of both strings are equal, indicating that `t` is an anagram of `s`.
#    - Time Complexity: O(n), where n is the length of the longer string between `s` and `t`, due to building the counters.
#    - Space Complexity: O(n), where n is the total number of unique characters in both `s` and `t`, due to the space used by the counters.

# 3. **Using Dictionary**:
#    - We can use two dictionaries to count the occurrences of characters in `s` and `t`.
#    - If the lengths of `s` and `t` are different, they can't be anagrams, so we return False.
#    - Then, we iterate through both strings, updating the counts in the dictionaries.
#    - Finally, we compare the counts in both dictionaries. If they are equal, `t` is an anagram of `s`.
#    - Time Complexity: O(n), where n is the length of the longer string between `s` and `t`, due to iterating through the strings and comparing counts.
#    - Space Complexity: O(n), where n is the total number of unique characters in both `s` and `t`, due to the space used by the dictionaries.

# All three approaches are valid, but the first two are more concise and clear. The third approach, though correct, is less efficient and more verbose.
