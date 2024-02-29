class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        a = cost[-2]
        b = cost[-1]

        for i in range(len(cost) - 3, -1, -1): #start at pos[-2]
            temp = a
            a = cost[i] + min(a,b)
            b = temp


        return min(a,b)
        