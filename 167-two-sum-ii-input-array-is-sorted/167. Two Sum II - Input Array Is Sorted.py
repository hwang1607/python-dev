class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        
        for i in range(len(numbers)):
            if target - numbers[i] in m:
                return sorted([i+1,m[target - numbers[i]]+1])
            else:
                m[numbers[i]] = i      
        