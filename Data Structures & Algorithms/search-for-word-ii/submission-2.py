class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
        self.index = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        rl = len(board)
        cl = len(board[0])

        root = TrieNode()
        curr = root

        # create Trie
        for (i, word) in enumerate(words):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.eow = True
            curr.index = i

        
        def search(r,c, curr, temp):
            
            if min(r,c) < 0 or r >= rl or c >= cl or not curr or temp[r][c]:
                return False
            now = board[r][c]
            if now not in curr.children:
                return False

            temp[r][c] = True
            curr = curr.children[now]
            if curr.index != -1:
                res.append(words[curr.index])
                curr.index = -1
            
            search(r-1, c, curr, temp) 
            search(r+1, c, curr, temp) 
            search(r, c-1, curr, temp) 
            search(r, c+1, curr, temp)
            temp[r][c] = False

        for r in range(rl):
            for c in range(cl):
                curr = root
                temp=[[False for _ in range(cl)] for _ in range(rl)]
                search(r,c, curr, temp)

        
        return res

        