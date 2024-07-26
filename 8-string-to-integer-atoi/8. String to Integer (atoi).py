class Solution:
    def myAtoi(self, s: str) -> int:
        MININT = -(2**31)
        MAXINT = 2**31 - 1

        #must begin with a + - or digit or whitespace

        res = 0
        sign = 1

        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and s[i] == "+":
            i += 1
        elif i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res *= sign
        print(res)

        if res > MAXINT:
            res = MAXINT
        elif res < MININT:
            res = MININT
        return res

    
            
            
        