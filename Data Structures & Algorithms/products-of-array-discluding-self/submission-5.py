class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n


        for i in range(1, n):
            first = i
            prefix[first] = nums[first-1] * prefix[first-1]


            last = n-1-i
            suffix[last] = nums[last+1] * suffix[last+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res


        