class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={
            0:1
        }
        presum=0
        count=0
        for num in nums:
            presum+=num
            need=presum-k
            if need in seen:
                count+=seen[need]
            seen[presum]=seen.get(presum,0)+1
        return count
