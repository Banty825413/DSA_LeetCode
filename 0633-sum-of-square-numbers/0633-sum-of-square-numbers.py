class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range (0, math.isqrt(c)+1):
            b= int(math.isqrt(c-a**2))
            if a**2 + b**2 == c :
                return True
            
            
            
        return False
