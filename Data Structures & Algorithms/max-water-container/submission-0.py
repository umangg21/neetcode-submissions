class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_water=0

        while(left<right):
            left_h = heights[left]
            right_h = heights[right]
            min_height = min(left_h, right_h)
            width = abs(right-left)
            totalWater = min_height*width

            max_water = max(max_water, totalWater)

            if left_h <= right_h:
                left+=1
            elif right_h < left_h:
                right-=1
            
        return max_water


            


        