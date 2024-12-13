class Solution:
    def isValid(self, x: str) -> bool:

        s = []
        closetoopen = {')':'(','}':'{',']':'['}
        

        for c in x:
            if c in closetoopen: 
                if s and s[-1] == closetoopen[c]:
                    s.pop()
                else:
                    return False
            else:#if opening
                s.append(c)
        
        if not s:
            return True
        return False
        