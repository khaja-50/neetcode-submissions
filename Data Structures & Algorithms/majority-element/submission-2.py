class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         r = {}
         for z in nums:
            if z not in r:
                r[z] = 1
            else:
                r[z] += 1
            for i, j in r.items():
                if j > len(nums) // 2:
                    return i
        