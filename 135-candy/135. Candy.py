class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        arr = [1] * length

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                arr[i] = arr[i-1] + 1

        res = arr[-1] #this one isnt counted in loop
        for i in range(len(ratings) - 2, -1 , -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i], arr[i+1] + 1)
            res += arr[i]
        

        
        return res



