class Solution:
    def buildMap(self, aa):
        a = {}
        for i in aa:
            if i in a:
                a[i] = a[i]+1
            else:
                a[i] = 1
        return a

    def isAnagram(self, s: str, t: str) -> bool:
        smap = self.buildMap(s)
        tmap = self.buildMap(t)

        for i in smap: 
            try:
                if smap[i] == tmap[i]:
                    continue
                else:
                    return False
            except:
                return False
        for i in tmap: 
            try:
                if smap[i] == tmap[i]:
                    continue
                else:
                    return False
            except:
                return False
        return True

        