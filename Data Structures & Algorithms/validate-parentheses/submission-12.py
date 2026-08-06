class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for z in s:
            if z in '({[':
                a.append(z)
            else:
                need=pairs[z]
                if not a:
                    return False
                if need != a[-1]:
                    return False
                else:
                    a.pop()
        return len(a)==0

