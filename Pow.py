#https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n): #wrapper function to make sure the exponent is positive
            if x==0:
                return 0
            if n==0:
                return 1
            res=helper(x,n//2) #break down the number of multiplications eg. 2^10n = 2^5*2^5=(2*(2^2X2^2))^2
            res=res*res
            return x*res if n%2 else res # if exponent is odd
        res=helper(x,abs(n))
        return res if n>=0 else 1/res # if exponent in negative, return the reciprocal of the result
        

        