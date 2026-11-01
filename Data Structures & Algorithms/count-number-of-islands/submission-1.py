class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        visited = set()
        row, col = len(grid), len(grid[0])



        def bfs(rr,cc):
            visited.add((rr,cc))
            
            q = collections.deque()
            q.append((rr,cc))
             
            direction =[[1,0], [-1,0], [0,1], [0, -1]]

            while q:
                r,c = q.popleft()
                for dr,dc in  direction:
                    nr = r + dr
                    nc = c + dc

                    if nr in range(row) and nc in range(col) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))

                    


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and  (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands

        