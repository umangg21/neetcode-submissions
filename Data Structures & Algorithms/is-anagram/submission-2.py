class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS = len(s)
        lent = len(t)

        if lenS != lent:
            return False

        mapS = {}
        mapT = {}

        for i in range(lenS):
            charS = s[i]
            mapS[charS] = mapS[charS] + 1 if charS in mapS else 1

            charT = t[i]
            mapT[charT] = mapT[charT] + 1 if charT in mapT else 1

        for j in mapS:
            if j in mapS and j in mapT and mapS[j] == mapT[j]:
                continue
            else:
                return False
        return True

        