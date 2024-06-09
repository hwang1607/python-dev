class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1

        idx = 2

        for i in range(2, len(nums)):
            if not (nums[i] == nums[p1] and nums[i] == nums[p2]):
                nums[idx] = nums[i]
                p1 += 1
                p2 += 1
                idx += 1
            else:
                # p1 += 1
                # p2 += 1
                pass

        
        return idx
                
