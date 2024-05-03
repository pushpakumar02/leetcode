class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l +=1
            while r > l and not self.alphaNum(s[r]):
                r -=1
            if  s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True

    def alphaNum(self, n):
        return (ord('A') <= ord(n) <= ord('Z') or 
                ord('a') <= ord(n) <= ord('z') or 
                ord('0') <= ord(n) <= ord('9'))       #Space Complexity: O(n) | Time Complexity: O(1)

