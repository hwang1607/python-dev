class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tcount = collections.Counter(t)
        curr = {k : 0 for k in t}


        l = 0

        have = 0
        need = len(tcount)

        minlen = float('inf')
        res = [0,0]
        
        for r in range(len(s)):
            if s[r] in curr:
                curr[s[r]] += 1
                if curr[s[r]] == tcount[s[r]]:
                    have += 1
                #print(have,need)
                #print(l,r)
                while have == need:

                    if (r - l + 1) < minlen:
                        minlen = min(minlen, r - l + 1)
                        res = [l,r]
                    
                    if s[l] in curr:

                        curr[s[l]] -= 1
                        if curr[s[l]] < tcount[s[l]]:

                            have -= 1
                    
                    l += 1
        l,r = res
        if minlen == float('inf'):
            return ""
        return s[l:r+1]
        