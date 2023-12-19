#https://leetcode.com/problems/reverse-integer/
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
import math
class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        max_int=2**31-1
        min_int=-2**31
        while x!=0:
            if(rev>max_int/10 or rev<min_int/10):
                return 0
            num=x%10 if x>0 else x% -10
            rev=rev*10+num
            x=math.trunc(x/10)
        return rev