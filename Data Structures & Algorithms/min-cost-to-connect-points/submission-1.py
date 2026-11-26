class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj ={i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        #prism 

        res = 0
        visit = set()

        minH = [[0,0]] #cost, point

        while minH:
            cost, i = heapq.heappop(minH)
            if i in visit: continue 
            res += cost
            visit.add(i)
            for ncost, ni in adj[i]:
                if ni not in visit: 
                    heapq.heappush(minH,[ncost, ni])
        
        return res
