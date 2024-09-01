class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for currow in range(1, numRows + 1):
            newrow = [0 for r in range(currow)]
            newrow[0] = 1
            newrow[-1] = 1

            for i in range(1, len(newrow) - 1):
                newrow[i] = res[-1][i-1] + res[-1][i]

            res.append(newrow)
        return res


        