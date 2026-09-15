class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a= {}
        len_number =len(nums)
        for i in range(len_number):
            diff = target - nums[i]
            if diff in a:
                return [a[diff], i]
            a[nums[i]] = i
                
        