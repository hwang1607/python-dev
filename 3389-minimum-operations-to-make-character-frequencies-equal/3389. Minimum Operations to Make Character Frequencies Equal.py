class Solution:
    def makeStringGood(self, s: str) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        @cache
        def dp(i, deleted, target):
            if i == 26:
                return 0

            x = count[i]
            if x <= target:
                ans = dp(i + 1, x, target) + x
                increase = min(deleted, target - x)
                cand = dp(i + 1, 0, target) + target - x - increase
                ans = min(ans, cand)
            else:
                ans = dp(i + 1, x - target, target) + x - target
            return ans

        return min(dp(0, 0, target) for target in range(max(count) + 1))