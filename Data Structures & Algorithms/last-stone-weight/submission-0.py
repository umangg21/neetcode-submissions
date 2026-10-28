class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneq = stones
        heapq.heapify_max(stoneq)
        while len(stoneq) >1:
            top = heapq.heappop_max(stoneq)
            second = heapq.heappop_max(stoneq)
            
            if top > second:
                diff = top-second
                heapq.heappush_max(stoneq, diff)

        

        return 0 if len(stoneq) == 0 else stoneq[0]
        