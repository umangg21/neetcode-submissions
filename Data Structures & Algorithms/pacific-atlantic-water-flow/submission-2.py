class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(x,y, visit, prevHeight):
            if x <0 or y<0 or x>= row or y>=col or (x,y) in visit or heights[x][y] < prevHeight:
                return 
            
            visit.add((x,y))

            directions = [[1,0], [-1, 0], [0,1], [0,-1]]
            for dx,dy in directions:
                dfs( x+dx, y+dy, visit, heights[x][y])

        
        for c in range(col):
            dfs(0,c, pac, heights[0][c])
            dfs(row-1,c, atl, heights[row-1][c])
        
                
        for r in range(row):
            dfs(r,0, pac, heights[r][0])
            dfs(r,col-1, atl, heights[r][col-1])
        
        res =[]

        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res

        # res = []
        # row,col = len(heights), len(heights[0])
        

        # def checkTravel(r,c, curr,  dir):
        #     if r < 0 or c <0: 
        #         return True
            
        #     if r == row or c == col:
        #         return True
            
        #     if heights[r][c] > curr:
        #         return False

        #     d=1 #right, down
        #     if dir == 0:
        #         d=-1 #left, up
        #     return checkTravel(r+d, c, heights[r][c], dir) or checkTravel(r, c+d, heights[r][c], dir)
        
        # def canTravel(r,c):
            
        #     leftup = checkTravel(r-1, c, heights[r][c], 0) or checkTravel(r, c-1, heights[r][c], 0)
        #     rightDown = checkTravel(r+1, c, heights[r][c], 1) or checkTravel(r, c+1, heights[r][c], 1)

        #     if leftup and rightDown:
        #         res.append((r,c))
        

        # for r in range(row):
        #     for c in range(col):
        #         canTravel(r,c) 

        # return res
