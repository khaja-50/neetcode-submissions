# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i=0
        j=n-1
        while i<=j:
            mid=(i+j)//2
            result=guess(mid)
            if result== 0:
                return mid
            elif result== -1:
                j=mid-1
            else:
                i=mid+1    
        return i