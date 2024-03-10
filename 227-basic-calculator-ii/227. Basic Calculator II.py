class Solution:
    def calculate(self, s: str) -> int:
        ops = {'+','-','*','/'}
        
        stack = []
        lastnum = 0

        curop = '+'

        curnum = 0

        res = 0

        for i,c in enumerate(s):
            if c.isdigit():

                curnum = curnum*10 + int(c)
            if c in ops or i == len(s) - 1:
                print(res, lastnum, curnum)
                if curop == '+':
                    res += lastnum
                    lastnum = curnum
                    #stack.append(curnum)
                elif curop == '-':
                    res += lastnum
                    lastnum = -curnum

                    #stack.append(-curnum)
                elif curop == '*':
                    lastnum *= curnum
                    #stack[-1] *= curnum
                elif curop == "/":
                    lastnum = int(lastnum/ curnum)
                    #stack[-1] =int(stack[-1] / curnum) 
                
                curnum = 0
                curop = c

        return res+lastnum
                