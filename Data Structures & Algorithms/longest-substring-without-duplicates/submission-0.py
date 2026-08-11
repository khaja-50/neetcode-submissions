class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        maximum=0
        l=0
        r=0
        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]]=r
            else:
                l=max(l,seen[s[r]]+1)
                seen[s[r]]=r
            
            currlen=r-l+1
            maximum=max(currlen,maximum)
        return maximum

        