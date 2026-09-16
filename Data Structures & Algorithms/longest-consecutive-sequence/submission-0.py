class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        st = set()

        for val in nums:
            st.add(val)

        for val in nums:

            if val in st and (val-1) not in st:
                cur = val
                cnt =0

                while cur in st:
                    cnt+=1
                    cur+=1
                
                res = max(res,cnt)
        return res