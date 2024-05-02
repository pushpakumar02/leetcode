class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        return len(word[-1])