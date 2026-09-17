class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_sum = 0
        prefix = []
        
        suffix_sum=0
        suffix =[]

        len_h = len(height)
        for i in range(0, len_h):
            right = i
            if right==0:
                prefix_sum = 0
            else:
                prefix_sum= max(prefix_sum, height[right-1])
                
            prefix.append(prefix_sum)
            
            
            left = len_h-1-i
            if left == len_h-1:
                suffix_sum =0
            else:
                suffix_sum = max(suffix_sum, height[left+1])
            suffix.append(suffix_sum)
        
        suffix.reverse()
        toatl_water = 0
        for i,h in enumerate(height):
            water = min(prefix[i], suffix[i])-h
            if water >0:
                toatl_water += water

        return toatl_water