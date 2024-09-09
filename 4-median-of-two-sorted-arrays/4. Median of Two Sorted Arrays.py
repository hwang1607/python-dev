class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newlist = nums1 + nums2

        newlist.sort()

        m = len(newlist) // 2

        if len(newlist) % 2 == 0:
            return (newlist[m] + newlist[m-1]) / 2
        else:
            return newlist[m]



        