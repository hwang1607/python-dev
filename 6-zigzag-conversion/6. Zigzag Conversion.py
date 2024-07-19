class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        res = ""

        space = numRows * 2 - 2
        i = 0
        while i < len(s):
            res += s[i]
            i += space


        space = numRows * 2 - 2
        #i = 1

        minus = 2

        for i in range(1, numRows-1):
            j = i
            #print(j)

            while j < len(s):
                #print(j,"d")
                res += s[j]
                #print(res)
                if j + space - minus < len(s):
                    res += s[j+space- minus]

                j += space
            minus += 2

        i = numRows - 1
        while i < len(s):
            res += s[i]
            i += space


        return res
                
        