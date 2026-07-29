class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}
        for s in strs:
            w=sorted(s)
            k="".join(w) 
            if  k not in groups:
                groups[k]=[]
            groups[k].append(s)
        return list(groups.values())
