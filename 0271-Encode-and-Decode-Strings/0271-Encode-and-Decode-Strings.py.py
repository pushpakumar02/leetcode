class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res





# The methods `encode` and `decode` are used to convert a list of strings to a single encoded string and vice versa. Here's the intuition and approach for both:

# ### encode
# - **Intuition**: To encode a list of strings into a single string, we need to store the length of each string followed by the string itself.
# - **Approach**:
#   1. Initialize an empty string `res`.
#   2. Iterate through each string `s` in `strs`.
#   3. For each string, append the length of the string followed by a '#' character and the string itself to `res`.
#   4. Finally, return `res`.

# - **Time Complexity**: O(n), where n is the total number of characters in all strings combined. We iterate through each string in `strs` once.
# - **Space Complexity**: O(n), where n is the total number of characters in all strings combined. We create a single string `res` to store the encoded result.

# ### decode
# - **Intuition**: To decode an encoded string into a list of strings, we need to parse the lengths and substrings from the encoded string.
# - **Approach**:
#   1. Initialize an empty list `res` to store the decoded strings.
#   2. Initialize an index `i` to traverse the encoded string `s`.
#   3. While `i` is within the bounds of `s`, do the following:
#      - Find the length of the current string by searching for the '#' character.
#      - Convert the substring from `i` to `j` (excluding '#') to an integer to get the length.
#      - Increment `i` to move past the length delimiter '#'.
#      - Set `j` to `i + length`.
#      - Extract the substring from `s[i:j]` and append it to `res`.
#      - Update `i` to `j` to move past the current string.
#   4. Finally, return `res`.

# - **Time Complexity**: O(n), where n is the length of the encoded string `s`. We traverse `s` once to decode it.
# - **Space Complexity**: O(n), where n is the length of the encoded string `s`. We create a list `res` to store the decoded strings.
