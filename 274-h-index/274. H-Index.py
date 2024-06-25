class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #solution without sorting
        temp = [0] * (len(citations) + 1)

        for i,n in enumerate(citations):
            if n > len(citations):
                temp[-1] += 1
            else:
                temp[n] += 1
        
        res = 0
        for i in range(len(citations), -1, -1):
            res += temp[i]
            if res >= i:
                return i
        