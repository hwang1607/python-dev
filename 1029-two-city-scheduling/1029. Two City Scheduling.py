class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        # arr = []
        n = len(costs) // 2

        # for i,c in enumerate(costs):
        #     arr.append([c[0] - c[1], i])

        # arr.sort()

        costs.sort(key = lambda x : x[0] - x[1])

        # for x in arr:
        #     if n > 0: #city a
        #         res += costs[x[1]][0]
        #         n -= 1
        #     else: #city b
        #         res += costs[x[1]][1]

        for i in range(n):
            res += costs[i][0] + costs[i+n][1]
        


        return res


        