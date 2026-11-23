class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for s, t, w in times:
            edges[s].append([t,w])
        
        visit = set()
        minheap = [[0,k]]

        t = 0 

        while minheap:
            w1, c = heapq.heappop(minheap)

            if c in visit: 
                continue

            visit.add(c)
            t = w1

            for node , w2 in edges[c]:
                if node not in visit:
                    heapq.heappush(minheap,[w1+w2, node])
             

        return t if len(visit) == n else -1
        