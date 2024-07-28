class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #sorted, non decreasing -> must increase or stay the same
        #remove duplicates in place, return unique elems

        #nums at least 1 item to large num
        #range of each item is -100 to 100

        unique = 0 #index of last unique num
        for i in range(1, len(nums)):
            if nums[unique] != nums[i]:
                unique += 1
                nums[unique], nums[i] = nums[i], nums[unique]


                


        return unique + 1



        