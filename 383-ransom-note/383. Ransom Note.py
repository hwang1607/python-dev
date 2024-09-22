class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)

        return all(c1[key] <= c2[key] for key in c1)

        