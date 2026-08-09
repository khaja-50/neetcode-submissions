class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums)<=1:
                return nums
            else:
                mid= len(nums)//2
                left=mergesort(nums[:mid])
                right=mergesort(nums[mid :])
            return merge(left,right)
        def merge(left,right):
            i=0
            j=0
            a=[]
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    a.append(left[i])
                    i+=1
                else:
                    a.append(right[j])
                    j+=1
            while i<len(left):
                a.append(left[i])
                i+=1
            while j <len(right):
                a.append(right[j])
                j+=1
            return a
        return mergesort(nums)
          