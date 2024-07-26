class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ans = max(self.check(s, i ,i), self.check(s, i ,i+1), ans, key=len)
            
        return(ans)
        
    def check(self,s, l, r):
        while l>=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        print(l,r)
        return s[l+1:r]
        