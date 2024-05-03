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
        return True                                 #Time Complexity: O(n) | Space Complexity: O(n)



