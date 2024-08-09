class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        cursum = 0
        presum = {0:1}

        for n in nums:
            cursum += n
            if cursum - k in presum:
                res += presum[cursum-k]
            
            presum[cursum] = presum.get(cursum,0) + 1
        
        return res
        