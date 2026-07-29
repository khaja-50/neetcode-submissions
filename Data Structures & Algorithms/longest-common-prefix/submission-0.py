class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest=strs[0]
        for s in strs:
            if len(s)<len(shortest):
                shortest =s
        for i in range(len(shortest)):
            for s in strs:
                if shortest[i]!=s[i]:
                    return shortest[:i]
        return shortest