class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums=sorted(nums)

        results=[]
        for i,value in enumerate(snums):

            if i>0 and value == snums[i-1]:
                continue
            
            j=i+1
            k=len(snums)-1
            

            target=-value
            while(j<k):
                latersum= snums[j]+snums[k]
                if latersum == target:
                    results.append([value, snums[j], snums[k]])
                    j+=1
                    k-=1

                    while j<k and snums[j] == snums[j-1]:
                        j+=1
                
                elif latersum < target:
                    j+=1
                elif latersum > target:
                    k-=1
        return results

