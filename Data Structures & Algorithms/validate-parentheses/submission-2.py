class Solution:
    def isValid(self, s: str) -> bool:
        relatedPop  = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        stack = []
        
        for i in s: 
            if i in ["[", "{", "("]: 
                stack.append(i)
            else:
                if(len(stack)):
                    topElement = stack.pop()
                    if relatedPop[i] != topElement:
                        return False
                else:
                    return False
        
        return True if len(stack) == 0 else False

