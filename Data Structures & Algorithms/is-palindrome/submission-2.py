class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=""
        for i in s:
            ord_c= ord(i)     
            if (ord_c>=48 and ord_c<=57) or (ord_c>=65 and ord_c<=90) or (ord_c>=97 and ord_c<=122):
                b +=i
        
        b = b.lower()

        i=0
        j=len(b)-1

        while( i<=j and b[i] == b[j]):
            i+=1
            j-=1
        
        return i>j