#https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        visited= set()
        while n not in visited:
            visited.add(n)  
            n=self.sumOfSquares(n)
            if n==1:
                return True
        return False
    def sumOfSquares(self,n:int)->int:
        sum=0
        while n:
            digit=(n%10)**2
            sum+=digit
            n//=10
        return sum