class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i in nums: 
            try: 
                if i in a:
                    return True
                else:
                    a[i] = True;
            except:
                return False
        return False
        