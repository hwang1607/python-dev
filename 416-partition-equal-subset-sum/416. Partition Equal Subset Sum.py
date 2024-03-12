class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) / 2

        for i in range(len(nums) - 1, -1 , -1):
            nextdp = dp.copy()
            for t in dp:
                nextdp.add(t + nums[i])
            dp = nextdp
        return True if target in dp else False