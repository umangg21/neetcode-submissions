class Solution:
    def findHours(self,piles, speed):
        sum = 0
        for p in piles:
            sum = sum + math.ceil(p/speed)
        return sum
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        left = 1 
        right  = max(piles)
        minSpeed = right
        
        while (left <= right):
            currSpeed = left + ((right-left)//2)
            hours = self.findHours(piles, currSpeed)
            
            if hours > h:
                left = currSpeed+1
            else:
                minSpeed = min(minSpeed, currSpeed)
                right = currSpeed -1
        
        
        return minSpeed
        
        