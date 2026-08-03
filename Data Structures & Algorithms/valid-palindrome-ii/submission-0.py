class Solution:
    def validPalindrome(self, s: str) -> bool:
        new=""
        for k in s:
            if k.isalnum:
                new=new+k.lower()
        def ispalindrome(left,right):
            while left<right:
                if new[left]==new[right]:
                    left=left+1
                    right=right-1
                else:
                    return False
            return True
        i=0
        j=len(new)-1
        while i<j:
            if new[i]==new[j]:
                i=i+1
                j=j-1
            else:
                return ispalindrome(i,j-1) or ispalindrome(i+1,j)
        return True
        