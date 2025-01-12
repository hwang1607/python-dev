class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(capacity):
            currload = 0
            daysneeded = 1
            
            for weight in weights:
                if currload + weight > capacity:
                    daysneeded += 1
                    currload = 0
                currload += weight
                if daysneeded > days:
                    return False
            return True
        
        
        
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right)//2

            if canship(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        