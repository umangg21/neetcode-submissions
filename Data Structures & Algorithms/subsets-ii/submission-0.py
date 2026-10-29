class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final =[]
        curr = []

        def dfs(i):
            if i>= len(nums):
                final.append(curr.copy())
                return
        

            curr.append(nums[i])
            dfs(i+1)

            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1

            curr.pop()
            dfs(i+1)

        dfs(0)
        return final
        