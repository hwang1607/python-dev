class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charmap = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res = []

        if not digits:
            return []

        
        def backtrack(i, curr):
            if i >= len(digits):
                res.append(curr)
                return
            
            
            for c in charmap[int(digits[i])]:
                curr += c
                backtrack(i+1, curr)
                curr = curr[:-1]

        backtrack(0, "")
        return res
        