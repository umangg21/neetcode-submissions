class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row, col = len(board), len(board[0])

        def dfs(x,y):
            if min(x,y) < 0 or x== row or y == col or board[x][y] == "X":
                return
            
            if board[x][y] == "O":
                board[x][y] = "#"
            
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)


        
        for c in range(col):
            if board[0][c] == "O": dfs(0,c)
            if board[row-1][c] == "O": dfs(row-1,c)
        
                
        for r in range(row):
            if board[r][0] == "O": dfs(r,0)
            if board[r][col-1] == "O": dfs(r,col-1)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
        
