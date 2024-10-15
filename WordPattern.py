#https://leetcode.com/problems/word-pattern/description
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        charToWords={}
        wordsToChar={}
        for c,w in zip(pattern,words):# use zip function to go through both the arrays at a time
            if c in charToWords and charToWords[c]!=w:# checks if the entries in both the maps are same or not.
                return False        
            if w in wordsToChar and wordsToChar[w]!=c:
                return False
            charToWords[c]=w #add the word to the character map
            wordsToChar[w]=c # add the character to the word map
        return True

        