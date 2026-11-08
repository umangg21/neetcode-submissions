class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for p,r in prerequisites:
            preMap[p].append(r)
        
        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True

            cycle.add(crs)
            for p in preMap[crs]:
                if not dfs(p): return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output


        
        