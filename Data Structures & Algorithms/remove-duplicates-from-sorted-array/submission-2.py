class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=0
        for i in range(1,len(nums)):
            if nums[i]==nums[unique]:
                i=i+1
            else:
                unique=unique+1
                nums[unique]=nums[i]
                i=i+1
        k=unique+1
        return k




       
        