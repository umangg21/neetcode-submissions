class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        row,col = len(grid), len(grid[0])
        fresh = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                
                if grid[r][c] == 1:
                    fresh+=1
        
        if not fresh: return 0

        dist = 0

        def fruit(r,c):
            nonlocal fresh
            if min(r,c) < 0 or r>= row or c>= col or grid[r][c] !=1:
                return 
            grid[r][c] = 2
            fresh -=1
            q.append((r,c))

        while q and fresh>0:
            for i in range(len(q)): 
                r,c = q.popleft()
                
                fruit(r+1,c)
                fruit(r-1,c)
                fruit(r,c+1)
                fruit(r,c-1)

            dist+=1
        
        return dist if not fresh else -1

        