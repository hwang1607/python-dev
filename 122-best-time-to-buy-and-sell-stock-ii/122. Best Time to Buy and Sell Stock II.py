class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        total = 0

        for r in range(len(prices)):
            if prices[r] <= prices[l]:
                l = r
                print(res)
                total += res
                res = 0
            else:
                print(l,r)
                if prices[r] - prices[l] > res:
                    res = prices[r] - prices[l]
                else:
                    total += res
                    res = 0
                    l = r
        
        return total + res


        