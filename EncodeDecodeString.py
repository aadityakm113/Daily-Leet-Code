#https://neetcode.io/problems/string-encode-and-decode
class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+'#'+s #code the length of the string along with the delimiter
        return res
    def decode(self, s: str) -> List[str]:
        list=[]
        i=0
        while i<len(s):
            j=i #create a pointer that will move until it finds the delimiter
            while s[j]!='#':
                j+=1
            length=int(s[i:j])#length of the string eg 45# length=45. i=0 j=2
            list.append(s[j+1:j+1+length])#start from j+1 as j is at the delimiter go until j+1+length position
            i=j+1+length #move i pointer to the next string
        return list