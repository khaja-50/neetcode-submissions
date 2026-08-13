class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        for token in tokens:
            if token not in ["+","-","*","/"]:
                a.append(int(token))
            elif token=="+":
                r=a.pop()
                z=a.pop()
                ans=r+z
                a.append(ans)
            elif token=="-":
                r=a.pop()
                z=a.pop()
                ans=z-r
                a.append(ans)
            elif token=="*":
                r=a.pop()
                z=a.pop()
                ans=r*z
                a.append(ans)
            elif token=="/":
                r=a.pop()
                z=a.pop()
                ans=int(z/r)
                a.append(ans)
        return a[-1]

        