class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26    

            for i in s:
                count[ord(i) - ord("a")]+=1
                
            res[tuple(count)].append(s)
        return res.values()

# Intuition and Approach:

# - We're given a list of strings `strs`, and we need to group anagrams together.
# - To efficiently group anagrams, we can use a hashmap where the keys are tuples representing the count of each character in a string and the values are lists of strings that have the same character counts.
# - We iterate through each string in `strs`:
#   - For each string `s`, we create a count list initialized with zeros.
#   - We iterate through each character in `s` and increment the count of the corresponding character in the count list.
#   - After creating the count list for `s`, we convert it to a tuple to make it hashable, and use it as a key in the hashmap.
#   - We append the string `s` to the list corresponding to the key in the hashmap.
# - Finally, we return the values of the hashmap, which are lists of grouped anagrams.

# Time Complexity: O(n * m), where n is the number of strings in `strs` and m is the maximum length of a string. We iterate through each string in `strs` once and count the characters, which takes linear time.

# Space Complexity: O(n * m), where n is the number of strings in `strs` and m is the maximum length of a string. The hashmap can potentially store all strings, and the count list can be as large as the length of the strings.
