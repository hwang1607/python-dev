class Solution:
    def isHappy(self, n: int) -> bool:
        tot = n
        seen = set()

        while tot not in seen:
            seen.add(tot)
            if tot == 1:
                return True
            temp = 0
            for d in str(tot):
                temp += int(d)**2
            tot = temp

            