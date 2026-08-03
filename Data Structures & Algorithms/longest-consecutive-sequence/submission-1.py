class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k=set(nums)
        if not nums:
            return 0
        maximum=1
        for num in nums:
            if num-1 not in k:
                current=num
                leng=1
                while current+1 in k:
                    leng=leng+1
                    current=current+1
                maximum=max(leng,maximum)
        return maximum



