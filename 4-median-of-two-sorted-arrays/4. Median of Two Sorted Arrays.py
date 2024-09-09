class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newarr = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                newarr.append(nums1[i])
                i += 1
            else:
                newarr.append(nums2[j])
                j += 1

        if i < len(nums1):
            newarr.extend(nums1[i:])
        elif j < len(nums2):
            newarr.extend(nums2[j:])

        mid = len(newarr) // 2

        if len(newarr) % 2 == 0:
            return (newarr[mid-1] + newarr[mid]) / 2
        else:
            return newarr[mid]

        