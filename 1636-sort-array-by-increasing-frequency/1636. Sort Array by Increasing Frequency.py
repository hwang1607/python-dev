class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)

        nums = sorted(nums, key = lambda x: (c[x], -x))
        #bro what you can sort based on tuple
        # so basially this is sorting based on this num in nums : (frequency in the counter, -num)
        #if the second value in tuple wasnt in there it would sort numbers of the same frequency from smallest to highest instead of biggest to smallest
        #this is not an easy question

        return nums
        