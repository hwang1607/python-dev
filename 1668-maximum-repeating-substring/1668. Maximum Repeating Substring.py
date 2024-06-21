class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        i = 1

        while word*i in sequence:
            res = i
            i += 1
        return res

      