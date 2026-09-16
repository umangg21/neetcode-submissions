class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for st in strs:
            en+=str(len(st))
            en+="#"
            en+=st
        return en

    def decode(self, s: str) -> List[str]:
        result =[]
        i=0
        n = len(s)

        while i<n:
            len_in_st = ""
            
            while s[i] != "#":
                len_in_st += s[i]
                i+=1
            
            len_in_num = int(len_in_st)
            i+=1
        
            temp = s[i:i+len_in_num]
            result.append(temp)

            i+=len_in_num
        return result


