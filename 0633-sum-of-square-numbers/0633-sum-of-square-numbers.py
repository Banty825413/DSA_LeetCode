class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square = set()
        for i in range (0,math.isqrt(c)+1 ):
            sqr = i*i
            temp =c - sqr
            square.add(sqr)
            if temp in square :
                return True
            
            
            
        return False
