class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(nums):
            n1 = 0 #two below
            n2 = 0  #one below

            for n in nums:
                temp = max(n + n1, n2)
                n1 = n2
                n2 = temp
            
            return max(n1,n2)
        return max(rob1(nums[1:]), rob1(nums[:-1]))
        
       
    