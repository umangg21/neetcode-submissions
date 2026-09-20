class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums)

        while (start<end):
            mid = int((end-start)/2)+start
            currEl = nums[mid]
            if(currEl == target):
                return mid
            elif (currEl >= target):
                end = mid
            else:
                start = mid+1
        return -1
        