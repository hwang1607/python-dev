class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1

        for i in range(len(haystack)):
            if haystack[i: i +len(needle)] == needle:
                return i        
        return -1
        