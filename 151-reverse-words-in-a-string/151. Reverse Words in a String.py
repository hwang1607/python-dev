class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr.reverse()
        arr = " ".join(arr)
        return arr
        