class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mm = [ "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        res = []
        l = len(digits)
        
        comb = []

        def dfs(i):
            if i >= l:
                if comb: res.append(''.join(comb))
                return

            char = digits[i]
            ss = mm[int(char)]

            for k in ss:
                comb.append(k)
                dfs(i+1)
                comb.pop()


        dfs(0)
        return res
        