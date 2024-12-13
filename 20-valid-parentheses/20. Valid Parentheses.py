class Solution:
    def isValid(self, s: str) -> bool:

        flipped = {")":"(", "}":"{", "]":"["}

        stack = []

        for c in s:
            if c in flipped:
                if stack and stack[-1] == flipped[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        return True
        