class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ln = len(nums)
        maxn = -10001
        final = []
        for i in range(k):
            maxn = max(nums[i],maxn)
        final.append(maxn)

        i=1
        j=k

        while (j<ln):
            maxSoFar = final[i-1]
            numtoremove = nums[i-1]
            numtoadd = nums[j]

            if numtoadd > maxSoFar:
                final.append(numtoadd)
                i+=1
                j+=1
            
            elif numtoremove == maxSoFar: 
                maxn = float("-inf")
                for m in range(i, j+1):
                    maxn= max(maxn, nums[m])
                final.append(maxn)
                i+=1
                j+=1
            else:
                final.append(maxSoFar)
                i+=1
                j+=1

        
        return final
                    


        