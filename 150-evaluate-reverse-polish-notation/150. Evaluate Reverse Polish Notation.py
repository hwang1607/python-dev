class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        numstack = []

        for n in tokens:
            if n == "+":
                n1 = numstack.pop()
                n2 = numstack.pop()

                numstack.append(n2 + n1)
            elif n == "-":
                n1 = numstack.pop()
                n2 = numstack.pop()

                numstack.append(n2 - n1)
            elif n == "*":
                n1 = numstack.pop()
                n2 = numstack.pop()

                numstack.append(n2 * n1)
            elif n == "/":
                n1 = numstack.pop()
                n2 = numstack.pop()

                numstack.append(int(n2 / n1)) # using // doesnt work lmao
            else:
                numstack.append(int(n))

        return numstack[0]
                
        