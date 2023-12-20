#https://leetcode.com/problems/palindrome-number/
'''Given an integer x, return true if x is a 
palindrome
, and false otherwise.'''

#string reverse approach
class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst=[]
        y=str(x)
        for i in y:
            lst.append(i)
        rev=[]
        for i in lst[::-1]:
            rev.append(i)
        if rev==lst:
            return True
        else:
            return False
            

