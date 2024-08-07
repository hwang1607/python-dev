class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l <= r: #if single int
            mid = l + (r-l)//2 #prevent overflow

            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]: #mid on left section
                if target < nums[l] or target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            else: #mid on right section
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l = mid+ 1

        return -1
                