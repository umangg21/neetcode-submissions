class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0] if board[0] else [])

        self.mboard = [[False for _ in range(col)] for _ in range(row)]
        def resetMBoard():
            self.mboard = [[False for _ in range(col)] for _ in range(row)]

        def backTrack(x,y,i):
            
            if x < 0 or x >= row or y < 0 or y >= col or i>=len(word) or self.mboard[x][y] == True or board[x][y] != word[i]:
                return False
            
            
            if i == len(word)-1:
                return True       
            self.mboard[x][y] = True
            if backTrack(x-1,y, i+1) or backTrack(x+1,y, i+1) or backTrack(x,y-1, i+1) or backTrack(x,y+1, i+1):
                return True

            self.mboard[x][y] = False
            return False

        for m in range(row):
            for n in range(col):
                resetMBoard()
                if backTrack(m,n,0):
                    return True

        return False
