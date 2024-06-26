class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        length = len(word)
        res = 0
        left = 0 
        forbidden = set(forbidden)

        for i in range(length):
            for j in range(max(left, i-10), i+1):
                if word[j:i+1] in forbidden:
                    left = j+1 #get out of forbidden

               

            res = max(res,i-left+1)


        return res
        