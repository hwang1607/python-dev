class Solution:
    def calculate(self, s: str) -> int:
        ops = {'+','-','*','/'}
        
        stack = []

        curop = '+'

        curnum = 0

        for i,c in enumerate(s):
            if c.isdigit():

                curnum = curnum*10 + int(c)
            if c in ops or i == len(s) - 1:
                if curop == '+':
                    stack.append(curnum)
                elif curop == '-':
                    stack.append(-curnum)
                elif curop == '*':
                    stack[-1] *= curnum
                elif curop == "/":
                    stack[-1] =int(stack[-1] / curnum) 
                
                curnum = 0
                curop = c

        return sum(stack)
                