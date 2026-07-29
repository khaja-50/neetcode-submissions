class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t=[]
        for z in nums:
            if z in t:
                return True
            else:
                t.append(z)
        return False