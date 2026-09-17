class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s= len(s)
        if len_s <=1:
            return len_s
        left=0
        seen = set()
        max_count=0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            max_count = max(max_count, right-left+1)
        return max_count