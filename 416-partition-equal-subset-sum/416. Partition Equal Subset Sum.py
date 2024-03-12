class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) / 2

        for n in nums:
            if n > target:
                return False
            nextdp = dp.copy()
            for t in dp:
                if t + n == target:
                    return True
                if t + n < target:
                    nextdp.add(t + n)
            dp = nextdp
        return True if target in dp else False