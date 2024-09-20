class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def custom(x,y):
            if x+y > y+x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        
        s = [str(x) for x in nums]


        s.sort(key=cmp_to_key(custom),reverse=True)

        return "".join(s).lstrip('0') or '0'


        



            