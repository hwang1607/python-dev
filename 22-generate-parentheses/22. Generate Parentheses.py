class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(numopen, numclose):
            if n == numopen == numclose:
                res.append("".join(stack))
                return

            if numopen < n:
                stack.append("(")
                backtrack(numopen +1, numclose)
                stack.pop()

            if numclose < numopen:
                stack.append(")")
                backtrack(numopen, numclose + 1)
                stack.pop()

        backtrack(0,0)
            
        return(res)
        