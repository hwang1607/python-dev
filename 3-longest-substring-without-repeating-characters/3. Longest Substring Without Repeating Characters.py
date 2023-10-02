class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cset = set()

        l = 0
        r = 0
        res = 0

        while r < len(s):
            while s[r] in cset:
                cset.remove(s[l])
                l+=1
            res = max(r-l+1, res)
            cset.add(s[r])
            print(cset)
            r += 1

        return res
        