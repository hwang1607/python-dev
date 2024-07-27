class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(maxsplit = k)
        #default seperator is whitespace, maxsplit prevents splitting the whole thing

        return " ".join(s[:k])
        