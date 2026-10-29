class MedianFinder:

    def __init__(self):
        self.small_maxheap = []
        self.large_minheap = []

        heapq.heapify_max(self.small_maxheap)
        heapq.heapify(self.large_minheap)
    
    def getLens(self):
        small_l = len(self.small_maxheap)
        large_l = len(self.large_minheap)

        return small_l, large_l

    def rebalance(self):
        small_l, large_l = self.getLens()

        if small_l > large_l:
            elem = heapq.heappop_max(self.small_maxheap)
            heapq.heappush(self.large_minheap, elem)
        else:
            elem = heapq.heappop(self.large_minheap)
            heapq.heappush_max(self.small_maxheap, elem)

    def addNum(self, num: int) -> None:
        if len(self.small_maxheap) == 0 or num <= self.small_maxheap[0]:
            heapq.heappush_max(self.small_maxheap, num)
        else:
            heapq.heappush(self.large_minheap, num)
        
        small_l, large_l = self.getLens()

        if abs(small_l - large_l)>1:
            self.rebalance()

    def findMedian(self) -> float:
        small_l, large_l = self.getLens()

        if small_l == large_l:
            return (self.small_maxheap[0]+self.large_minheap[0])/2
        
        elif small_l > large_l:
            return self.small_maxheap[0]
        else:
            return self.large_minheap[0]

