class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visit = {}

        for index,num in enumerate(nums):
            comp = target - num

            if num in visit:
                return [visit[num], index]
            else:
                visit[comp] = index 
