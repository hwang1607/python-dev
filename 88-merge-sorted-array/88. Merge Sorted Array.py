class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = len(nums1) - 1
        m -= 1
        n -= 1

        while n >= 0:
            #print(m,n,end)
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[end] = nums1[m]
                m -= 1
        
            else:
                print("d")
                nums1[end] = nums2[n]
                n -= 1

            end -= 1
        
     
                

        