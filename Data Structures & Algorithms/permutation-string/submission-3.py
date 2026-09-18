class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        s1_map =Counter(s1)
        s2_map =Counter(s2[:len(s1)])
        
        l=0
        r= len(s1)

        while r< len(s2):
            if s2_map == s1_map:
                return True
            
            s2_map[s2[l]]-=1 
            l+=1 
            s2_map[s2[r]] = s2_map.get(s2[r],0)+1 
            r+=1 
        
        return s2_map == s1_map

        
        