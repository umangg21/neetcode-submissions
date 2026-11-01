class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        row, col = len(grid), len(grid[0])
        visit = set()


        def bfs(r,c):
            if r not in range(row) or c not in range(col) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            direction =[[1,0], [-1,0], [0,1], [0, -1]]

            sum = 1 
            for dr,dc in direction:
                nr, nc = r+dr, c+dc
                sum += bfs(nr,nc)

            return sum

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    maxArea = max(area, maxArea)

        return maxArea

        