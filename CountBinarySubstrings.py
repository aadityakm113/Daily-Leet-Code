# https://leetcode.com/problems/count-binary-substrings/
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res=0
        prevCount=0
        i=0
        while i<len(s):
            curCount=1 #count starts from the first digit 
            while i<len(s)-1 and s[i]==s[i+1]: #i keeps moving until it finds a different digit
                curCount+=1 #as soon as a new digit is found, current counter is incremented
                i+=1
            if prevCount>0: #if the previous count is greater than zero that means there are multiple digits and this counter must be updated.
                res+=min(prevCount,curCount) #keeps track of all the pairs 
            prevCount=curCount
            i+=1
        return res

