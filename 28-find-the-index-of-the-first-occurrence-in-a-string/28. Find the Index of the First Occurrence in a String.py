class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1

        for i in range(len(haystack)):
            temp = i
            for j in range(len(needle)):

                if temp >= len(haystack) or haystack[temp] != needle[j]:
                    break
                if j == len(needle) -1:
                    return temp - len(needle) +1
                temp += 1
        
        return -1
        