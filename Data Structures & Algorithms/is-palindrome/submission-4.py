class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphaNum(c):
            return (
                (ord(c) >= ord("A") and ord(c) <= ord("Z"))
                or (ord(c) >= ord("a") and ord(c) <= ord("z"))
                or (ord(c) >= ord('0') and ord(c) <= ord('9'))
            )

        l, r = 0, len(s)-1

        while(l<r):
            while l<r and not isAlphaNum(s[l]):
                l +=1
            
            while r > l and not isAlphaNum(s[r]):
                r-=1

            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1

        return True