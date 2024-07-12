class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest = float('inf')
        cache = {} #curr number: remaining to get to amount

        def dfs(curr):
           # nonlocal fewest
            if curr > amount:
                return float('inf')

            if curr == amount:
                return 0
            
            if curr in cache:
                return cache[curr]
            

            fewest = float('inf')

            for c in coins:
                func = dfs(curr + c) + 1
                fewest = min(fewest, func)
            cache[curr] = fewest
            return cache[curr]
                    
        res = dfs(0)

        print(cache)
        if res == float('inf'):
            return -1
        return res
        