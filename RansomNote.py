#https://leetcode.com/problems/ransom-note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc=Counter(ransomNote) #Creates a hashmap that keep track of the frequency of each key
        mc=Counter(magazine)

        for ch, c in rc.items(): #ch is the character(key) c is the count(value) of the ransom hashmap
            if mc[ch]<c: # checks if the frequency of the character in the magazine hashmap is lesser than the count of the ransom character
                return False
        return True
        