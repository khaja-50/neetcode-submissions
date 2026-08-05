class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        z=[]
        for i in range(0,len(nums)):
            
            if i>0 and nums[i]==nums[i-1]:
                continue 
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue 
                fix1=nums[i]
                fix2=nums[j]
                left=j+1
                right=len(nums)-1
                while left<right:
                    f=fix1+fix2
                    r=nums[left]+nums[right]
                    if f+r==target:
                        z.append([fix1,fix2,nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif f+r>target:
                        right-=1
                    else:
                        left+=1
        return z
                    


        