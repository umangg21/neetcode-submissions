class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final =[]
        open = 0
        close = 0

        stack = []

        def backTrack(op, cl):
            if op==cl==n:
                final.append(''.join(stack))
                return
            
            if op < n:
                stack.append("(")
                backTrack(op+1, cl)
                stack.pop()
            
            if cl < op:
                stack.append(")")
                backTrack(op, cl+1)
                stack.pop()

        
        backTrack(0,0)
        return final