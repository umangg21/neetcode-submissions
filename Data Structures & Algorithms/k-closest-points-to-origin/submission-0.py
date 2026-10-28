class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        def findDist(x,y):
            return math.sqrt( x**2 + y**2)
        
        minheap = [[findDist(x,y), [x,y]] for x,y in points]
        heapq.heapify(minheap)
        
        while k >0:
            res.append(heapq.heappop(minheap)[1])
            k-=1

        return res