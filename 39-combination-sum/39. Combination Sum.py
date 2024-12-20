class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total = 0
        arr = []
        res = []

        def backtrack(i):
            if sum(arr) == target:
                res.append(arr[:])
                return
            if i == len(candidates) or sum(arr) > target:
                return

            arr.append(candidates[i])
            backtrack(i)

            arr.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res

