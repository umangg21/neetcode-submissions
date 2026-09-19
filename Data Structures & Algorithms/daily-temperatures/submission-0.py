class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lent = len(temperatures)
        output = [0]*lent
        stack = []
        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                output[prev] = i-prev
            
            stack.append(i)
        return output