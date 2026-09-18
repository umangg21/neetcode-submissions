class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        n= len(s)
        max_f = 0
        res = 0

        for i in range(n):
            freq[s[i]] = freq.get(s[i],0)+1
            max_f = max(max_f, freq[s[i]])

            if i-l+1-max_f>k :
                freq[s[l]]-=1
                l+=1
            
            res = max(res, i-l+1)

        return res
        # max_freq = 0
        # s_freq={}
        # for i in s:
        #     s_freq[i] = s_freq.get(i, 0)+1

        # i = j = 0
        # max_output = 0
        # output = 0
        # op_left=k
        # while j<len(s):
        #     if(s[j]==`):
        #         j+=1
        #         output+=1

        #     else:
        #         if op_left > 0:
        #             j+=1
        #             output+=1
        #             op_left-=1
                    
        #         else:
        #             i=j
        #             op_left=k
        #             output=0

            
        #     max_output = max(max_output, output)
        
        # return max_output