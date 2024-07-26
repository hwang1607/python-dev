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
            digit = int(s[i])

            #if the res is greater than maxint with last digit cut off then you cannot add anything to the result and not overflow it
            # if it is equal to maxint you can only add up to what the last digit of max int is
            if (res > MAXINT // 10) or (res == MAXINT // 10 and digit > MAXINT % 10):
                return MAXINT if sign == 1 else MININT
            
            res = 10 * res + digit
            i += 1

  
        return res * sign

    
            
            
        