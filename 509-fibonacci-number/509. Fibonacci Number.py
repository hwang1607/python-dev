class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        arr = [0] * (n+1)
        
        arr[1] = 1
        for x in range(2, len(arr)):
            arr[x] = arr[x-1] + arr[x-2]
            
        return(arr[n])
            
        