class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()

        def dfs(i, prev):
            if i in visit: return

            visit.add(i)
            for j in adj[i]:
                if j == prev : continue
                dfs(j, i)
        

        count=0
        for i in range(n):
            if i not in visit:
                count+=1
                dfs(i, -1)
        
        return count