class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                elem = board[r][c]

                if elem == ".": continue

                if ( elem in rows[r] or elem in cols[c] or elem in squares[(r//3, c//3)] ): return False


                rows[r].add(elem)
                cols[c].add(elem)
                squares[(r//3, c//3)].add(elem)
        
        return True