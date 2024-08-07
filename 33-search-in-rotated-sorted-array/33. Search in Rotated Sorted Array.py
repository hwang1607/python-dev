class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m


            if nums[m] < nums[l]:
                print("pivot in first half", m)
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                print("second half", m)
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

        
        return -1


            
        