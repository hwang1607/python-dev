class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0

        for i,n in enumerate(citations):
            if res == len(citations):
                return res
            if n >= i+1:
                res = max(res, i+1)
        return res


        