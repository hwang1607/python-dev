class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0

        for i in range(1, len(sequence) // len(word) + 1):
            if word*i in sequence:
                res = i
            else:
                return res
        
        return res