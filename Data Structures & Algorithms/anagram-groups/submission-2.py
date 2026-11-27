class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}
        for word in strs:
            mapS = [0] * 26

            for s in word:
                mapS[ord(s)- ord('a')] +=1

            
            tup =tuple(mapS)
            if tup not in res:
                res[tup] = []
            
            res[tup].append(word)
        
        return list(res.values())