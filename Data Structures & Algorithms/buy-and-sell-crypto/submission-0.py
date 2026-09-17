class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_p = len(prices)
        if len_p <=1:
            return 0


        min_p = prices[0]
        max_gain = 0

        for i in range(len_p):
            if min_p > prices[i]:
                min_p = prices[i]
            
            max_gain = max(max_gain, prices[i]-min_p)

        return max_gain
        