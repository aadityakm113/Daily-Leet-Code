# https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/?envType=daily-question&envId=2026-05-27

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lastLow= {}
        firstUp={}
        for i, c in enumerate(word):
            if c.islower():
                lastLow[c] = i
            else:
                if c not in firstUp:
                    firstUp[c]=i
        ans = 0
        for c in string .ascii_lowercase:
            if(
                c in lastLow and c.upper() in firstUp and lastLow[c]<firstUp[c.upper()]
            ):
                ans+=1
        return ans
