#https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=''
        for i in s:
            if i.isalnum():
                x+=i.lower()
        return x==x[::-1]

# Solution 2
#with helper function check ascii value
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.alphaNum(s[l]):
                l+=1
            while r>l and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1    
        return True
    def alphaNum(self,x):
        return (ord("a")<= ord(x) <= ord("z") or
        ord("A")<= ord(x) <= ord("Z") or
        ord("0")<= ord(x) <= ord("9"))
        