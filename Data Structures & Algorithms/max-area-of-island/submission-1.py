class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        row, col = len(grid), len(grid[0])

        def bfs(r,c):
            if r not in range(row) or c not in range(col) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + bfs(r-1,c) + bfs(r+1, c) + bfs(r,c-1) + bfs(r, c+1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    maxArea = max(area, maxArea)

        return maxArea

        