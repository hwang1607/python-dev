class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        ltor = [1] * length
        rtol = [1] * length
        res = 0
        #left to right and right to left
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                ltor[i] = ltor[i-1] + 1
        
        for i in range(len(ratings) - 2, -1 , -1):
            if ratings[i] > ratings[i+1]:
                rtol[i] = rtol[i+1] + 1
        
        for i in range(len(ratings)):
            res += max(ltor[i],rtol[i])

        
        return res



