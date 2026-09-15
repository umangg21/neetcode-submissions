class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a ={}
        for i in nums:
            if i not in a:
                a[i] = 0
            a[i] +=1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num in a:
            freq = a[num]
            buckets[freq].append(num)

        result = []

        for freq in range(len(nums), 0 , -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result

        