class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        
        if len(s) != len(t):
            return False
        
        for x in range(len(s)):
            if s[x] not in map1:
                map1[s[x]] = 0
            if t[x] not in map2:
                map2[t[x]] = 0
            map1[s[x]] += 1
            map2[t[x]] += 1
            
        if map1 == map2:
            return True
        else:
            return False
            
        
        