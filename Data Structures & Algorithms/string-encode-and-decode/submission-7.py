class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for st in strs:
            res += str(len(st)) + "#" + st
        
        return res
            

    def decode(self, s: str) -> List[str]:
        
        res = []
        n = len(s)
        i=0
        
        while i < n:
            stlen = ""

            while s[i] != "#":
                stlen += s[i]
                i+=1
            
            len_num = int(stlen)
            i+=1

            temp = s[i:i+len_num]
            res.append(temp)
            i+=len_num
        
        return res


        
        
