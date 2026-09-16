class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = {}
        to_mul= 1
        for i in range(len(nums)):
            if i==0:
                to_mul = 1
            else: 
                to_mul = to_mul * nums[i-1]
            prefix_mul[i] = to_mul
        
        
        suffix_mul = {}
        to_mul = 1
        
        for i in range(len(nums),0, -1):
            if i==len(nums):
                to_mul = 1
            else: 
                to_mul = to_mul * nums[i]
            suffix_mul[i-1] = to_mul

        final_mul = []
        for i in range(len(nums)):
            final_mul.append(prefix_mul[i] * suffix_mul[i] )

        return final_mul   
        

