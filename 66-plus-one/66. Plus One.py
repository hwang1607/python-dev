class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = "".join(str(x) for x in digits)
        temp = int(temp) + 1

        return [int(x) for x in str(temp)]
        