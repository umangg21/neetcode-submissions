class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # // search a row
        start = 0
        end = len(matrix)-1
        initialIndex = 0
        lastIndex = len(matrix[0])-1
        inf = float("inf")
        rowToFind = float("inf")
        while (start <= end):
            mid = start + ((end - start)//2)
            
            if (target in range (matrix[mid][initialIndex], matrix[mid][lastIndex]+1)):
                rowToFind = mid
                break
            
            elif (target < matrix[mid][initialIndex]):
                end = mid-1
            else:
                start = mid+1
                
        if (rowToFind == inf):
            return False
        
        start = 0 
        end = lastIndex
        
        row = matrix[rowToFind]
        while (start <= end):
            mid = start + ((end - start)//2)
            currEl = row[mid]
            if(currEl == target):
                return True
                
            elif (currEl > target):
                end = mid -1
            else:
                start = mid+1
        return False
             