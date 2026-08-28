class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        answer=0
        maximum=0
        freq={}
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            maximum=max(freq[s[r]],maximum)
            while (r-l+1)-maximum>k:
                freq[s[l]] -= 1 
                l += 1
            answer=max(answer,r-l+1)
        return answer

