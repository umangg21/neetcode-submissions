class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        visit = set()
        directions = [(0,1), (0,-1), (1,0) ,(-1, 0)]

        minH = [[grid[0][0], 0, 0]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N-1 and c == N-1: return t 

            for dr, dc in directions:
                nr, nc = r+dr,  c+dc

                if (min(nr, nc)<0 or max(nr,nc) >= N or (nr,nc) in visit):
                    continue
                
                visit.add((nr,nc))
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
            
        