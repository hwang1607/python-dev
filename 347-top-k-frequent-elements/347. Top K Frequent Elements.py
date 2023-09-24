class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        arr = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1

        for key, value in hmap.items():
            arr[value].append(key)
        
        print(arr)

        res = []
        
        for i in range(len(arr) - 1, -1, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
                