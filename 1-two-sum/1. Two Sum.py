class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} #number : index

        for i,n in enumerate(nums):
            #i index, n number
            complement = target - n
            if complement in seen:
                return (i, seen[complement])
            
            seen[n] = i
        

            
        