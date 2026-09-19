class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for i in tokens:

            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                last = stack.pop()
                lastSecond = stack.pop()

                if i == "*":
                    stack.append(last*lastSecond)
                elif i == "+":
                    stack.append(last+lastSecond)
                elif i == "-":
                    stack.append(lastSecond-last)
                elif i == "/":
                    stack.append(int(lastSecond/last))
        
        return stack.pop()
        