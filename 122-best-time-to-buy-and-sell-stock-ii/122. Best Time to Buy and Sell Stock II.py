class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        total = 0
        l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
                total += curr
                curr = 0
            else:
                if prices[r] - prices[l] > curr:
                    curr = prices[r] - prices[l]
                else:
                    l = r
                    total += curr
                    curr = 0

        return total + curr

        