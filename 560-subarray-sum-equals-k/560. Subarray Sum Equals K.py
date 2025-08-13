class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cumulativeSum =0

        sumFreq = defaultdict(int)
        sumFreq[0] = 1

        for num in nums:
            cumulativeSum += num
            if (cumulativeSum -k) in sumFreq:
                count += sumFreq[cumulativeSum - k]

            sumFreq[cumulativeSum] += 1
        return count

        