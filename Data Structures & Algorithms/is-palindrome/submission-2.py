class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        new = ""
        for k in s:
            if k.isalnum():
                new=new+k.lower()
        j=len(new)-1
        while i<j:
            if new[i]==new[j]:
                i=i+1
                j=j-1

            else:
                return False
        return True