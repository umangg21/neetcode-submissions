class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}

        for p,r in prerequisites: 
            preMap[p].append(r)

        visit = set()

        def dfs(c):
            if c in visit:
                return False

            if not preMap[c]:
                return True
            
            visit.add(c)

            for k in preMap[c]:
                if not dfs(k): return False
            
            preMap[c] = []

            visit.remove(c)

            return True
        


        for i in range(numCourses):
            if not dfs(i): return False
        
        return True



        