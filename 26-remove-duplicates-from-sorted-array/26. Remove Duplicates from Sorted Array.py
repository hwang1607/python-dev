class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        new_list = []
        for i in nums:
            if i not in s:
                s.add(i)
                new_list.append(i)
        nums[:len(s)] = new_list
        print(nums)
        return len(new_list)