class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        total = m+n-1
        m -= 1
        n -= 1
        print(n)
       # p = m + n -1 # last index of nums 1

        for i in range(total, -1, -1):
            print(i, m, n)
            if m == -1:
                nums1[i] = nums2[n]
                n-= 1
                continue
            if n == -1:
                nums1[i] = nums1[m]
                m -= 1
                continue

            if nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n-= 1
        


        