class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        used = [False]* len(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                final.append(curr.copy())
                return 
            
            for i in range(len(nums)):
                print(i, nums[i], used, curr)
                if used[i]:
                    continue

                curr.append(nums[i])
                used[i] = True

                dfs(curr)

                used[i] = False
                curr.pop()
        
        dfs([])

        return final
            



        