class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()

        for i in range(len(nums)-1,-1,-1):
            cur =  i-k

            if cur < 0:
                cur = cur % len(temp)
            
            nums[i] = temp[cur]
        