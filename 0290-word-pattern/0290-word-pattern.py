class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap = {}
        word = s.split()
        if len(pattern) != len(word):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in hashMap:
                if word[i] in hashMap.values():
                    return False
                hashMap[pattern[i]] = word[i]
            else:
                if hashMap[pattern[i]] != word[i]:
                    return False
        return True                                 




# Intuition and Approach:

# - We're given a pattern and a string `s`, and we need to determine if each character in the pattern corresponds to a unique word in `s`.
# - We use a hashmap to map each character in the pattern to its corresponding word in `s`.
# - We split `s` into words.
# - If the lengths of `pattern` and `s` are different, we return False, as there can't be a one-to-one mapping.
# - We iterate through each character and its corresponding word.
#   - If the character is not in the hashmap:
#     - We check if the word is already mapped to another character. If it is, we return False.
#     - Otherwise, we add the character and its corresponding word to the hashmap.
#   - If the character is in the hashmap, we check if its corresponding word matches the current word. If not, we return False.
# - If we complete the loop without returning False, it means the pattern is valid, and we return True.

# Time Complexity: O(n), where n is the length of the pattern or the number of words in `s`. We iterate through each character of the pattern or each word in `s` once.

# Space Complexity: O(n), where n is the number of unique characters in the pattern or the number of unique words in `s`. We use a hashmap to store mappings, which could potentially store all characters or words.
