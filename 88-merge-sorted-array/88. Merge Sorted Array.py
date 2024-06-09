class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        total = m+n-1
        m -= 1
        n -= 1


        for i in range(total, -1, -1):
            if n < 0:
                break
        

            if m < 0 or nums1[m] < nums2[n]:
                nums1[i] = nums2[n]
                n-= 1
            else:
                nums1[i] = nums1[m]
                m -= 1

           