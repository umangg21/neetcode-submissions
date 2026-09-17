class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while(i<j):
            val_i = numbers[i]
            val_j = numbers[j]

            sum = val_i+val_j

            if sum == target:
                return [i+1, j+1]
            
            elif sum > target:
                j=j-1
            
            elif sum < target:
                i=i+1
        
        return []
