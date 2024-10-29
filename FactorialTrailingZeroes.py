# https://leetcode.com/problems/factorial-trailing-zeroes
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        #trailing zeros are created by factors of 10, 
        # which are products of 2 and 5. In factorials, there are always more factors of 2 than 5
        # we must calculate the factors of 5
        while n>=5:
            n//=5
            count+=n
        return count
   