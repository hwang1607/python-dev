class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0

        nums = {"I":1, "V":5, "X": 10, "L":50, "C": 100, "D":500, "M":1000}

        i = 0
        while i < len(s):

            if s[i] == "I" and i+1 < len(s) and (s[i+1] == "V" or s[i+1] == "X"):
                if  s[i+1] == "V":
                    res += 4
                elif s[i+1] == "X":
                    res += 9
                i+=2
                continue
            
            if s[i] == "X" and i+1 < len(s) and (s[i+1] == "L" or s[i+1] == "C"):
                if  s[i+1] == "L":
                    res += 40
                elif s[i+1] == "C":
                    res += 90
                i+=2
                continue

            if s[i] == "C" and i+1 < len(s) and (s[i+1] == "D" or s[i+1] == "M"):
                if  s[i+1] == "D":
                    res += 400
                elif s[i+1] == "M":
                    res += 900
                i+=2
                continue

            res += nums[s[i]]
            i += 1
        
        return res
        