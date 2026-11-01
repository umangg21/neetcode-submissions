class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        col= set()
        pos = set()
        neg = set()

        def backTrack(r):
            if r == n:
                copy = ["".join(row) for row in board].copy()
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg:
                    continue 
                
                board[r][c] = "Q"
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)

                backTrack(r+1)

                board[r][c] = "."
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)

        backTrack(0)
        return res

        # self.temp = [["." for _ in range(n)] for _ in range(n)]
        # self.mBoard = [[True for _ in range(n)] for _ in range(n)]
        # res = []

        # def resetBoard():
        #     self.temp = [["." for _ in range(n)] for _ in range(n)]
        #     self.mBoard = [[True for _ in range(n)] for _ in range(n)]

        # def fillboard(x, y):
        #     for i in range(n):
        #         self.mBoard[i][y] = False  # fill col
        #         self.mBoard[x][i] = False  # fill row

        #         pos = x + y
        #         neg = x - y

        #     for i in range(x, n):
        #         for j in range(0, n):
        #             if i + j == pos:
        #                 self.mBoard[i][j] = False
        #             if i - j == neg:
        #                 self.mBoard[i][j] = False

        # def dfs(row):
        #     if row == n:
        #         tr = self.temp.copy()
        #         br = [ "".join(r) for r in tr]
        #         res.append(br)
        #         return


        #     for col in range(n):
        #         if self.mBoard[row][col]:
        #             previous_board = [r[:] for r in self.mBoard]
        #             self.temp[row][col] = "Q"
        #             fillboard(row, col)

        #             dfs(row + 1)


        #             self.temp[row][col] = "."
        #             self.mBoard = previous_board


        # for i in range(n):
        #     resetBoard()
        #     self.temp[0][i] = "Q"
        #     fillboard(0, i)
        #     dfs(1)

        # return res
