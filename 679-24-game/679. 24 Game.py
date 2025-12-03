class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 0.0001

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    
                    new_list = [nums[k] for k in range(len(nums)) if k!= i and k!=j]

                    a,b = nums[i], nums[j]

                    if solve(new_list + [a+b]):
                        return True
                    if solve(new_list + [a-b]):
                        return True
                    if solve(new_list + [b-a]):
                        return True
                    if solve(new_list + [a*b]):
                        return True


                    if b != 0 and solve(new_list + [a/b]):
                        return True
                    if a!= 0 and solve(new_list + [b/a]):
                        return True
            return False
        return solve([float(c) for c in cards])
        