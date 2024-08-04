class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {")":"(", "]":"[","}":"{"}

        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack or pmap[c] != stack[-1]:
                    return False
                stack.pop()
        
        if not stack:
            return True
        return False

        